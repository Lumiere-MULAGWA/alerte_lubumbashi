from sqlalchemy import text
from app.database import engine
from app.models.base import Base




def init_db():
with engine.begin() as conn:
# Activer PostGIS
conn.execute(text("CREATE EXTENSION IF NOT EXISTS postgis"))
Base.metadata.create_all(bind=conn)