# -*- coding: utf-8 -*-
import scrapy
from mySpider.items import BookItem


class BooklistSpider(scrapy.Spider):
    name = 'booklist'
    allowed_domains = ['xhsd.cn']
    start_urls = ['https://www.xhsd.cn/lb.jsp?pid=0401010000']

    def parse(self, response):
        #filename = "booklist.html"
        #open(filename, 'w').write(response.body.decode('utf-8'))
        names = response.xpath('//div[@class="tab_box5"]/table/tr/td/div/a/@title').extract()
        print(len(names))
        photos = response.xpath('//div[@class="tab_box5"]/table/tr/td/div/a/img/@src').extract()
        print(len(photos))
        urls = response.xpath('//div[@class="tab_box5"]/table/tr/td/div/a/@href').extract()
        print(len(urls))
        prices = response.xpath('//td[@class="gray14"]/span[@class="red14"]/text()').extract()
        print(len(prices))
        

        authors = response.xpath('//div[@class="gray12"]')
        auths = []
        for author in authors:
        	auth = author.xpath('text()').extract()
        	if len(auth) == 1:
        		auths.append(auth[0])
        	else :
        		auths.append(' ')
        print(len(auths))

        items = []
        for i in range(0, len(names)-1):
        	item = BookItem()
        	item['name'] = names[i]
        	item['url'] = urls[i]
        	item['author'] = auths[i]
        	item['price'] = prices[i]
        	item['photo'] = photos[i]
        	items.append(item)

        return items



        

