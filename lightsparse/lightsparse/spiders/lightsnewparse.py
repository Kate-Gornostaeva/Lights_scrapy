import scrapy
import csv


class LightsnewparseSpider(scrapy.Spider):
    name = "lightsnewparse"
    allowed_domains = ["svetilnik-online.ru"]
    start_urls = ["https://svetilnik-online.ru/lustri"]

    def parse(self, response):
        lights = response.css('li.item')
        data = []  # Создаем список для хранения данных

        for light in lights:
            name = light.css('a').attrib['title']
            price = light.css('span.pprice::text').get()
            link = light.css('a').attrib['href']

            data.append({'Наименование': name, 'Цена': price, 'Ссылка': link})  # Добавляем данные в список

        # Записываем данные в CSV файл
        filename = "lights_data.csv"
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Наименование', 'Цена', 'Ссылка']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()  # Записываем заголовки столбцов
            writer.writerows(data)  # Записываем данные

        
