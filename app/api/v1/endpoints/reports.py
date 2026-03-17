from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import uuid
from app.core.database import get_db
from app.schemas.report import Report, ReportCreate
from app.schemas.alert import Alert
from app.schemas.user import User
from app.dependencies import get_current_user
from app.service.alert_service import AlertService

router = APIRouter()

@router.post("", response_model=Alert)
def report_alert(
    report_in: ReportCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Signaler une alerte comme fausse"""
    alert_service = AlertService(db)
    
    # Vérifier que l'alerte existe
    from app.crud.crud_alert import crud_alert
    alert = crud_alert.get(db, alert_id=report_in.alert_id)
    if not alert:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Alert not found"
        )
    
    # Ne pas signaler ses propres alertes
    if alert.user_id == current_user.id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot report your own alert"
        )
    
    # Ne pas signaler les alertes officielles
    if alert.is_official:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Cannot report official alerts"
        )
    
    # Ne pas signaler les alertes déjà supprimées
    if alert.status == "deleted":
        raise HTTPException(
            status_code=status.HTTP_410_GONE,
            detail="Alert already deleted"
        )
    
    try:
        updated_alert = alert_service.report_alert(
            alert_id=report_in.alert_id,
            user_id=current_user.id
        )
        
        # TODO: Notifier les utilisateurs si l'alerte est limitée/supprimée
        # if updated_alert.status in ["limited", "deleted"]:
        #     notification_service = NotificationService()
        #     recipient_tokens = get_subscribed_users_tokens(alert.id)
        #     notification_service.send_alert_status_update(updated_alert, recipient_tokens)
        
        return updated_alert
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )