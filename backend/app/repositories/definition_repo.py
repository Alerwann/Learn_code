from typing import Any

from app.schemas.definition_shema import definitionIn, definitionOut


class SqlDefinitionRepo:
    def __init__(self, conn: Any) -> None:
        self._conn = conn

    def _to_out(self, row: dict[str, Any]) -> definitionOut:
        return definitionOut.model_validate(row)

    def createDef(self, data: definitionIn) -> definitionOut:
        sql = """
            INSERT INTO all_definition (
               def_name,
               def_description,
               def_category
            )
            VALUES (%s, %s, %s)
        """
        params = (
            data.def_name,
            data.def_description,
            data.def_category,
        )
        with self._conn.cursor() as cur:
            cur.execute(sql, params)
            created_id = cur.lastrowid
        self._conn.commit()
        created = self.get_by_id(created_id)
        if created is None:
            raise RuntimeError("Échec de récupération après insertion dans balise_info")
        return created

    def getAllDef(self) -> list[definitionOut]:
        sql = """
            SELECT def_id, def_name, def_description, def_category
            FROM all_definition
            ORDER BY def_name ASC
            """
        with self._conn.cursor() as cur:
            cur.execute(sql)
            rows = cur.fetchall()
        return [self._to_out(row) for row in rows]

    def getDefById(self, def_id: int) -> definitionOut:
        sql = """
            SELECT def_id, def_name, def_description, def_category
            FROM all_definition 
            WHERE def_id=%s
        """
        with self._conn.cursor() as cur:
            cur.execute(sql, (def_id,))
            row = cur.fetchone()
        return self._to_out(row) if row else None

    def getDefByCategory(self, def_category: str) -> list[definitionOut]:
        sql = """
            SELECT def_id, def_name, def_description, def_category
            FROM all_definition 
            WHERE def_category=%s
        """
        with self._conn.cursor() as cur:
            cur.execute(sql, (def_category))
            rows = cur.fetchall()
        return [self._to_out(row) for row in rows]

    def updateCategory(self, data: definitionOut) -> definitionOut:
        sql = """
            UPDATE all_definition
            SET
                def_name = %s,
                def_description = %s,
                def_category = %s,
            WHERE def_id = %s
        """
        params = (data.def_name, data.def_description, data.def_category, data.def_id)

        with self._conn.cursor() as cur:
            cur.execute(sql, params)
            affected = cur.rowcount
        self._conn.commit()
        if affected == 0:
            return None
        return self.get_by_id(data.def_id)

    def delete(self, def_id: int) -> bool:
        sql = "DELETE FROM all_definition WHERE def_id = %s"
        with self._conn.cursor() as cur:
            cur.execute(sql, (def_id,))
            affected = cur.rowcount
        self._conn.commit()
        return affected > 0
