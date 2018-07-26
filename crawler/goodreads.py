from bs4 import BeautifulSoup as bs
from classes import Product
from utils import clean_whitespace, retrieve_data, link_to_fname


BASE_URL = "https://www.goodreads.com"
BOOK_LIST = ("/list/show/10198.Books_With_a_Goodreads_Average_Rating_of_Over_4"
             "_5_and_With_At_Least_100_Ratings")


def retrieve():
    list_link = "{}{}".format(BASE_URL, BOOK_LIST)
    html = retrieve_data("goodreads.top-books.html", list_link)
    soup = bs(html, "html.parser")
    rows = soup.find_all("tr", {"itemtype": "http://schema.org/Book"})

    for row in rows[:100]:
        link = row.find("div", {"data-resource-type": "Book"}).a["href"]
        book_link = "{}{}".format(BASE_URL, link)
        fname = "{}.{}.html".format("goodreads", link_to_fname(link))

        print("Fetching {}...".format(book_link))
        html = retrieve_data(fname, book_link)

        try:
            soup = bs(html, "html.parser")
            title = soup.find("h1", {"id": "bookTitle"}).get_text()
            title = clean_whitespace(title)
            description = soup.select("div#description span")[-1].get_text()
            description = clean_whitespace(description)
            link = soup.find("a", {"id": "buyButton"})["href"]
            genres = soup.select(".left .bookPageGenreLink")
            genres = [clean_whitespace(genre.get_text()) for genre in genres]
            image = soup.find("img", {"id": "coverImage"})["src"]
            if not image.startswith("http"):
                image = "{}{}".format(BASE_URL, image)
            product = Product(title,
                              "{}{}".format(BASE_URL, link),
                              image,
                              "books",
                              genres,
                              description)
            product.dump()
        except Exception as e:
            print("ERROR:", e)
        print("")


if __name__ == "__main__":
    retrieve()
