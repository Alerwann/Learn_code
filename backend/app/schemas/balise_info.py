from pydantic import BaseModel, ConfigDict


class BaliseInfoIn(BaseModel):
    balise_type: str
    balise_name: str
    balise_exemple: str
    balise_explication: str


class BaliseInfoOut(BaliseInfoIn):
    model_config = ConfigDict(from_attributes=True)

    balise_id: int
