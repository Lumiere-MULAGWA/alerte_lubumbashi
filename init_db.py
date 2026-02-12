# init_db_local.py
import os
import sys

# Définir DATABASE_URL avant tout import
os.environ["DATABASE_URL"] = "postgresql://alert_user:strong_password@localhost:5432/alert_db"

# Ajouter le chemin du projet
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base

# Connexion directe à la base
DATABASE_URL = "postgresql://alert_user:strong_password@localhost:5432/alert_db"

try:
    # Tester la connexion
    engine = create_engine(DATABASE_URL)
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    print("✅ Connexion à PostgreSQL réussie!")
    
    # Importer les modèles
    from app.models.users import User
    from app.models.alert import Alert
    from app.models.report import Report
    
    # Créer les tables
    Base = declarative_base()
    Base.metadata.create_all(bind=engine)
    print("✅ Tables créées avec succès!")
    
    # Vérifier les tables créées
    with engine.connect() as conn:
        result = conn.execute(text("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public'
        """))
        tables = [row[0] for row in result]
        print(f"📊 Tables dans la base: {', '.join(tables)}")
        
except Exception as e:
    print(f"❌ Erreur: {e}")
    print("\nSolutions possibles:")
    print("1. Vérifiez que PostgreSQL est en cours d'exécution:")
    print("   sudo systemctl status postgresql")
    print("2. Vérifiez les identifiants dans .env")
    print("3. Testez la connexion manuellement:")
    print("   psql -h localhost -U alert_user -d alert_db -W")