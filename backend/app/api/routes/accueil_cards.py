from app.db.mongo import get_mongo
from app.repositories.accueil_card_repo import (
    AccueilCardCreate,
    AccueilCardOut,
    create_accueil_card,
    get_accueil_card_by_id,
    list_accueil_cards,
)
from fastapi import APIRouter, Depends, HTTPException, status
from pymongo.database import Database

router = APIRouter(prefix="/accueil-cards", tags=["Accueil Cards"])


@router.get("", response_model=list[AccueilCardOut])
def get_cards(mongo_db: Database = Depends(get_mongo)) -> list[AccueilCardOut]:  # noqa: B008
    return list_accueil_cards(mongo_db)


@router.get("/{card_id}", response_model=AccueilCardOut)
def get_card(card_id: str, mongo_db: Database = Depends(get_mongo)) -> AccueilCardOut:  # noqa: B008
    card = get_accueil_card_by_id(mongo_db, card_id)
    if not card:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Carte introuvable"
        )
    return card


@router.post("", response_model=AccueilCardOut, status_code=status.HTTP_201_CREATED)
def post_card(
    payload: AccueilCardCreate,
    mongo_db: Database = Depends(get_mongo),  # noqa: B008
) -> AccueilCardOut:
    return create_accueil_card(mongo_db, payload)
