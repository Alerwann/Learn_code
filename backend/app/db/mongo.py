from collections.abc import Generator
from urllib.parse import quote_plus
from pymongo import MongoClient
from pymongo.database import Database

from app.core.config import settings


def build_mongo_uri() -> str:
    """Construit l'URI MongoDB en encodant correctement identifiants et mot de passe."""
    username = quote_plus(settings.MONGO_INITDB_ROOT_USERNAME)
    password = quote_plus(settings.MONGO_INITDB_ROOT_PASSWORD)
    return (
        f"mongodb://{username}:{password}"
        f"@{settings.MONGO_HOST}:{settings.MONGO_PORT}/"
        f"?authSource=admin"
    )


_client: MongoClient | None = None


def get_mongo_client() -> MongoClient:
    """Réutilise un unique MongoClient (pool de connexions géré par PyMongo)."""
    global _client
    if _client is None:
        _client = MongoClient(
            build_mongo_uri(),
            serverSelectionTimeoutMS=5000,
        )
    return _client


def get_mongo() -> Generator[Database, None, None]:
    """Dépendance FastAPI : fournit la base MongoDB cible."""
    client = get_mongo_client()
    db: Database = client[settings.MONGO_INITDB_DATABASE]
    yield db