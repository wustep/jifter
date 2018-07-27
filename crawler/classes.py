import json
from uuid import uuid4
from utils import link_to_fname, clean_whitespace
from constants import PRODUCT_PATH, QUESTION_PATH


class Product(object):
    def __init__(self,
                 name,
                 link,
                 image,
                 primary_tag,
                 secondary_tags,
                 description,
                 price=None):
        super(Product, self).__init__()
        unique_tags = set()
        for tag in secondary_tags:
            tag = clean_whitespace(tag).lower()
            unique_tags.add(tag)
        self.name = name
        self.link = link
        self.image = image
        self.primary_tag = primary_tag
        self.secondary_tags = list(unique_tags)
        self.description = description
        self.price = price

    def dump(self):
        fname = link_to_fname(self.name)
        fname = "{}.{}".format(self.primary_tag, fname)
        fname = "{}.json".format(fname)
        fname = fname.lower()
        fpath = PRODUCT_PATH.joinpath(fname)
        with open(fpath, "w") as f:
            json.dump(vars(self), f)


class Question(object):
    def __init__(self, text, primary_tag, secondary_tags):
        super(Question).__init__()
        self.id = uuid4()
        self.text = text
        self.primary_tag = primary_tag
        self.secondary_tags = secondary_tags

    def dump(self):
        fname = "question.{}.json".format(self.id)
        fpath = QUESTION_PATH.joinpath(fname)
        with open(fpath, "w") as f:
            data = dict(vars(self))
            del data["id"]
            json.dump(data, f)
