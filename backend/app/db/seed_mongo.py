from app.db.mongo import get_mongo
from app.schemas.accueil_card import AccueilCardCreate
from app.schemas.accueil_card_enum import DifficulteEnum, ThemeEnum
from pymongo.database import Database

DEFAULT_ACCUEIL_CARDS: list[AccueilCardCreate] = [
    AccueilCardCreate(
        title="HTML",
        description="Les bases pour comprendre le fonctionnement d'HTML",
        theme=ThemeEnum.FRONTEND,
        niveau=DifficulteEnum.FACILE,
    ),
    AccueilCardCreate(
        title="CSS",
        description="Apprendre mise en forme de votre page",
        theme=ThemeEnum.FRONTEND,
        niveau=DifficulteEnum.FACILE,
    ),
    AccueilCardCreate(
        title="Git/Github",
        description="Créer le versonning de ton projet",
        theme=ThemeEnum.SETUP,
        niveau=DifficulteEnum.MOYEN,
    ),
    AccueilCardCreate(
        title="Environnements avec Docker",
        description="Lancer des services isolés et orchestrer avec Compose.",
        theme=ThemeEnum.SETUP,
        niveau=DifficulteEnum.DIFFICILE,
    ),
    AccueilCardCreate(
        title="Navigation efficace en CLI",
        description="Commandes shell, droits fichiers et scripts courants.",
        theme=ThemeEnum.CLI,
        niveau=DifficulteEnum.FACILE,
    ),
]


def seed_accueil_cards(db: Database) -> None:
    collection = db["accueil_cards"]
    collection.create_index("title", unique=True)

    for card in DEFAULT_ACCUEIL_CARDS:
        data = card.model_dump(mode="json")
        collection.update_one(
            {"title": data["title"]},
            {"$setOnInsert": data},
            upsert=True,
        )


if __name__ == "__main__":
    mongo_db = next(get_mongo())
    seed_accueil_cards(mongo_db)
