import re
import requests
from constants import CACHE_PATH


def clean_whitespace(text):
    text = text.replace(r"\n", " ")
    text = re.sub(r"\s{2,}", "", text)
    text = text.strip(" ")
    return text


def link_to_fname(link):
    link = re.sub(r"[^\w]", "", link)
    link = link.strip()
    return link


def retrieve_data(fname, url):
    fpath = CACHE_PATH.joinpath(fname)
    if fpath.exists():
        with open(fpath) as f:
            html = f.read()
    else:
        html = requests.get(url).content
        with open(fpath, "w") as f:
            f.write(str(html))
    return html
