from pydantic import BaseModel, ConfigDict


class definitionIn(BaseModel):
    def_name: str
    def_description: str
    def_category: str


class definitionOut(definitionIn):
    model_config = ConfigDict(from_attributes=True)

    def_id: int
