from bs4 import BeautifulSoup
from fiil_form import FillerGoogleForm
import requests
import lxml


class ScraperData:

    def __init__(self, url_for_scrap, parser="html.parser"):
        self.url = url_for_scrap
        self.headers = {
            "USER-AGENT": "Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/93.0.4577.63 Safari/537.36 ",
            "ACCEPT-LANGUAGE": "en-US",
        }
        self.response = requests.get(url=self.url, headers=self.headers).text
        self.soup = BeautifulSoup(self.response, parser)

    def get_list_of_references(self):
        """
        :return: list of references to different houses
        """
        links = []
        refs = self.soup.find_all(name="a", class_="list-card-link")
        for ref in refs:
            link = ref.get("href")
            if link[0] == "/":
                link = "https://www.zillow.com/" + link
            if link not in links:
                links.append(link)
        return links

    def get_list_of_prices(self):
        """
        :return: list of prices for houses
        """
        prices = []
        divs = self.soup.find_all(name="div", class_="list-card-price")
        for div in divs:
            price = div.get_text().split("+")[0]
            price = price.split("/")[0]
            prices.append(price)
        return prices

    def get_addresses(self):
        """
        :return: list of addresses for houses
        """
        addresses = []
        addrs = self.soup.find_all(name="address", class_="list-card-addr")
        for addr in addrs:
            address = addr.get_text()
            addresses.append(address)
        return addresses

    def get_list_of_houses(self):
        """
        test
        """
        houses = self.soup.find_all(name="article", class_="list-card")
        print(len(houses))