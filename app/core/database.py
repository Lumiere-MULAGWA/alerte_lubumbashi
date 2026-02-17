from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Pour MySQL, pas besoin de check_same_thread
engine = create_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG,
    pool_size=5,  # Connection pool
    max_overflow=10
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()