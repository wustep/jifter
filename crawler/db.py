import os
import json
import pymongo
from constants import PRODUCT_PATH, QUESTION_PATH


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


def upload_questions():
    question_col = get_collection("question")
    question_col.remove({})
    questions = []

    for fname in QUESTION_PATH.iterdir():
        fpath = QUESTION_PATH.joinpath(fname)
        with open(fpath) as f:
            question = json.load(f)
        questions.append(question)

    question_col.insert_many(questions)


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


def get_products(p_tags, s_tags={}, min_price=0, max_price=9999999):
    product_col = get_collection("product")
    p_tags = [tag for tag, weight in p_tags.items() if weight >= 0.45]
    s_tags = [tag for tag, weight in s_tags.items() if weight >= 0.65]
    products = product_col.find({"price": {"$gte": min_price,
                                           "$lte": max_price},
                                 "$or": [
                                    {"primary_tag": {"$in": p_tags}},
                                    {"secondary_tags": {"$in": s_tags}}
                                 ]}).limit(10)
    return list(products)


def get_question_for_tags(p_tags, s_tags={}):
    p_tags = [tag for tag, weight in p_tags.items() if weight >= 0.45]
    s_tags = [tag for tag, weight in s_tags.items() if weight >= 0.65]
    question_col = get_collection("question")
    questions = list(question_col.find({"$or": [
       {"primary_tag": {"$in": p_tags}},
       {"secondary_tags": {"$in": s_tags}}
    ]}).limit(10))
    return questions[0] if questions else None


if __name__ == "__main__":
    upload_products()
    upload_questions()
