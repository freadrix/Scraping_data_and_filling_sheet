from scraping_data import ScraperData
from fiil_form import FillerGoogleForm

# constants
GOOGLE_FORM_URL = "https://forms.gle/SxZtRm1PpxnfUVHW7"
URL_FOR_SCRAPING_DATA = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D" \
                        "%2C%22mapBounds%22%3A%7B%22west%22%3A-122.6954563431091%2C%22east%22%3A-122.29376872103879" \
                        "%2C%22south%22%3A37.626629422985715%2C%22north%22%3A37.846552958808786%7D%2C%22isMapVisible" \
                        "%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A" \
                        "%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22" \
                        "%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C" \
                        "%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A" \
                        "%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22" \
                        "%3Atrue%2C%22mapZoom%22%3A12%7D "
RESPONSES_URL = "https://docs.google.com/forms/d/13AkAG5A702lVSyHWD6ATUQ3ETQwjHA_WXhR8LpceNs8/edit#responses"


def main():
    # scrap data
    scraper = ScraperData(url_for_scrap=URL_FOR_SCRAPING_DATA, parser="lxml")
    links = scraper.get_list_of_references()
    prices = scraper.get_list_of_prices()
    addresses = scraper.get_addresses()
    # scrap.get_list_of_houses()  # test

    # fill google form
    for n in range(len(links)):
        filler = FillerGoogleForm(GOOGLE_FORM_URL)
        filler.fill_form(answer_for_first_question=addresses[n], answer_for_second_question=prices[n],
                         answer_for_third_question=links[n])

    # open google sheet
    # opener = FillerGoogleForm(RESPONSES_URL)
    # opener.open_sheet()


if __name__ == "__main__":
    main()
