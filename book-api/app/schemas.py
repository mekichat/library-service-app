# Create Pydantic Schema
from pydantic import BaseModel
from pydantic import ConfigDict


class BookBase(BaseModel):
    title: str
    author: str
    price: float


class BookCreate(BookBase):
    pass


class BookUpdate(BookBase):
    pass


class BookResponse(BookBase):
    id: int

    model_config = ConfigDict(
        from_attributes=True
    )