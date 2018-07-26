import re
import requests
from constants import CACHE_PATH, TAG_EXCLUSIONS


def get_tags(text):
    word_map = {}
    for word in text.split(" "):
        word = word.lower().strip(" .!?,\"'()[]\{\}:;")
        count = word_map.get(word, 0)
        count += 1
        word_map[word] = count
    tags = list(word_map.items())
    tags = sorted(tags, key=lambda x: x[1], reverse=True)
    tags = [tag for tag, _ in tags if tag not in TAG_EXCLUSIONS][:4]
    return tags


def clean_whitespace(text):
    text = text.replace(r"\n", " ")
    text = text.replace("\\", "")
    text = re.sub(r"\s{2,}", " ", text)
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
