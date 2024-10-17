from typing import List, Optional, TypedDict


class ProductsAsDict(TypedDict):
    id: int
    seller: int
    name: str
    description: Optional[str]


async def get_products(limit: int) -> List[ProductsAsDict]:
    pass
