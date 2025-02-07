import scrapy


class LightsnewparseSpider(scrapy.Spider):
    name = "lightsnewparse"
    allowed_domains = ["https://svetilnik-online.ru"]
    start_urls = ["https://svetilnik-online.ru/lustri"]

    def parse(self, response):
        lights = response.css('li.item')
        for light in lights:
            yield {
                'name': light.css('a').attrib['title'],
                'price': light.css('span.pprice::text').get(),
                'link': light.css('a').attrib['href'],
            }
