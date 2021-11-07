# -*- coding: utf-8 -*-
import scrapy
from ..items import JdprojectItem
from scrapy_redis.spiders import RedisSpider


# start_url = https://book.jd.com/booksort.html
class JdSpider(RedisSpider):
    name = 'JD'  # 爬虫名字
    redis_key = 'jd'  # 起始url的key名字，用lpush key url存入数据
    allowed_domains = ['jd.com']
    # 增加__init__()方法，动态获取allowed_domains()
    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = list(filter(None, domain.split(',')))
        super(JdSpider, self).__init__(*args, **kwargs)

    # def start_requests(self):
    #     start_urls = ['https://book.jd.com/booksort.html']
    #     for ur in start_urls:
    #         yield scrapy.Request(url=ur, callback=self.parse)

    # 解析出类标签的url
    def parse(self, response):
        dt = response.xpath('//*[@id="booksort"]/div[2]/dl/dt')
        for big in dt:
            # 查询同级下的下一个标签
            s_title = big.xpath('./following-sibling::dd[1]/em')
            for s in s_title:
                print(s)
                temp = {}
                temp["big_name"] = big.xpath('./a/text()').extract_first()
                temp["small_name"] = s.xpath('./a/text()').extract_first()
                temp["small_url"] = "https:" + s.xpath('./a/@href').extract_first()
                yield scrapy.Request(url=temp["small_url"],
                                     callback=self.data_spider,
                                     meta={"meta": temp}
                                     )

    # 提取各类里的书籍名称
    def data_spider(self, response):
        temp = response.meta["meta"]
        book_list = response.xpath('//*[@id="J_goodsList"]/ul/li')
        for book in book_list:
            print(book)
            item = JdprojectItem()
            item["big_name"] = temp["big_name"]
            # item["big_url"] = temp["big_url"]
            item["small_name"] = temp["small_name"]
            item["small_url"] = temp["small_url"]

            item["book_name"] = book.xpath('./div/div[3]/a/em/text()').extract_first()
            item["book_url"] = "https:" + book.xpath('./div/div[1]/a/@href').extract_first()
            if "v=404" in item["book_url"]:
                # print(item["book_name"])
                # print(item["book_url"])
                continue
            item["price"] = book.xpath('./div/div[2]/strong/i/text()').extract_first()
            item["press"] = book.xpath('./div/div[6]/a/text()').extract_first()
            yield item
