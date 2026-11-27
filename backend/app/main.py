from contextlib import asynccontextmanager

from app.api.routes import accueil_cards, balise_info, definition
from app.core.config import settings
from app.db.mongo import get_mongo, get_mongo_client
from app.db.mysql import get_db
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pymongo.database import Database
from pymysql.connections import Connection


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Démarrage : on s'assure que le client Mongo est initialisable si besoin
    yield
    # Arrêt : fermeture propre du pool de connexions PyMongo
    mongo_client = get_mongo_client()
    if mongo_client is not None:
        mongo_client.close()


app = FastAPI(
    title="CodeLearn API",
    debug=settings.APP_DEBUG,
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:4200",
        "http://127.0.0.1:4200",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(accueil_cards.router)
app.include_router(balise_info.router)
app.include_router(definition.router)


@app.get("/health", status_code=status.HTTP_200_OK)
def healthcheck(
    db: Connection = Depends(get_db),  # noqa: B008
    mongo_db: Database = Depends(get_mongo),  # noqa: B008
) -> dict[str, str]:
    errors: dict[str, str] = {}

    # 1. Vérification MySQL avec PyMySQL (SQL explicite)
    try:
        with db.cursor() as cursor:
            cursor.execute("SELECT 1 AS ok")
            row = cursor.fetchone()
            if not row or row.get("ok") != 1:
                errors["mysql"] = "unexpected SELECT 1 result"
    except Exception as exc:  # noqa: BLE001
        errors["mysql"] = str(exc)

    # 2. Vérification MongoDB avec PyMongo
    try:
        ping_result = mongo_db.command("ping")
        if ping_result.get("ok") != 1:
            errors["mongodb"] = "unexpected ping result"
    except Exception as exc:  # noqa: BLE001
        errors["mongodb"] = str(exc)

    if errors:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail={"status": "degraded", "errors": errors},
        )

    return {
        "status": "ok",
        "mysql": "connected",
        "mongodb": "connected",
    }
