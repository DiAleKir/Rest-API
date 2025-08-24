from typing import Optional

from pydantic import BaseModel, field_validator, Field


class DataModel(BaseModel):
    year: int = Field(gt=0)
    price: int | float = Field(gt=0)
    cpu: str = Field(alias="CPU model")
    hd_size: str = Field(alias="Hard disk size")

class ObjectModel(BaseModel):
    id: str
    name: str
    createdAt: Optional[str] = None
    data: DataModel

    @field_validator("id", "name", "data")
    def field_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

class CreateObjectModel(ObjectModel):
    createdAt: str

    @field_validator("createdAt")
    def field_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

class UpdateObjectModel(ObjectModel):
    updatedAt: str

    @field_validator("updatedAt")
    def field_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value