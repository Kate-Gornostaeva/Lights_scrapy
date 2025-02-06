import scrapy


class LightsnewparseSpider(scrapy.Spider):
    name = "lightsnewparse"
    allowed_domains = ["https://svetilnik-online.ru"]
    start_urls = ["https://svetilnik-online.ru/lustri"]

    def parse(self, response):
        pass
