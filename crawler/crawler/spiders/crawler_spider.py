from scrapy import Spider, Request
from scrapy.selector import Selector
from crawler.items import CrawlerItem
import json

class CrawlerSpider(Spider):
    name = 'crawler'
    allowed_domains = ["ani4u.org"]
    def follow_urls(self):
        urls = ["http://ani4u.org/list-anime"]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.follow)
    def follow(self, respond):
        
        
    
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
