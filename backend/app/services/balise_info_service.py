from app.protocols.balise_info import BaliseInfoRepository
from app.schemas.balise_info import BaliseInfoIn, BaliseInfoOut


class BaliseInfoNotFoundError(Exception):
    """Levée lorsqu'aucune balise ne correspond à l'identifiant demandé."""


class BaliseInfoService:
    def __init__(self, repository: BaliseInfoRepository) -> None:
        self._repository = repository

    def create_balise(self, data: BaliseInfoIn) -> BaliseInfoOut:
        cleaned = BaliseInfoIn(
            balise_type=data.balise_type.strip(),
            balise_nom=data.balise_nom.strip(),
            balise_exemple=data.balise_exemple.strip(),
            balise_explication=data.balise_explication.strip(),
        )
        if not cleaned.balise_type or not cleaned.balise_nom:
            raise ValueError("balise_type et balise_nom ne peuvent pas être vides")
        return self._repository.create(cleaned)

    def get_balise(self, balise_id: int) -> BaliseInfoOut:
        if balise_id <= 0:
            raise ValueError("balise_id doit être un entier strictement positif")
        balise = self._repository.get_by_id(balise_id)
        if balise is None:
            raise BaliseInfoNotFoundError(f"Balise {balise_id} introuvable")
        return balise

    def list_balises(self, limit: int = 100, offset: int = 0) -> list[BaliseInfoOut]:
        if limit < 1 or limit > 500:
            raise ValueError("limit doit être compris entre 1 et 500")
        if offset < 0:
            raise ValueError("offset ne peut pas être négatif")
        return self._repository.list_all(limit=limit, offset=offset)

    def update_balise(self, balise_id: int, data: BaliseInfoIn) -> BaliseInfoOut:
        if balise_id <= 0:
            raise ValueError("balise_id doit être un entier strictement positif")
        cleaned = BaliseInfoIn(
            balise_type=data.balise_type.strip(),
            balise_nom=data.balise_nom.strip(),
            balise_exemple=data.balise_exemple.strip(),
            balise_explication=data.balise_explication.strip(),
        )
        if not cleaned.balise_type or not cleaned.balise_nom:
            raise ValueError("balise_type et balise_nom ne peuvent pas être vides")
        updated = self._repository.update(balise_id, cleaned)
        if updated is None:
            raise BaliseInfoNotFoundError(f"Balise {balise_id} introuvable")
        return updated

    def delete_balise(self, balise_id: int) -> None:
        if balise_id <= 0:
            raise ValueError("balise_id doit être un entier strictement positif")
        deleted = self._repository.delete(balise_id)
        if not deleted:
            raise BaliseInfoNotFoundError(f"Balise {balise_id} introuvable")
