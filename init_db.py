# init_mysql.py
import os
import sys

os.environ["DATABASE_URL"] = "mysql+pymysql://alert_user:strong_password@localhost:3306/alert_db"

from app.core.database import engine, Base
from app.models.users import User
from app.models.alert import Alert
from app.models.report import Report

print("🚀 Création des tables MySQL...")
Base.metadata.create_all(bind=engine)
print("✅ Tables créées avec succès !")