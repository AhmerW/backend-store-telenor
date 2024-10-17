from typing import List
from resources.products.models import ProductOut, ProductIN
import random

def validate_product_name():
    ...

class ProductsManager:
    def __init__(self):
        self.products = [
            ProductOut(
                seller=0,
                title="Tittel!",
                description="Default produkst!",
                image="",
                id=1,
            )
        ]


manager = ProductsManager()

async def get_products(limit: int, query="") -> List[ProductOut]:
    products = manager.products[0:limit]
    if not query:
        return products

    return  [product for product in manager.products if query.lower() in product.title.lower() or query in product.description.lower()]

async def add_product(product: ProductIN):
    product_out = ProductOut(id=random.randint(1, 1000), **product.model_dump())
    manager.products.append(product_out)


