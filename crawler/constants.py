import os
from pathlib import Path

ROOT_DIR = os.path.dirname(__file__)
CACHE_PATH = Path(ROOT_DIR).joinpath("cache")
PRODUCT_PATH = Path(ROOT_DIR).joinpath("product")

os.makedirs(CACHE_PATH, exist_ok=True)
os.makedirs(PRODUCT_PATH, exist_ok=True)
