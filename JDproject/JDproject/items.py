# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JdprojectItem(scrapy.Item):
    # define the fields for your item here like:
    big_name = scrapy.Field()  # �鼮ϵ����
    small_name = scrapy.Field()  # �鼮����
    small_url = scrapy.Field()  # ����url
    book_name = scrapy.Field()  # �鼮����
    book_url = scrapy.Field()  # �鼮url
    price = scrapy.Field()  # �鼮�۸�
    press = scrapy.Field()  # �鼮����
