import requests
from bs4 import BeautifulSoup

class WebScraping:

        content = None
        header = {
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
                "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
        }

        def __init__(self, url:str):
                response = requests.get(url=url, headers=self.header)
                response.raise_for_status()
                self.content = response.text
                self.parseContent = BeautifulSoup(self.content, 'html.parser')

        def getContent(self):
                return self.content

        def getListOfLink(self):
                links = [( item.select_one("a")['href'] , item.select_one("div:nth-child(1)").text) for item in
                         self.parseContent.select(selector="div[data-testid^='listing-ad-item-'] > div:nth-child(2)")]
                address = [item.text for item in
                         self.parseContent.select(selector="div[data-testid^='listing-ad-item-'] > div:nth-child(3) > div:nth-child(1) > span:nth-child(2)")]

                new_links = []
                for i in range(len(links)):
                        new_links.append( (*links[i], address[i]))

                return new_links
