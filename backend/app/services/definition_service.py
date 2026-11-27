from app.protocols.def_protocol import DefRepository
from app.schemas.definition_shema import definitionIn, definitionOut


class DefNotFoundError(Exception):
    """Levée lorsqu'aucune balise ne correspond à l'identifiant demandé."""


class DefService:
    def __init__(self, repository: DefRepository) -> None:
        self._repository = repository

    def create_def(self, data: definitionIn) -> definitionOut:
        cleaned = definitionIn(
            def_name=data.def_name.strip(),
            def_description=data.def_description.strip(),
            def_category=data.def_category.strip(),
        )
        if (
            not cleaned.def_name
            or not cleaned.def_description
            or not cleaned.def_category
        ):
            raise ValueError(" Aucun champs ne peut être vides")
        return self._repository.create(cleaned)

    def getAllDef(self) -> list[definitionOut]:
        return self._repository.getAllDef()

    def getDefByCategory(self, def_category: str) -> list[definitionOut]:
        definition = self._repository.getDefByCategory(def_category)
        if not definition:
            raise DefNotFoundError("Aucune définition dans cette catégorie")
        return definition

    def getDefById(self, def_id: int) -> definitionOut:
        if def_id < 0:
            raise ValueError("def_id doit être un entier strictement positif")
        definition = self._repository.getDefById(def_id)
        if definition is None:
            raise ValueError(f"Definition {def_id} n'existe pas")
        return definition

    def updateDef(self, data: definitionOut) -> definitionOut:
        if not data:
            raise ValueError("Aucune données reçue")
        cleaned = definitionIn(
            def_id=data.def_id,
            def_name=data.def_name.strip(),
            def_description=data.def_description.strip(),
            def_category=data.def_category.strip(),
        )

        if (
            cleaned.def_id < 0
            or not cleaned.def_name
            or not cleaned.def_description
            or not cleaned.def_category
        ):
            raise ValueError("Données incomplètes")
        update = self._repository.updateCategory(cleaned)
        if update is None:
            raise ValueError(f"Definition {cleaned.def_id} n'existe pas")
        return update

    def deleteCategory(self, def_id: int) -> None:
        if def_id < 0:
            raise ValueError("L'id doit être positif")
        deleted = self._repository.deleteCategory(def_id)
        if not deleted:
            raise ValueError(f"Definition {def_id} n'existe pas")
