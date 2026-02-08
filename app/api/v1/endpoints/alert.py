from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
import uuid
from app.core.database import get_db
from app.schemas.alert import Alert, AlertCreate, AlertWithDistance, AlertStats
from app.schemas.user import User
from app.dependencies import get_current_user, get_current_authority_user
from app.services.alert_service import AlertService
from app.services.notification_service import NotificationService

router = APIRouter()

@router.post("", response_model=Alert, status_code=status.HTTP_201_CREATED)
def create_alert(
    alert_in: AlertCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Créer une nouvelle alerte"""
    alert_service = AlertService(db)
    
    # Vérifier le rôle pour les alertes officielles
    if alert_in.source == "authority" and current_user.role != "authority":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only authorities can create official alerts"
        )
    
    # Créer l'alerte
    alert = alert_service.create_alert(alert_in, current_user.id)
    
    # TODO: Implémenter l'envoi de notifications
    # notification_service = NotificationService()
    # recipient_tokens = get_user_tokens_in_radius(...)
    # notification_service.send_alert_notification(alert, recipient_tokens, current_user.full_name)
    
    return alert

@router.get("/nearby", response_model=List[AlertWithDistance])
def get_nearby_alerts(
    latitude: float = Query(..., description="Latitude de l'utilisateur"),
    longitude: float = Query(..., description="Longitude de l'utilisateur"),
    radius: float = Query(5000, description="Rayon de recherche en mètres", ge=100, le=20000),
    alert_types: Optional[List[str]] = Query(None, description="Filtrer par types d'alerte"),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Récupérer les alertes à proximité"""
    alert_service = AlertService(db)
    
    # Convertir les types si fournis
    types = None
    if alert_types:
        types = [t.lower() for t in alert_types]
    
    return alert_service.get_nearby_alerts(
        latitude=latitude,
        longitude=longitude,
        radius=radius,
        alert_types=types,
        exclude_user_id=current_user.id
    )

@router.get("/my-alerts", response_model=List[Alert])
def get_my_alerts(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Récupérer les alertes créées par l'utilisateur"""
    from app.crud.crud_alert import crud_alert
    return crud_alert.get_multi(
        db, skip=skip, limit=limit, user_id=current_user.id
    )

@router.get("/{alert_id}", response_model=Alert)
def get_alert(
    alert_id: uuid.UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Récupérer une alerte spécifique"""
    from app.crud.crud_alert import crud_alert
    alert = crud_alert.get(db, alert_id=alert_id)
    if not alert:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Alert not found"
        )
    
    # Vérifier si l'alerte est supprimée
    if alert.status == "deleted":
        raise HTTPException(
            status_code=status.HTTP_410_GONE,
            detail="Alert has been deleted"
        )
    
    return alert

@router.get("/stats", response_model=AlertStats)
def get_stats(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_authority_user)
):
    """Récupérer les statistiques des alertes (admin/authority only)"""
    alert_service = AlertService(db)
    stats = alert_service.get_alert_stats()
    return AlertStats(**stats)

@router.delete("/cleanup-expired")
def cleanup_expired_alerts(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin_user)
):
    """Nettoyer les alertes expirées (admin only)"""
    alert_service = AlertService(db)
    deleted_count = alert_service.cleanup_expired_alerts()
    return {"deleted_count": deleted_count}