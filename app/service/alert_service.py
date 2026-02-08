from typing import List, Optional
from sqlalchemy.orm import Session
import uuid
from datetime import datetime
from app.crud import crud_alert, crud_report
from app.schemas.alert import AlertCreate, AlertWithDistance
from app.core.config import settings

class AlertService:
    def __init__(self, db: Session):
        self.db = db
    
    def create_alert(self, alert_data: AlertCreate, user_id: uuid.UUID):
        """Crée une nouvelle alerte"""
        return crud_alert.create(self.db, obj_in=alert_data, user_id=user_id)
    
    def get_nearby_alerts(
        self,
        latitude: float,
        longitude: float,
        radius: float = 5000,
        alert_types: Optional[List[str]] = None,
        exclude_user_id: Optional[uuid.UUID] = None
    ) -> List[AlertWithDistance]:
        """Récupère les alertes à proximité"""
        results = crud_alert.get_nearby(
            self.db,
            latitude=latitude,
            longitude=longitude,
            radius=radius,
            alert_types=alert_types,
            exclude_user_id=exclude_user_id
        )
        
        alerts_with_distance = []
        for alert, distance in results:
            alert_dict = alert.__dict__.copy()
            alert_dict['distance'] = distance
            alerts_with_distance.append(AlertWithDistance(**alert_dict))
        
        return alerts_with_distance
    
    def report_alert(self, alert_id: uuid.UUID, user_id: uuid.UUID):
        """Signale une alerte comme fausse"""
        # Vérifier si l'utilisateur a déjà signalé cette alerte
        existing_report = crud_report.get_by_alert_and_user(
            self.db, alert_id=alert_id, user_id=user_id
        )
        
        if existing_report:
            raise ValueError("User already reported this alert")
        
        # Créer le signalement
        report_data = {"alert_id": alert_id}
        crud_report.create(self.db, obj_in=report_data, user_id=user_id)
        
        # Incrémenter le compteur de signalements
        return crud_alert.increment_report_count(self.db, alert_id=alert_id)
    
    def cleanup_expired_alerts(self):
        """Nettoie les alertes expirées"""
        return crud_alert.delete_expired(self.db)
    
    def get_alert_stats(self):
        """Récupère les statistiques des alertes"""
        return crud_alert.get_stats(self.db)