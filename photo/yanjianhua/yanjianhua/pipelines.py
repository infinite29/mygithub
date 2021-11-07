# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json
import hashlib

from itemadapter import ItemAdapter
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline

# 自定义一个管道，，继承图片管道，，修改他的方法，，实现自定义文件夹的名称，，图片名称
from scrapy.utils.python import to_bytes

class YanjianhuaPipeline(ImagesPipeline):
    num=1
    # 传递item对象里面的数据,,图片名称数据
    def get_media_requests(self, item, info):
        urls = ItemAdapter(item).get(self.images_urls_field, [])
        return [Request(u, meta={'jiujiu': item}) for u in urls]

    # 重写文件名方法,
    def file_path(self, request, response=None, info=None):
        item_ = request.meta.get('jiujiu')  # 对象:存有图片名称的数据,request不可写成response
        title_ = item_['title_']
        # print('图片item对象',item_)
        self.num +=1
        # image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest()
        return f'美女/%s{self.num}.jpg' % (title_)


# class YanjianhuaPipeline:
#     def __init__(self):
#         """只会在爬虫任务开启的时候执行一次"""
#         # 文件的创建,得到一个文件对象
#         self.file_ = open('douban03.json', 'w', encoding='utf-8')
#         print('文件打开了....')
#
#     def process_item(self, item, spider):
#         # 每接收一个item对象，调用一次
#         dict_=dict(item)
#         json_data=json.dumps(dict_,ensure_ascii=False)+',\n'
#         self.file_.write(json_data)
#         print('文件已写入>>>>>>')
#         return item
#
#     def __del__(self):
#         """只会在爬虫任务最后的时候执行一次"""
#         self.file_.close()
#         print('文件关闭了...')
