from bs4 import BeautifulSoup as bs
from classes import Product
from utils import retrieve_data, link_to_fname, clean_whitespace

BASE_URL = "https://www.imdb.com"
FILM_LIST = "/chart/top?ref_=nv_mv_250"


def retrieve():
    list_link = "{}{}".format(BASE_URL, FILM_LIST)
    html = retrieve_data("imdb.top-films.html", list_link)
    soup = bs(html, "html.parser")
    film_links = soup.select("tbody.lister-list tr .titleColumn a")
    film_links = [link["href"] for link in film_links]

    for link in film_links[:100]:
        film_link = "{}{}".format(BASE_URL, link)
        fname = "{}.{}.html".format("imdb", link_to_fname(link))

        print("Fetching {}...".format(film_link))
        html = retrieve_data(fname, film_link)
        soup = bs(html, "html.parser")

        try:
            title = soup.select_one(".title_wrapper h1").get_text()
            title = clean_whitespace(title)
            description = soup.select_one(".plot_summary .summary_text")
            description = clean_whitespace(description.get_text())
            image = soup.select_one(".poster a img")["src"]
            if not image.startswith("http"):
                image = "{}{}".format(BASE_URL, image)
            link = soup.select_one(".winner-option.watch-option")["data-href"]
            genres = soup.select(".title_wrapper .subtext a[href^=\"/genre\"]")
            genres = [clean_whitespace(genre.get_text()) for genre in genres]
            product = Product(title,
                              "{}{}".format(BASE_URL, link),
                              image,
                              "films",
                              genres,
                              description)
            product.dump()
        except Exception as e:
            print("ERROR:", e)
        print("")


if __name__ == "__main__":
    retrieve()
