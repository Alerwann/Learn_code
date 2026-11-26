from typing import Any

from app.schemas.balise_info import BaliseInfoIn, BaliseInfoOut


class SqlBaliseInfoRepository:
    def __init__(self, conn: Any) -> None:
        self._conn = conn

    def _to_out(self, row: dict[str, Any]) -> BaliseInfoOut:
        return BaliseInfoOut.model_validate(row)

    def create(self, data: BaliseInfoIn) -> BaliseInfoOut:
        sql = """
            INSERT INTO balise_info (
                balise_type,
                balise_nom,
                balise_exemple,
                balise_explication
            )
            VALUES (%s, %s, %s, %s)
        """
        params = (
            data.balise_type,
            data.balise_nom,
            data.balise_exemple,
            data.balise_explication,
        )
        with self._conn.cursor() as cur:
            cur.execute(sql, params)
            created_id = cur.lastrowid
        self._conn.commit()
        created = self.get_by_id(created_id)
        if created is None:
            raise RuntimeError("Échec de récupération après insertion dans balise_info")
        return created

    def get_by_id(self, balise_id: int) -> BaliseInfoOut | None:
        sql = """
            SELECT
                balise_id,
                balise_type,
                balise_nom,
                balise_exemple,
                balise_explication
            FROM balise_info
            WHERE balise_id = %s
        """
        with self._conn.cursor() as cur:
            cur.execute(sql, (balise_id,))
            row = cur.fetchone()
        return self._to_out(row) if row else None

    def list_all(self, limit: int = 100, offset: int = 0) -> list[BaliseInfoOut]:
        sql = """
            SELECT
                balise_id,
                balise_type,
                balise_nom,
                balise_exemple,
                balise_explication
            FROM balise_info
            ORDER BY balise_id ASC
            LIMIT %s OFFSET %s
        """
        with self._conn.cursor() as cur:
            cur.execute(sql, (limit, offset))
            rows = cur.fetchall()
        return [self._to_out(row) for row in rows]

    def update(self, balise_id: int, data: BaliseInfoIn) -> BaliseInfoOut | None:
        sql = """
            UPDATE balise_info
            SET
                balise_type = %s,
                balise_nom = %s,
                balise_exemple = %s,
                balise_explication = %s
            WHERE balise_id = %s
        """
        params = (
            data.balise_type,
            data.balise_nom,
            data.balise_exemple,
            data.balise_explication,
            balise_id,
        )
        with self._conn.cursor() as cur:
            cur.execute(sql, params)
            affected = cur.rowcount
        self._conn.commit()
        if affected == 0:
            return None
        return self.get_by_id(balise_id)

    def delete(self, balise_id: int) -> bool:
        sql = "DELETE FROM balise_info WHERE balise_id = %s"
        with self._conn.cursor() as cur:
            cur.execute(sql, (balise_id,))
            affected = cur.rowcount
        self._conn.commit()
        return affected > 0
