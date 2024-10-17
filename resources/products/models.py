from typing import Optional
from pydantic import BaseModel


class ProductIN(BaseModel):
    # FK users
    seller: int
    # Product title
    title: str
    # Product description
    description: Optional[str]
    image: str


class ProductOut(ProductIN):
    # Unique product identifier (PK)
    id: int
