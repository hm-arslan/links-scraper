import scrapy
from scrapy.crawler import CrawlerProcess
from bs4 import BeautifulSoup
import requests

class LinkSpider(scrapy.Spider):
    name = 'link_spider'

    def __init__(self, url=None, *args, **kwargs):
        super(LinkSpider, self).__init__(*args, **kwargs)
        self.start_urls = [url]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')
        
        soup = BeautifulSoup(response.body, 'html.parser')
        links = soup.find_all('a', href=True)
        for link in links:
            yield {
                'url': link['href']
            }

def fetch_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = soup.find_all('a', href=True)
    return [link['href'] for link in links]

if __name__ == "__main__":
    website_url = input("Enter the website URL: ")
    
    print("Fetching links using BeautifulSoup:")
    links_bs4 = fetch_links(website_url)
    for link in links_bs4:
        print(link)
    
    print("\nFetching links using Scrapy:")
    process = CrawlerProcess()
    process.crawl(LinkSpider, url=website_url)
    process.start()
