# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# 图片管道
from scrapy.pipelines.images import ImagesPipeline

class YanjianhuaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 电影名称的数据:之后电影名称的数据就保存在title_字段当中
    title_ = scrapy.Field()

    # 评分数据
    score_ = scrapy.Field()

    # 简洁数据
    text_ = scrapy.Field()

    # 图片url的字段名 > 固定名称,,不能修改
    image_urls = scrapy.Field()
    pass


