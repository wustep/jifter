import os
import json
import pymongo
from constants import PRODUCT_PATH


def get_collection(collection):
    mongo_uri = os.environ["MONGO_URI"]
    client = pymongo.MongoClient(mongo_uri)
    mongo_db = client["jifter"]
    col = mongo_db[collection]
    return col


def upload_products():
    product_col = get_collection("product")
    product_col.remove({})
    products = []

    for fname in PRODUCT_PATH.iterdir():
        fpath = PRODUCT_PATH.joinpath(fname)
        with open(fpath) as f:
            product = json.load(f)
        products.append(product)

    product_col.insert_many(products)


def get_primary_tags():
    product_col = get_collection("product")
    primary_tags = product_col.distinct("primary_tag")
    return primary_tags


def get_secondary_tags():
    product_col = get_collection("product")
    secondary_tags = product_col.find({}, {"secondary_tags": 1})
    unique_tags = set()
    for tag in secondary_tags:
        unique_tags.update(tag["secondary_tags"])
    return unique_tags


if __name__ == "__main__":
    upload_products()
