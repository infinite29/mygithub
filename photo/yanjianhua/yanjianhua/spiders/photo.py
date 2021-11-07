import re

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import YanjianhuaItem

#mzitu.com
# class PhotoSpider(CrawlSpider):
#     name = 'photo'
#     allowed_domains = ['mzitu.com']
#     start_urls = ['https://www.mzitu.com/xinggan/']
#
#     rules = (
#         Rule(LinkExtractor(restrict_xpaths=('//ul[@id="pins"]/li/a')), #callback='parse_item'
#               follow=False),
#         Rule(LinkExtractor(restrict_xpaths=("/html/body/div[2]/div[1]/div[3]/div/a[5]")), follow=True),  # follow意味着一直按照这个规则提取url,,构建请求对象
#         Rule(LinkExtractor(restrict_xpaths=("//div[@class='TypeList']/ul/li/a")),callback='parse_item', follow=True),
#
#     )
#
#     def parse_item(self, response):
#         """进入了详情页的resposne的解析"""
#         item_ = YanjianhuaItem()
#
#         # 获取到图片的url
#         url_ = response.xpath('//div[@class="main-image"]//p/a/img/@src').getall()
#         # print('图片的url:', url_)
#
#         # 获取图片的文件名
#         title_ = response.xpath('/html/body/div[2]/div[1]/h2').getall()
#         # print('图片的文件名:',title_)
#         item_['image_urls'] = url_ # 进行数据装车item对象,图片url如果想使用图片管道,必须是一个列表
#         item_['title_'] = title_
#
#         return item_  # 图片管道,除了图片的url,,还有图片文件名
#
#     def parse_item(self, response):  # 用来做数据的提取，形参response接收的就是响应对象的response
#
#         # 详情页的url
#         url_list = response.xpath("//h3[@class='title']/a/@href").getall()
#
#         # 保存需要依赖item对象，构建对象就需要依赖类的定义
#         for i in range(len(url_list)):
#             # 拼接url
#             url_ = "https://www.sixstaredu.com" + url_list[i]
#             # 构建一个运输车载体,类似一个字典
#             item_ = YanjianhuaItem()
#             # 老师名称保存在item对象的teacher_部分
#             item_['teacher_'] = teacher_list[i]
#             info_ = info_list[i].replace(" ", "")
#             info_ = info_.replace("\n", "")
#             # 老师介绍保存在item对象的info_部分
#             item_['info_'] = info_
#             # 发送请求
#             yield scrapy.Request(url_, callback=self.parse_url, meta={"Cara": item_})
#
#         # 利用response响应实现（无脑的抓取）
#         url_next = \
#         re.findall(' <li><a  href="(.*?)"><i class="cd-icon cd-icon-arrow-right"></i></a></li>', response.text)[0]
#         print('下一页的url', url_next)
#         yield response.follow(url_next, callback=self.parse)  # 翻页： follow会自动补全残缺的url


# ku66.net
class PhotoSpider(CrawlSpider):
    name = 'photo'
    allowed_domains = ['ku66.net']
    start_urls = ['https://www.ku66.net/r/2/index.html']

    rules = (
        # Rule(LinkExtractor(restrict_xpaths=('//div[@class="w850 l oh"]/a')), # callback='parse_item',
        #      follow=False),
        Rule(LinkExtractor(restrict_xpaths=('//div[@class="TypeList"]/ul/li/a')), callback='parse_item'),
        Rule(LinkExtractor(restrict_xpaths=("//a[text()='下一页']")), follow=True),
        # Rule(LinkExtractor(restrict_xpaths=('//div[@class="TypeList"]/ul/li/a')), callback='parse_item',follow=True),
        # follow意味着一直按照这个规则提取url,,构建请求对象
        # Rule(LinkExtractor(restrict_xpaths=("//div[@class='TypeList']/ul/li/a")), callback='parse_item',
        #      follow=True),

    )

    def parse_item(self, response):
        """进入了详情页的resposne的解析"""
        item_ = YanjianhuaItem()
        # 获取到图片的url
        url_ = response.xpath('//div[@class="content"]/img/@src').getall()
        # print('图片的url:', url_)

        # 获取图片的文件名
        title_=response.xpath('//strong/text()').getall()[0]
        item_['title_'] = title_
        url_next = response.xpath("//a[text()='下一页']/@href").getall()
        # print('下一页的url', url_next)
        item_['image_urls'] = url_  # 进行数据装车item对象,图片url如果想使用图片管道,必须是一个列表
        # item_['image_urls'] = url_next   # 进行数据装车item对象,图片url如果想使用图片管道,必须是一个列表
        return item_  # 图片管道,除了图片的url,,还有图片文件名
        # url_next = response.xpath("//a[text()='下一页']/@href").getall()
        # print('下一页的url', url_next)
        # yield response.follow(url_next, callback=self.parse_item)  # 翻页： follow会自动补全残缺的url











    # rules = (
    #     Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    # )
    #
    # def parse_item(self, response):
    #     item = {}
    #     #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
    #     #item['name'] = response.xpath('//div[@id="name"]').get()
    #     #item['description'] = response.xpath('//div[@id="description"]').get()
    #     return item
