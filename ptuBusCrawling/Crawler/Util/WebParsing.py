from bs4 import BeautifulSoup
import requests

class WebParsing:
    def __init__(self, url):
        self.url = url

    def openURL(self):
        req = requests.get(self.url)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        return soup

    def parsingSelector(self, selector):
        soup = self.openURL()
        selec = soup.select(selector)
        return selec