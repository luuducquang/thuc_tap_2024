from fastapi import APIRouter
from pymongo.collection import Collection
from config.database import database
from schemas.schemas import ImageProduct
from service.product_service import insert_product    

router = APIRouter()

product_collection: Collection = database['AnhSanPham']

@router.post("/products/")
async def create_product(product_data: ImageProduct):
    product_id = insert_product(product_data)
    return {"message": "Product created successfully", "product_id": product_id}

@router.get("/products")
async def get_products():
    products = []
    for product in product_collection.find():
        product["_id"] = str(product["_id"])
        products.append(product)
    return products


