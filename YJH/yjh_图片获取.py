"""
www.ku66.net
参照代码
1. 主页:https://www.ku66.net/
2. 列表页
3. 详情页(图片)
    -- 多页,,翻页
    -- 页数不一定,8页,11页,页数,
    -- 分类的名称,,A类文件夹(A图片) , B类(B图片)
"""
import re

import os

"""
1.确认数据类型:
    --大体上分为两个分类
      -- A:html格式的数据,,json格式的数据呢
        -- html格式的数据, 十个数据...获取十个a标签里面的href属性: 对应的详情页的url
      -- B:
"""

import requests
from lxml import etree

if __name__ == '__main__':
    b_ = 1  # 总计数器
    # 主页的url
    url_ = 'https://www.ku66.net/r/14/index.html'

    # 手动构造一下请求头的参数
    headers_ = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'Referer': "https://www.ku66.net/"
    }

    # 主页数据的获取
    response_ = requests.get(url_, headers=headers_, )
    data_ = response_.text

    # 解析: 进入列表页//div[@class="SpecBox indexSpec fc"]/ul/li/a/@href
    html_obj = etree.HTML(data_)
    url_list = html_obj.xpath('//div[@class="TypeList"]/ul/li/a/@href')
    print("主页解析:", url_list)  # 得到十个列表页的url

    # 循环进入每一个列表页
    # for url_a in url_list:  # 单个类表页的url  //div[@class="TypeList"]/ul/li/a/@href
        # 去获取详情页的url
        # response_a = requests.get(url_a, headers=headers_)
        # data_a = response_a.text
        # html_obj_a = etree.HTML(data_a)
        # url_list_a = html_obj_a.xpath('//div[@class="TypeList"]/ul/li/a/@href')
        # print("列表页解析:", url_list_a)

        # 进入详情页: jpg的图片的url数据
    for url_b in url_list:  # https://www.ku66.net/r/5/34986.html
        print("详情页的url:", url_b)
        # 详情页的获取的数据是url,html里面的,数量是每一页八张,八个数据
        response_b = requests.get(url_b, headers=headers_)

        # 获取页数: 数据的编码格式不是utf-8
        data_b = response_b.content.decode('gbk')  # 火眼金睛

        html_obj_b = etree.HTML(data_b)
        pages_str = html_obj_b.xpath('//div[@class="NewPages"]/ul/li[1]/a/text()')[0]
        print(pages_str)  # 共11页:

        # 使用正则提取数字: 页数数据
        pages_ = int(re.findall(r'\d+', pages_str)[0])
        print("页数为:", pages_, type(pages_))

        # 名称的获取
        name_ = html_obj_b.xpath('//title/text()')[0]
        print('名称是:', name_)

        # 创建单独的文件夹
        os.mkdir(name_)

        # 获取图片数据,进行保存,翻页
        for i in range(pages_):  # 11: 0 1 2
            if i == 0:
                page_url = url_b
            else:
                j = i + 1
                page_url = re.sub(r'\.html', f'_{j}.html', url_b)
            print('翻页的url:', page_url)

            response_c = requests.get(page_url, headers=headers_)
            data_c = response_c.text
            html_obj_c = etree.HTML(data_c)
            url_list_c = html_obj_c.xpath('//div[@class="content"]/img/@src')
            print('单页每一图片的url:', url_list_c)

            # 保存图片到本地: 来两个计数器. 计算单类型图片, 总图片数量
            a_ = 1
            # 获取到当前路径
            pwd_ = os.getcwd()

            for url_c in url_list_c:
                """图片的获取"""
                response_d = requests.get(url_c, headers=headers_)
                data_d = response_d.content
                #      项目根目录   创建出来的文件夹 数字单类型
                with open(pwd_ + "\\" + name_ + "\\"f'{a_}+{b_}.jpg', 'wb') as f:
                    f.write(data_d)
                print(f'本类型第{a_}下载成功......')
                print(f'总共第{b_}下载成功......')
                a_ += 1
                b_ += 1

"""
详情页翻页的注意点,,,,
url_1 =   https://www.ku66.net/r/5/34986.html
url_2 =   https://www.ku66.net/r/5/34986_2.html
url_3 =   https://www.ku66.net/r/5/34986_3.html
url_4 =   https://www.ku66.net/r/5/34986_4.html    
第二页怎么获取
无法进行格式化输出:
1. 以前的url是自己直接复制的
url_1 =   https://www.ku66.net/r/5/34986.html{}

2. 现在的详情页的url是解析得到的,,,保存在变量里面的,,,
url_1
url_2
使用正则让url进行替换,,,达到翻页的效果.......

正则的话..sub.
字符串  ..replace
"""

