import os
import json
import pymongo
from constants import PRODUCT_PATH


def upload_products():
    mongo_uri = os.environ["MONGO_URI"]
    client = pymongo.MongoClient(mongo_uri)
    mongo_db = client["jifter"]
    product_col = mongo_db["product"]
    product_col.remove({})
    products = []

    for fname in PRODUCT_PATH.iterdir():
        fpath = PRODUCT_PATH.joinpath(fname)
        with open(fpath) as f:
            product = json.load(f)
        products.append(product)

    product_col.insert_many(products)


if __name__ == "__main__":
    upload_products()
