import requests
from bs4 import BeautifulSoup

PAGE_URL = "https://monitordolarvenezuela.com/"


def fetch_data():
    try:
        res = requests.get(PAGE_URL)

        soup = BeautifulSoup(res.text, 'html.parser')

        cards = soup.find_all(class_='col-12 col-sm-4 col-md-2 col-lg-2')

        data = []

        for card in cards:
            monitor = {
                "name": card.find(class_='title-prome').text,
                "price": card.find('p').text,
                "last_update": card.find_all('small')[1].text
            }

            data.append(monitor)

        return data

    except:
        return False
