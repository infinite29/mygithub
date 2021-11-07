# -*- coding : utf-8 -*-
# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from selenium import webdriver
import time
from scrapy.http import HtmlResponse
from selenium.webdriver import ChromeOptions
from selenium.webdriver import Chrome

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


# 使用selenium进行页面渲染
class SeleniumMiddleware(object):
    def process_request(self, request, spider):
        url = request.url  # 提取出url
        # 当页面是图书分类的页面时，使用下面方式进行页面渲染
        if "booksort" in url:
            # ===设置不加载页面
            options_ = ChromeOptions()
            # 添加参数,进行隐藏
            options_.add_experimental_option('excludeSwitches', ["enable-automation"])  # 不需要死记硬背
            options_.add_argument('--headless')  # 设置无界面
            driver = Chrome(options=options_)
            driver.get(url)
            time.sleep(3)
            data = driver.page_source
            driver.close()

            # 创建响应对象，必须创建响应对象返回
            res = HtmlResponse(url=url, body=data, encoding='utf-8', request=request)
            return res  # 当放回的是Response时，他不会经过下载中间件
        # 当页面是图书详情页面时，使用下面进行页面渲染，让页面向下滑
        if "list.jd" in url:
            # ===设置不加载页面
            options_ = ChromeOptions()
            # 添加参数,进行隐藏
            options_.add_experimental_option('excludeSwitches', ["enable-automation"])  # 不需要死记硬背
            options_.add_argument('--headless')  # 设置无界面
            driver = Chrome(options=options_)
            driver.maximize_window()  # 页面最大化
            driver.get(url)
            time.sleep(3)
            driver.execute_script('window.scrollBy(0,4000)')
            time.sleep(1)
            driver.execute_script('window.scrollBy(0,4000)')
            time.sleep(1)
            data = driver.page_source

            driver.close()

            # 创建响应对象，必须创建响应对象返回
            res = HtmlResponse(url=url, body=data, encoding='utf-8', request=request)
            return res  # 当放回的是Response时，他不会经过下载中间件

# class JdprojectSpiderMiddleware:
#     # Not all methods need to be defined. If a method is not defined,
#     # scrapy acts as if the spider middleware does not modify the
#     # passed objects.
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         # This method is used by Scrapy to create your spiders.
#         s = cls()
#         crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
#         return s
#
#     def process_spider_input(self, response, spider):
#         # Called for each response that goes through the spider
#         # middleware and into the spider.
#
#         # Should return None or raise an exception.
#         return None
#
#     def process_spider_output(self, response, result, spider):
#         # Called with the results returned from the Spider, after
#         # it has processed the response.
#
#         # Must return an iterable of Request, or item objects.
#         for i in result:
#             yield i
#
#     def process_spider_exception(self, response, exception, spider):
#         # Called when a spider or process_spider_input() method
#         # (from other spider middleware) raises an exception.
#
#         # Should return either None or an iterable of Request or item objects.
#         pass
#
#     def process_start_requests(self, start_requests, spider):
#         # Called with the start requests of the spider, and works
#         # similarly to the process_spider_output() method, except
#         # that it doesn’t have a response associated.
#
#         # Must return only requests (not items).
#         for r in start_requests:
#             yield r
#
#     def spider_opened(self, spider):
#         spider.logger.info('Spider opened: %s' % spider.name)
#
#
# class JdprojectDownloaderMiddleware:
#     # Not all methods need to be defined. If a method is not defined,
#     # scrapy acts as if the downloader middleware does not modify the
#     # passed objects.
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         # This method is used by Scrapy to create your spiders.
#         s = cls()
#         crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
#         return s
#
#     def process_request(self, request, spider):
#         # Called for each request that goes through the downloader
#         # middleware.
#
#         # Must either:
#         # - return None: continue processing this request
#         # - or return a Response object
#         # - or return a Request object
#         # - or raise IgnoreRequest: process_exception() methods of
#         #   installed downloader middleware will be called
#         return None
#
#     def process_response(self, request, response, spider):
#         # Called with the response returned from the downloader.
#
#         # Must either;
#         # - return a Response object
#         # - return a Request object
#         # - or raise IgnoreRequest
#         return response
#
#     def process_exception(self, request, exception, spider):
#         # Called when a download handler or a process_request()
#         # (from other downloader middleware) raises an exception.
#
#         # Must either:
#         # - return None: continue processing this exception
#         # - return a Response object: stops process_exception() chain
#         # - return a Request object: stops process_exception() chain
#         pass
#
#     def spider_opened(self, spider):
#         spider.logger.info('Spider opened: %s' % spider.name)
