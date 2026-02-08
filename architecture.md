alert-app-backend/
├── app/
│   ├── __init__.py
│   ├── main.py              # Point d'entrée FastAPI
│   ├── core/                # Configuration, sécurité
│   │   ├── __init__.py
│   │   ├── config.py        # Variables d'environnement
│   │   ├── security.py      # JWT, hash passwords
│   │   └── database.py      # Connexion DB
│   ├── api/                 # Routes API
│   │   ├── __init__.py
│   │   ├── v1/              # Version 1 API
│   │   │   ├── __init__.py
│   │   │   ├── endpoints/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── auth.py
│   │   │   │   ├── alerts.py
│   │   │   │   ├── reports.py
│   │   │   │   └── users.py
│   │   │   └── api.py       # Router principal v1
│   ├── models/              # SQLAlchemy models
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── alert.py
│   │   └── report.py
│   ├── schemas/             # Pydantic schemas
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── alert.py
│   │   └── report.py
│   ├── crud/                # Opérations DB
│   │   ├── __init__.py
│   │   ├── crud_user.py
│   │   ├── crud_alert.py
│   │   └── crud_report.py
│   ├── services/            # Logique métier
│   │   ├── __init__.py
│   │   ├── alert_service.py
│   │   ├── notification_service.py
│   │   └── geolocation.py
│   └── dependencies.py      # Dépendances FastAPI
├── alembic/                 # Migrations
│   └── versions/
├── tests/                   # Tests
├── requirements.txt
├── .env.example
├── docker-compose.yml
└── README.md