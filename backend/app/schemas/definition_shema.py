from pydantic import BaseModel, ConfigDict


class DefinititionIn(BaseModel):
    def_name: str
    def_description: str
    def_category: str


class DefinititionOut(DefinititionIn):
    model_config = ConfigDict(from_attributes=True)

    def_id: int
