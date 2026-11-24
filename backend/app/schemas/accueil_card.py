from app.schemas.accueil_card_enum import DifficulteEnum, ThemeEnum
from pydantic import BaseModel, ConfigDict


class AccueilCardOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    title: str
    description: str
    lien: str
    theme: ThemeEnum
    niveau: DifficulteEnum


class AccueilCardCreate(BaseModel):
    title: str
    description: str
    lien: str
    theme: ThemeEnum
    niveau: DifficulteEnum
