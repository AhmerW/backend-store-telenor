from typing import Final, List
from fastapi import APIRouter

from data.services import product_service
from core.responses import Success, Response
from resources.products.models import ProductIN, ProductOut

router: Final[APIRouter] = APIRouter(
    prefix="/products",
)


class ProductsResponse(Response):
    products: List[ProductOut]


@router.get(
    "/",
    response_class=ProductsResponse,
)
async def get_products(
    limit: int,
    query: str
) -> Success:
    products: List[ProductOut] = await product_service.get_products(
        limit,
        query
    )

    return Success(
        dict(
            products=products,
        ),
    )

@router.post("/")
async def post_products(product: ProductIN):
    await product_service.add_product(product)