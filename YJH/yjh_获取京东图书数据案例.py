import time

from selenium.webdriver import Chrome
from selenium.common.exceptions import TimeoutException
from lxml import etree
import json
from selenium.webdriver import ChromeOptions
if __name__ == '__main__':
    #创建浏览器对象
    options_ = ChromeOptions()
    # 添加参数,进行隐藏
    options_.add_experimental_option('excludeSwitches', ["enable-automation"])  # 不需要死记硬背

    chrome_obj = Chrome(options=options_)
    #设置超时参数
    chrome_obj.set_page_load_timeout(5)
    #打开淘宝首页
    try:
        chrome_obj.get('https://www.jd.com/')
    except TimeoutException:
        print('主页渲染超时了.......')
    #定位到搜索框
    time.sleep(1)
    input_obj=chrome_obj.find_element_by_xpath('//*[@id="key"]')
    input_obj.send_keys('小说')
    #点击搜索
    time.sleep(0.5)
    click_obj=chrome_obj.find_element_by_xpath('//*[@id="search"]/div/div[2]/button')
    click_obj.click()
    #页面的滚动
    for i in range(5):  # 0 1
        time.sleep(0.5)
        j = (i + 1) * 1000  # 1000 2000
        js_ = f'document.documentElement.scrollTop={j}'
        chrome_obj.execute_script(js_)
    #页面等待，数据加载完
    time.sleep(3)
    #获取网页源代码
    html_data=chrome_obj.page_source
    #数据提取
    html_obj=etree.HTML(html_data)
    #书名列表
    title_list=html_obj.xpath('//div[@class="p-name p-name-type-2"]/a[@target="_blank"]/em/text()[1]')
    print(len(title_list))
    print(title_list)
    price_list=html_obj.xpath('//div/div[@class="p-price"]/strong/i/text()')
    print(len(price_list))
    print(price_list)
    with open('小说01.json','w',encoding='utf-8') as f:
        for i in range(len(title_list)):
            dict_={}
            dict_[title_list[i]]=price_list[i]
            json_data=json.dumps(dict_,ensure_ascii=False)+',\n'
            f.write(json_data)

#?: 为什么京东的网页有时打开需要登录有时不用























































































































































