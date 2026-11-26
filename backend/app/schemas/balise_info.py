from pydantic import BaseModel, ConfigDict


class BaliseInfoOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    balise_id: int
    base_type: str
    base_nom: str
    base_exemple: str
    base_description: str


class BaliseInfoIn(BaseModel):
    base_type: str
    base_nom: str
    base_exemple: str
    base_description: str
