#! /usr/bin/env python
# coding: utf-8
#@author：严健华
#@time：2021/10/1-11:23
#@email：yanjianhua29@163.com
import re
import time

import jsonpath
import requests
import execjs
from bs4 import BeautifulSoup
from lxml import etree
from openpyxl.workbook import Workbook
from selenium.webdriver import ChromeOptions
from selenium.webdriver import Chrome
from selenium.common.exceptions import TimeoutException

if __name__ == '__main__':
    while True:
        key_word= input('请输入要搜索的内容：') # 搜索关键词
        # url_menu=[]
        # for i in range(60):
        # # url_=f'https://www.aliexpress.com/wholesale?trafficChannel=main&d=y&CatId=0&SearchText={data_}'
        #     url_=f'https://www.aliexpress.com/wholesale?trafficChannel=main&d=y&CatId=0&SearchText={data_}&ltype=wholesale&SortType=default&page={i+1}'
        #     url_menu.append(url_)
        url_menu=[f'https://www.aliexpress.com/wholesale?trafficChannel=main&d=y&CatId=0&SearchText={key_word}&ltype=wholesale&SortType=default&page={i+1}' for i in range(60)]
        # print(url_menu)
        # 手动构造请求头信息
        headers_ = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
            'cookie':'_US; aep_usuc_f=site=glo&c_tp=USD&region=CN&b_locale=en_US; xman_t=fykD0gBeF2VoseRI5rEr/K3eFrWg/XjLlfOs3HtI7nlLBjG1Ie4kzKUtcIeHPSHL; xman_f=hKb+y5mh0Vq9cuIkzwh85yP8J8HltZ6pAic0hT16HPO4Mjw5kB7y29KeD+MdONSzJ6fRji9NZMyzIchzAYJXkyHD6Am9W47HJfXHug/TB2orVezIDMD3VA==; xlly_s=1; cna=wlHXGYeMjyMCAbSPdI9orJQ9; _gid=GA1.2.1843294626.1633053843; _gcl_au=1.1.284378522.1633053844; XSRF-TOKEN=ecc3899b-7869-4266-ad26-6f1236cd090e; _m_h5_tk=31aa30b7c0d2ef52a4ec85560e4d840a_1633080701401; _m_h5_tk_enc=3f601675433423c275dad198897ce6c3; _ga=GA1.1.933356438.1633053843; aep_history=keywords%5E%0Akeywords%09%0A%0Aproduct_selloffer%5E%0Aproduct_selloffer%091005002661899483%091005002466679433%091005001828282979%091005003098107502%091005002129463368%091005002630725787%091005002932240747%091005001828282979; intl_common_forever=/SeG+TLI6dl5I2UhV1I1rzGfBTo+opwL2+I7JsD9Rmo9Scf45zfRKA==; xman_us_f=x_locale=en_US&x_l=1&x_c_chg=0&x_as_i=%7B%22cookieCacheEffectTime%22%3A1633082741925%2C%22isCookieCache%22%3A%22Y%22%2C%22ms%22%3A%220%22%7D&acs_rt=c20b8b12106e4e2298e9c58353f738a8; _ga_VED1YSGNC7=GS1.1.1633080353.6.1.1633082559.0; JSESSIONID=8701E473DA333ECE9E8B73D3F94749F4; tfstk=cX4fBOv9qKvb-uswuS1yQhpIj83lC2BSZiMYGlO4VUqFjT9EHF104ekIdOZMEVltN; l=eBgGwwU7gh3zD5IMBO5Churza77TVpRXcsPzaNbMiIncC6VdgDJhAPtQc42jUL-RR8XVioLp44v7xnetVFe0JyMXCT2IrYnERDQXQe8C.; isg=BDIyZsS-hxtE2LsnQOkFX2V2g3gUwzZdIiVmTvwF9emkj8KJ5VFcbY2pfysz_671',
            'Referer': 'https://www.aliexpress.com/',
            'authority':'www.aliexpress.com',
            'method':'GET',
            'scheme':'https',
            'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding':'gzip, deflate, br',
            'accept-language':'zh-CN,zh;q=0.9',
            'cache-control':'no-cache',
            'pragma':'no-cache',
            'sec-ch-ua':'"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
            'sec-ch-ua-mobile':'?0',
            'ec-ch-ua-platform':'"Windows"',
            'sec-fetch-dest':'document',
            'sec-fetch-mode':'navigate',
            'sec-fetch-site':'same-origin',
            'sec-fetch-user':'?1',
            'upgrade-insecure-requests':'1',
        }
        proxies_ = {
                    "http": "47.100.14.22:9006",
                    "http": "192.168.0.103:8286",
                    "http": "140.255.139.135:3256",
                    "http": "140.255.139.115:3256",
                    "http": "121.230.210.58:3256",
                    }    # 手动添加代理
        # 新建工作簿
        wb = Workbook()
        # 选择默认的工作表
        sheet = wb.active
        # 给工作表重命名
        sheet.title = '商品链接'
        # 给工作表添加标题
        # row_title=['链接页数']
        row_title=[f'商品{i+1}链接' for i in range(60)]
        row_title.insert(0,'链接页数')
        # print(row_title)
        sheet.append(row_title)
        for index,item in enumerate(url_menu):
            # 2、发送请求获取响应
            # print(f'第{index+1}页的url:',item)
            response_ = requests.get(item,headers=headers_,proxies=proxies_)
            data_ = response_.text
            # print(data_)
            # 3、正则提取数据
            url_ID = re.findall(r'"productId":(.*?),', data_)  # 获取产品ID
            # 判断页面加载是否成功
            if url_ID:
                print(f'第{index+1}页的url的数量:', len(url_ID))
                url_list = [f'第{index+1}页的链接',]
                for i in url_ID:
                    url_mix = 'https://www.aliexpress.com/item/' + i + '.html'  # URL拼接
                    url_list.append(url_mix)
                # print(url_list)
                sheet.append(url_list)
            else:
                print(f'第{index+1}页面加载不成功')
                break

        # 保存文件
        wb.save(f'{key_word}商品链接表.xlsx')
























# 商品页URL分析
'''
https://www.aliexpress.com/glosearch/api/product?trafficChannel=main&d=y&CatId=0&SearchText=%E6%89%8B%E6%9C%BA&ltype=wholesale&SortType=default&page=2&origin=y&pv_feature=4001201523871,32846212848,4001291994485,1005001769274036,1005001967006694,1005002224662668,1005001901817517,1005002341887484,1005003212802383,1005003141695590,1005003086849420,1005003093109586,1005002941151665,1005003325221509,1005002288551640,1005002863296689,1005003234126625,1005002322310733,1005003081376946,1005001819064225,32717611421,4000078214704,1005002571653275,1005002995598149,1005003333052254,1005001452960369,1005003197626429,1005002882170876,1005002439996297,1005003205699345,1005002383264963,1005002753347510,32846404800,1005002965708362,1005003307239001,1005001639600335,1005002037696688,32793479920,1005003007663163,1005003056778014
1、https://www.aliexpress.com/item/1005001828282979.html?spm=a2g0o.productlist.0.0.207862e2sTNSNF&algo_pvid=ed4df564-116f-4712-8ec1-43fed41b5cb0&algo_exp_id=ed4df564-116f-4712-8ec1-43fed41b5cb0-2&pdp_ext_f=%7B%22sku_id%22%3A%2212000025081517704%22%7D
2、https://www.aliexpress.com/item/1005002418816521.html?spm=a2g0o.productlist.0.0.207862e2sTNSNF&algo_pvid=ed4df564-116f-4712-8ec1-43fed41b5cb0&algo_exp_id=ed4df564-116f-4712-8ec1-43fed41b5cb0-1&pdp_ext_f=%7B%22sku_id%22%3A%2212000025099793867%22%7D
3、https://www.aliexpress.com/item/1005002466679433.html?spm=a2g0o.productlist.0.0.207862e2sTNSNF&algo_pvid=ed4df564-116f-4712-8ec1-43fed41b5cb0&algo_exp_id=ed4df564-116f-4712-8ec1-43fed41b5cb0-0&pdp_ext_f=%7B%22sku_id%22%3A%2212000024784607418%22%7D

1、https://www.aliexpress.com/wholesale?trafficChannel=main&d=y&CatId=0&SearchText=%E6%89%8B%E6%9C%BA&ltype=wholesale&SortType=default&page=1
2、https://www.aliexpress.com/wholesale?trafficChannel=main&d=y&CatId=0&SearchText=%E6%89%8B%E6%9C%BA&ltype=wholesale&SortType=default&page=2
'''


# 翻页cookie分析
"""
1、ali_apache_id=11.180.122.25.1633053841379.255456.4; acs_usuc_t=x_csrf=1a_1oi28y94cu&acs_rt=c20b8b12106e4e2298e9c58353f738a8; intl_locale=en_US; aep_usuc_f=site=glo&c_tp=USD&region=CN&b_locale=en_US; xman_t=fykD0gBeF2VoseRI5rEr/K3eFrWg/XjLlfOs3HtI7nlLBjG1Ie4kzKUtcIeHPSHL; xman_f=hKb+y5mh0Vq9cuIkzwh85yP8J8HltZ6pAic0hT16HPO4Mjw5kB7y29KeD+MdONSzJ6fRji9NZMyzIchzAYJXkyHD6Am9W47HJfXHug/TB2orVezIDMD3VA==; xlly_s=1; cna=wlHXGYeMjyMCAbSPdI9orJQ9; _gid=GA1.2.1843294626.1633053843; _gcl_au=1.1.284378522.1633053844; XSRF-TOKEN=ecc3899b-7869-4266-ad26-6f1236cd090e; _m_h5_tk=e7fb354374f6e0900c6fa8a68bf5d9b0_1633072813253; _m_h5_tk_enc=723a3c129f015a716c87f6983cd3a1a2; aep_history=keywords%5E%0Akeywords%09%0A%0Aproduct_selloffer%5E%0Aproduct_selloffer%091005002661899483%091005002466679433%091005001828282979%091005003098107502%091005002129463368%091005002630725787%091005002932240747%091005002932240747; xman_us_f=x_locale=en_US&x_l=1&x_c_chg=0&x_as_i=%7B%22cookieCacheEffectTime%22%3A1633071913421%2C%22isCookieCache%22%3A%22Y%22%2C%22ms%22%3A%220%22%7D&acs_rt=c20b8b12106e4e2298e9c58353f738a8; intl_common_forever=yArWzUgYVRkZ9xqFBd6I+X7BvSb/uWQCykw6+w8BFex++PQYvcYqSw==; JSESSIONID=6D12288DA2EA457901857074ABC785D2; _ga=GA1.1.933356438.1633053843; _ga_VED1YSGNC7=GS1.1.1633067671.5.1.1633072214.0; l=eBgGwwU7gh3zD5FCBO5Cnurza77TfQRb8sPzaNbMiInca1zcTsS-6NCLUn-M7dtjgt50cetrrLZHDR3k8r438A1_bNMieDuIvGpM-e1..; tfstk=cIV1BVxvKhx14WX2_P_e0KUSN4hcaeSI-OiT5-TaQHhFnw0tvsAea0i5c-xngq3C.; isg=BKioBHZAXR0qQ3GZflsvGaMkeZa60QzbpNeskGLbGCKRvUknCuAUaiu3tVVNjcSz
2、ali_apache_id=11.180.122.25.1633053841379.255456.4; acs_usuc_t=x_csrf=1a_1oi28y94cu&acs_rt=c20b8b12106e4e2298e9c58353f738a8; intl_locale=en_US; aep_usuc_f=site=glo&c_tp=USD&region=CN&b_locale=en_US; xman_t=fykD0gBeF2VoseRI5rEr/K3eFrWg/XjLlfOs3HtI7nlLBjG1Ie4kzKUtcIeHPSHL; xman_f=hKb+y5mh0Vq9cuIkzwh85yP8J8HltZ6pAic0hT16HPO4Mjw5kB7y29KeD+MdONSzJ6fRji9NZMyzIchzAYJXkyHD6Am9W47HJfXHug/TB2orVezIDMD3VA==; xlly_s=1; cna=wlHXGYeMjyMCAbSPdI9orJQ9; _gid=GA1.2.1843294626.1633053843; _gcl_au=1.1.284378522.1633053844; XSRF-TOKEN=ecc3899b-7869-4266-ad26-6f1236cd090e; _m_h5_tk=e7fb354374f6e0900c6fa8a68bf5d9b0_1633072813253; _m_h5_tk_enc=723a3c129f015a716c87f6983cd3a1a2; aep_history=keywords%5E%0Akeywords%09%0A%0Aproduct_selloffer%5E%0Aproduct_selloffer%091005002661899483%091005002466679433%091005001828282979%091005003098107502%091005002129463368%091005002630725787%091005002932240747%091005002932240747; xman_us_f=x_locale=en_US&x_l=1&x_c_chg=0&x_as_i=%7B%22cookieCacheEffectTime%22%3A1633072539557%2C%22isCookieCache%22%3A%22Y%22%2C%22ms%22%3A%220%22%7D&acs_rt=c20b8b12106e4e2298e9c58353f738a8; intl_common_forever=o3GdpKEas3n6aVPqHoh1/g99pWg2iisI+iEZ3WE72+noYeMpQ6Xmmg==; _ga=GA1.1.933356438.1633053843; tfstk=cV7GBbcEyG-6t5xhVPT1OCprNLrdaurwCZ7F8avb4-EMORb6_s4rY0z41WvTFRof.; l=eBgGwwU7gh3zDiKLBO5Cnurza779yIRbzsPzaNbMiInca6phtel7GNCLUnyMSdtjgt5mEetrrLZHDRHJ8baLRx91EJgoeDuIvIJ6Re1..; isg=BNHRDiBZVLbrtLiiT4S2wkKD4N1rPkWwpVClC7NmeBiaWvOs-4--gJz4_C680t3o; _ga_VED1YSGNC7=GS1.1.1633067671.5.1.1633072343.0; JSESSIONID=64B0A913D9EF263A237D8BC9B752FDB1
1、
:authority: www.aliexpress.com
:method: GET
:path: /wholesale?trafficChannel=main&d=y&CatId=0&SearchText=%E6%89%8B%E6%9C%BA&ltype=wholesale&SortType=default&page=1
:scheme: https
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9
cache-control: no-cache
cookie: ali_apache_id=11.180.122.25.1633053841379.255456.4; acs_usuc_t=x_csrf=1a_1oi28y94cu&acs_rt=c20b8b12106e4e2298e9c58353f738a8; intl_locale=en_US; aep_usuc_f=site=glo&c_tp=USD&region=CN&b_locale=en_US; xman_t=fykD0gBeF2VoseRI5rEr/K3eFrWg/XjLlfOs3HtI7nlLBjG1Ie4kzKUtcIeHPSHL; xman_f=hKb+y5mh0Vq9cuIkzwh85yP8J8HltZ6pAic0hT16HPO4Mjw5kB7y29KeD+MdONSzJ6fRji9NZMyzIchzAYJXkyHD6Am9W47HJfXHug/TB2orVezIDMD3VA==; xlly_s=1; cna=wlHXGYeMjyMCAbSPdI9orJQ9; _gid=GA1.2.1843294626.1633053843; _gcl_au=1.1.284378522.1633053844; XSRF-TOKEN=ecc3899b-7869-4266-ad26-6f1236cd090e; aep_history=keywords%5E%0Akeywords%09%0A%0Aproduct_selloffer%5E%0Aproduct_selloffer%091005002661899483%091005002466679433%091005001828282979%091005003098107502%091005002129463368%091005002630725787%091005002932240747%091005001828282979; _m_h5_tk=fa72b7776efd21304ae0c5b7a15bbb6e_1633094923215; _m_h5_tk_enc=f00a2cf59b14c88c5280f2b4c1700128; xman_us_f=x_locale=en_US&x_l=1&x_c_chg=0&x_as_i=%7B%22cookieCacheEffectTime%22%3A1633093480903%2C%22isCookieCache%22%3A%22Y%22%2C%22ms%22%3A%220%22%7D&acs_rt=c20b8b12106e4e2298e9c58353f738a8; intl_common_forever=BP2CHusv1YlcgPYFnuUkLPAK4028aWHo7+Vf8td0Pj5wKPkRQhFJng==; _ga=GA1.1.933356438.1633053843; tfstk=csrdB9xSQ1fH8fDT3yQGF19PxVWGa-vKZpGJ2OeDvaRpwdKpAsDYmoeUuwMrgXBO.; l=eBgGwwU7gh3zD6yyBOfwhurza77O9IRfguPzaNbMiOCPO0Cpt_91W6euhlY9CnGVnsWDR3ukFkxYB4YUwyUIhd6ud4D-Y2iLLdTh.; isg=BCUlEfC2qHOVIMwu-yjahr5nNOFfYtn0afTxhycK3NzWPkSw77MhxBGcyKJIPvGs; _ga_VED1YSGNC7=GS1.1.1633091869.7.1.1633093351.0; JSESSIONID=79ECF92B3B2825B0BBB4B08E72FB7685
pragma: no-cache
referer: https://www.aliexpress.com/wholesale?trafficChannel=main&d=y&CatId=0&SearchText=ipad&ltype=wholesale&SortType=default&page=2
sec-ch-ua: "Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
sec-fetch-dest: document
sec-fetch-mode: navigate
sec-fetch-site: same-origin
sec-fetch-user: ?1
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36
"""
