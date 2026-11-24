from app.schemas.accueil_card import AccueilCardCreate, AccueilCardOut
from bson import ObjectId
from bson.errors import InvalidId
from pymongo.database import Database


def _serialize_card(doc: dict) -> AccueilCardOut:
    return AccueilCardOut(
        id=str(doc["_id"]),
        title=doc["title"],
        lien=doc["lien"],
        description=doc["description"],
        theme=doc["theme"],
        niveau=doc["niveau"],
    )


def list_accueil_cards(db: Database) -> list[AccueilCardOut]:
    cursor = db["accueil_cards"].find()
    return [_serialize_card(doc) for doc in cursor]


def create_accueil_card(db: Database, payload: AccueilCardCreate) -> AccueilCardOut:
    result = db["accueil_cards"].insert_one(payload.model_dump(mode="json"))
    created = db["accueil_cards"].find_one({"_id": result.inserted_id})
    return _serialize_card(created)


def get_accueil_card_by_id(db: Database, card_id: str) -> AccueilCardOut | None:
    try:
        oid = ObjectId(card_id)
    except InvalidId:
        return None
    doc = db["accueil_cards"].find_one({"_id": oid})
    return _serialize_card(doc) if doc else None
