import requests
from bs4 import BeautifulSoup
import html5lib


def make_soup(url):
    response = requests.get(url, {'page': '5'})
    return BeautifulSoup(response.text, 'html5lib')
