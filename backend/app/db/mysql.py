from collections.abc import Generator

import pymysql
from app.core.config import settings
from pymysql.connections import Connection
from pymysql.cursors import DictCursor


def get_mysql_connection() -> Connection:
    """Ouvre une connexion PyMySQL vers MySQL à partir de la configuration."""
    return pymysql.connect(
        host=settings.MYSQL_HOST,
        port=settings.MYSQL_PORT,
        user=settings.MYSQL_USER,
        password=settings.MYSQL_PASSWORD,
        database=settings.MYSQL_DATABASE,
        charset="utf8mb4",
        cursorclass=DictCursor,
        autocommit=False,
    )


def get_db() -> Generator[Connection, None, None]:
    """Dépendance FastAPI : fournit une connexion par requête et gère la transaction."""
    conn = get_mysql_connection()
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
