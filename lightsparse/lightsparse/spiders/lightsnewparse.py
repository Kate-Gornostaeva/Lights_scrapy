import scrapy


class LightsnewparseSpider(scrapy.Spider):
    name = "lightsnewparse"
    allowed_domains = ["https://svetilnik-online.ru"]
    start_urls = ["https://svetilnik-online.ru/lustri"]

    custom_settings = {
        'FEED_URI': 'lights_data.csv',
        'FEED_FORMAT': 'csv',
        'FEED_EXPORT_FIELDS': ["Наименование", "Цена", "Ссылка"],
        'FEED_OVERWRITE': True,
    }

    def parse(self, response):
        lights = response.css('li.item')
        for light in lights:
            yield {
                "Наименование": light.css('a').attrib['title'],
                "Цена": light.css('span.pprice::text').get(),
                "Ссылка": light.css('a').attrib['href'],
            }
