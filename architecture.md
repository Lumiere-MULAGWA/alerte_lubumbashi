app/
├── main.py
├── core/
│ ├── config.py
│ ├── security.py
│ └── dependencies.py
│
├── database.py
│
├── models/ # SQLAlchemy (DB)
│ ├── base.py
│ ├── user.py
│ └── alert.py
│
├── schemas/ # Pydantic (API I/O)
│ ├── auth.py
│ ├── user.py
│ └── alert.py
│
├── domain/ # Logique métier pure
│ ├── user_domain.py
│ └── alert_domain.py
│
├── repositories/ # Accès base de données
│ ├── user_repository.py
│ └── alert_repository.py
│
├── services/ # Cas d’usage
│ ├── auth_service.py
│ └── alert_service.py
│
├── routers/ # Endpoints FastAPI
│ ├── auth.py
│ └── alert.py
│
└── alembic/