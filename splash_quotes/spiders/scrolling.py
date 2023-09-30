import scrapy
from scrapy_splash import SplashRequest
from scrapy.loader import ItemLoader
from splash_quotes.items import SplashQuotesItem


class ScrollingSpider(scrapy.Spider):
    name = 'scrolling'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/scroll']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(
                url=url,
                callback=self.parse,
                args={
                    'wait': 1
                }
            )

    def parse(self, response):
        # /html/body/div/div[2]/div/div/div[1]
        container = response.xpath("//div[@class='quote']")
        for q in container:
            item = ItemLoader(item=SplashQuotesItem(), response=response, selector=q)
            item.add_xpath("quote", ".//span[@class='text']/text()")
            item.add_xpath("author", ".//small[@class='author']/text()")
            yield item.load_item()
