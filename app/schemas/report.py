from pydantic import BaseModel
import uuid
from datetime import datetime

class ReportBase(BaseModel):
    alert_id: uuid.UUID

class ReportCreate(ReportBase):
    pass

class ReportInDB(ReportBase):
    id: uuid.UUID
    user_id: uuid.UUID
    created_at: datetime
    
    class Config:
        from_attributes = True

class Report(ReportInDB):
    pass