import scrapy


class OpenflatformSpider(scrapy.Spider):
    name = 'openFlatform'
    allowed_domains = ['open.gwm.cn']
    start_urls = ['https://open.gwm.cn/']

    def parse(self, response):
        pass
