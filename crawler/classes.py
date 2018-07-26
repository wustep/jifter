import json
from utils import link_to_fname, clean_whitespace
from constants import PRODUCT_PATH


class Product(object):
    def __init__(self,
                 name,
                 link,
                 image,
                 primary_tag,
                 secondary_tags,
                 description):
        super(Product, self).__init__()
        secondary_tags = {clean_whitespace(tag) for tag in secondary_tags}
        self.name = name
        self.link = link
        self.image = image
        self.primary_tag = primary_tag
        self.secondary_tags = list(secondary_tags)
        self.description = description

    def dump(self):
        fname = link_to_fname(self.name)
        fname = "{}.{}".format(self.primary_tag, fname)
        fname = "{}.json".format(fname)
        fname = fname.lower()
        fpath = PRODUCT_PATH.joinpath(fname)
        with open(fpath, "w") as f:
            json.dump(vars(self), f)
