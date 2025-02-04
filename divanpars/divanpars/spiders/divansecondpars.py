import csv

import scrapy
from scrapy.cmdline import execute


class DivansecondparsSpider(scrapy.Spider):
    name = "divansecondpars"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/ekaterinburg/category/dekor"]

    def parse(self, response):
        parsed_data = []
        decors = response.css('div.WdR1o')
        for decor in decors:
            name = decor.css('span[itemprop="name"]::text').get()
            price = decor.css('span.ui-LD-ZU.KIkOH::text').get()
            link = self.start_urls[0] + decor.css('a').attrib['href']

            parsed_data.append([name, price, link])
            print(parsed_data[-1])

        with open('div_decor.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Название', 'Цена', 'Ссылка'])
            writer.writerows(parsed_data)
        return


if __name__ == '__main__':
    execute(['scrapy', 'crawl', 'divansecondpars'])