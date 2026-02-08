from typing import List
import uuid
from pyfcm import FCMNotification
from app.core.config import settings
from app.schemas.alert import Alert
from app.schemas.user import User

class NotificationService:
    def __init__(self):
        self.push_service = None
        if settings.FCM_SERVER_KEY:
            self.push_service = FCMNotification(api_key=settings.FCM_SERVER_KEY)
    
    def send_alert_notification(
        self,
        alert: Alert,
        recipient_tokens: List[str],
        sender_name: str = "Un citoyen"
    ):
        """Envoie une notification push pour une nouvelle alerte"""
        if not self.push_service or not recipient_tokens:
            return
        
        # Préparation du message
        title = f"⚠️ Nouvelle alerte: {alert.title}"
        
        if alert.is_official:
            title = f"🚨 ALERTE OFFICIELLE: {alert.title}"
            sender_name = "Autorités"
        
        message = f"{sender_name} - {alert.type.value}"
        if alert.description:
            message = f"{message}: {alert.description[:100]}..."
        
        data_message = {
            "type": "new_alert",
            "alert_id": str(alert.id),
            "alert_type": alert.type.value,
            "latitude": str(alert.location.y),
            "longitude": str(alert.location.x),
            "is_official": str(alert.is_official)
        }
        
        # Envoi groupé
        self.push_service.notify_multiple_devices(
            registration_ids=recipient_tokens,
            message_title=title,
            message_body=message,
            data_message=data_message,
            sound="default",
            badge=1
        )
    
    def send_alert_status_update(self, alert: Alert, recipient_tokens: List[str]):
        """Notifie du changement de statut d'une alerte"""
        if not self.push_service or not recipient_tokens:
            return
        
        if alert.status == "deleted":
            title = "Alerte supprimée"
            body = f"L'alerte '{alert.title}' a été supprimée suite à plusieurs signalements"
        elif alert.status == "limited":
            title = "Alerte limitée"
            body = f"L'alerte '{alert.title}' a été limitée suite à des signalements"
        else:
            return
        
        data_message = {
            "type": "alert_update",
            "alert_id": str(alert.id),
            "new_status": alert.status
        }
        
        self.push_service.notify_multiple_devices(
            registration_ids=recipient_tokens,
            message_title=title,
            message_body=body,
            data_message=data_message
        )