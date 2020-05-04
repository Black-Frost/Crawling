from scrapy import Spider, Request
from scrapy.selector import Selector
from crawler.items import CrawlerItem

class CrawlerSpider(Spider):
    name = 'crawler'
    allowed_domains = ["ani4u.org"]
    start_urls = ['http://ani4u.org/xem-anime/toaru-kagaku-no-railgun-t',
                  'http://ani4u.org/xem-anime/kaguya-sama-wa-kokurasetai-tensai-tachi-no-renai-zunousen-ss2']
    i = 0
    def parse(self, response):
        lists = Selector(response).xpath('//div[@class="data"]')
        for anime in lists:
            item = CrawlerItem()
            item['Name'] = anime.xpath('h1/text()').extract_first()
            genre_list = anime.xpath('p[2]/a[1]/text()').extract_first()
            item['Genre'] = ', '.join(genre_list)
            item['Year'] = anime.xpath('p[4]/a[2]/text()').extract_first()
            item['View'] = anime.xpath('p[7]/text()').extract_first()
            item['Url'] = anime.xpath('a/@href/text()').extract_first()
            #item['Time'] = anime.xpath(
            #    'div[@class="actionuser"]/a[@class="time"]/text()').extract_first()
            yield item
