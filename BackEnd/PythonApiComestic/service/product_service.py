from pymongo.collection import Collection
from schemas.schemas import ImageProduct
from config.database import database

product_collection: Collection = database['ImageProduct']

def insert_product(product_data: ImageProduct) -> str:
    product_dict = product_data.dict()
    result = product_collection.insert_one(product_dict)
    return str(result.inserted_id)
