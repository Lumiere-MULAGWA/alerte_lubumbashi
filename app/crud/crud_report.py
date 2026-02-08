from typing import Optional
from sqlalchemy.orm import Session
import uuid
from app.models.report import Report
from app.schemas.report import ReportCreate

class CRUDReport:
    def get(self, db: Session, report_id: uuid.UUID) -> Optional[Report]:
        return db.query(Report).filter(Report.id == report_id).first()
    
    def get_by_alert_and_user(
        self, 
        db: Session, 
        alert_id: uuid.UUID, 
        user_id: uuid.UUID
    ) -> Optional[Report]:
        return db.query(Report).filter(
            Report.alert_id == alert_id,
            Report.user_id == user_id
        ).first()
    
    def create(self, db: Session, obj_in: ReportCreate, user_id: uuid.UUID) -> Report:
        db_report = Report(
            alert_id=obj_in.alert_id,
            user_id=user_id
        )
        db.add(db_report)
        db.commit()
        db.refresh(db_report)
        return db_report
    
    def delete(self, db: Session, report_id: uuid.UUID) -> bool:
        report = self.get(db, report_id)
        if not report:
            return False
        
        db.delete(report)
        db.commit()
        return True

crud_report = CRUDReport()