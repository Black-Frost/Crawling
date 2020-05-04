from scrapy import Spider, Request
from scrapy.selector import Selector
from crawler.items import CrawlerItem
import json

class CrawlerSpider(Spider):
    f = open('links.json')
    films = json.load(f);
    name = 'crawler'
    allowed_domains = ["ani4u.org"]
    start_urls = [i['Url'] for i in films]
    
    def parse(self, response):
        lists = Selector(response).xpath('//div[@class="data"]')
        for anime in lists:
            item = CrawlerItem()
            item['Name'] = anime.xpath('h1/text()').extract_first()
            genre_list = anime.xpath('p[2]/a/text()').getall()
            item['Genre'] = ', '.join(genre_list[1:])
            item['Year'] = anime.xpath('p[4]/a[2]/text()').extract_first()
            item['Url'] = anime.xpath('a/@href').extract_first()
            yield item