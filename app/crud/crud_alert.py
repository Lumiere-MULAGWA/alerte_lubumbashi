from typing import Optional, List, Tuple
from sqlalchemy.orm import Session
from sqlalchemy import func, text
import uuid
from datetime import datetime, timedelta
from app.models.alert import Alert, AlertStatus
from app.schemas.alert import AlertCreate
from app.core.config import settings

class CRUDAlert:
    def get(self, db: Session, alert_id: uuid.UUID) -> Optional[Alert]:
        return db.query(Alert).filter(Alert.id == alert_id).first()
    
    def get_multi(
        self, 
        db: Session, 
        skip: int = 0, 
        limit: int = 100,
        user_id: Optional[uuid.UUID] = None,
        status: Optional[AlertStatus] = None
    ) -> List[Alert]:
        query = db.query(Alert)
        
        if user_id:
            query = query.filter(Alert.user_id == user_id)
        if status:
            query = query.filter(Alert.status == status)
        
        query = query.order_by(Alert.created_at.desc())
        return query.offset(skip).limit(limit).all()
    
    def get_nearby(
        self,
        db: Session,
        latitude: float,
        longitude: float,
        radius: float = 5000,
        alert_types: Optional[List[str]] = None,
        exclude_user_id: Optional[uuid.UUID] = None
    ) -> List[Tuple[Alert, float]]:
        """Retourne les alertes à proximité avec leur distance"""
        point = f"POINT({longitude} {latitude})"
        
        query = db.query(
            Alert,
            func.ST_Distance(
                Alert.location,
                func.ST_GeomFromText(point, 4326)
            ).label('distance')
        ).filter(
            func.ST_DWithin(
                Alert.location,
                func.ST_GeomFromText(point, 4326),
                radius
            ),
            Alert.status != AlertStatus.DELETED,
            Alert.expires_at > datetime.utcnow()
        )
        
        if alert_types:
            query = query.filter(Alert.type.in_(alert_types))
        if exclude_user_id:
            query = query.filter(Alert.user_id != exclude_user_id)
        
        query = query.order_by('distance')
        return query.all()
    
    def create(self, db: Session, obj_in: AlertCreate, user_id: uuid.UUID) -> Alert:
        # Calcul de la date d'expiration
        expires_at = datetime.utcnow() + timedelta(hours=settings.ALERT_DURATION_HOURS)
        
        # Création de la géométrie PostGIS
        location = f"POINT({obj_in.longitude} {obj_in.latitude})"
        
        db_alert = Alert(
            title=obj_in.title,
            description=obj_in.description,
            type=obj_in.type,
            source=obj_in.source,
            is_official=(obj_in.source == "authority"),
            location=location,
            radius=obj_in.radius,
            user_id=user_id,
            expires_at=expires_at
        )
        
        db.add(db_alert)
        db.commit()
        db.refresh(db_alert)
        return db_alert
    
    def increment_report_count(self, db: Session, alert_id: uuid.UUID) -> Optional[Alert]:
        alert = self.get(db, alert_id)
        if not alert:
            return None
        
        alert.report_count += 1
        
        # Vérifier les seuils
        if alert.report_count >= settings.ALERT_DELETE_THRESHOLD:
            alert.status = AlertStatus.DELETED
        elif alert.report_count >= settings.ALERT_LIMIT_THRESHOLD:
            alert.status = AlertStatus.LIMITED
        
        db.add(alert)
        db.commit()
        db.refresh(alert)
        return alert
    
    def delete_expired(self, db: Session) -> int:
        """Supprime les alertes expirées et retourne le nombre supprimé"""
        result = db.query(Alert).filter(
            Alert.expires_at <= datetime.utcnow(),
            Alert.status != AlertStatus.DELETED
        ).update(
            {Alert.status: AlertStatus.DELETED}
        )
        db.commit()
        return result
    
    def get_stats(self, db: Session) -> dict:
        stats = {}
        
        # Total par statut
        status_counts = db.query(
            Alert.status,
            func.count(Alert.id)
        ).group_by(Alert.status).all()
        
        stats['by_status'] = dict(status_counts)
        
        # Total par type
        type_counts = db.query(
            Alert.type,
            func.count(Alert.id)
        ).group_by(Alert.type).all()
        
        stats['by_type'] = dict(type_counts)
        
        # Alertes aujourd'hui
        today = datetime.utcnow().date()
        today_count = db.query(Alert).filter(
            func.date(Alert.created_at) == today
        ).count()
        
        stats['today'] = today_count
        
        return stats

crud_alert = CRUDAlert()