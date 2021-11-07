# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JdprojectItem(scrapy.Item):
    # define the fields for your item here like:
    big_name = scrapy.Field()  # 书籍系列名
    small_name = scrapy.Field()  # 书籍类名
    small_url = scrapy.Field()  # 类名url
    book_name = scrapy.Field()  # 书籍名称
    book_url = scrapy.Field()  # 书籍url
    price = scrapy.Field()  # 书籍价格
    press = scrapy.Field()  # 书籍作者
