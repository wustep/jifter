import json
from classes import Product
from constants import PRODUCT_PATH


if __name__ == "__main__":
    for product_fname in PRODUCT_PATH.iterdir():
        fpath = PRODUCT_PATH.joinpath(product_fname)
        print("Cleaning {}".format(fpath))
        with open(fpath) as f:
            data = json.load(f)
        price = data["price"]
        del data["price"]
        product = Product(*list(data.values()), price=price)
        product.dump()
