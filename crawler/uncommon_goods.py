from bs4 import BeautifulSoup as bs
from classes import Product
from utils import retrieve_data, link_to_fname, clean_whitespace, get_tags

BASE_URL = 'https://www.uncommongoods.com'
LIST_URL = '/fun/by-interest'
INTERESTS = ['sports',
             'geek',
             'business',
             'music',
             'animal',
             'fitness']
QUERY_STR = "?view=all&custom_country=US&n=100&p=1"


def retrieve_products_for_interest(interest):
    list_url = "{}{}/{}-gifts{}".format(BASE_URL,
                                        LIST_URL,
                                        interest,
                                        QUERY_STR)
    html = retrieve_data("uncommon-goods.{}.html".format(interest), list_url)
    soup = bs(html, "html.parser")
    prod_links = [link["href"] for link in soup.select("article.product a")]

    for link in prod_links[:100]:
        prod_link = "{}{}".format(BASE_URL, link)
        fname = "{}.{}.html".format("uncommon-goods", link_to_fname(link))

        print("Fetching {}...".format(prod_link))
        html = retrieve_data(fname, prod_link)
        soup = bs(html, "html.parser")

        try:
            title = soup.find("h1", {"itemprop": "name"}).get_text()
            title = clean_whitespace(title)
            description = soup.select_one(".theStoryCopy p").get_text()
            description = clean_whitespace(description)
            image = soup.select_one("a#mainImage img")["src"]
            if not image.startswith("http"):
                image = "{}{}".format(BASE_URL, image)
            price = soup.find("span", {"itemprop": "price"}).get_text()
            price = float(clean_whitespace(price))
            tags = get_tags(description)
            product = Product(title,
                              "{}{}".format(BASE_URL, link),
                              image,
                              interest,
                              tags,
                              description,
                              price=price)
            product.dump()
        except Exception as e:
            print("ERROR:", e)
        print("")


def retrieve():
    for interest in INTERESTS:
        retrieve_products_for_interest(interest)


if __name__ == "__main__":
    retrieve()
