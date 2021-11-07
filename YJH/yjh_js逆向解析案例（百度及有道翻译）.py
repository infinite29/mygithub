import time
import random
import hashlib

import jsonpath
import requests
import execjs

# 有道翻译
# if __name__ == '__main__':
#     while True:
#         # 请输入要翻译的内容
#         data_=input('请输入你要翻译的内容：')
#         # 确认URL
#         url_='https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
#         # 构造请求头参数
#         headers_={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
#                   'Cookie':'OUTFOX_SEARCH_USER_ID_NCOO=1634865557.1147249; OUTFOX_SEARCH_USER_ID="-1256743721@10.169.0.102"; fanyi-ad-id=114757; fanyi-ad-closed=1; JSESSIONID=aaacOGNb6rRtCaPItabUx; ___rl__test__cookies=1629957541441',
#                   'Referer':'https://fanyi.youdao.com/'
#                   }
#         # lts是以毫秒单位的时间戳
#         lts_=str(int(time.time() * 1000))
#         # salt：lts+随机的一位数
#         salt_=lts_+str(random.randint(0,9))
#         # sign: "fanyideskweb" + e（你好） + i（salt）+ "Y2FYu%TNSbMCxc3t2u^XT" 进行md5加密
#         demo_ = "fanyideskweb" + data_ + salt_ + "Y2FYu%TNSbMCxc3t2u^XT"
#         # demo_ = "fanyideskweb" + data_ + salt_ + "Tbh5E8=q6U3EXe+&L[4c@"
#         sign_=hashlib.md5(demo_.encode()).hexdigest()
#
#         # form表单数据
#         form_data={
#         'i': data_,
#         'from': 'AUTO',
#         'to':'AUTO',
#         'smartrsult': 'dict',
#         'client': 'fanyideskweb',
#         'salt': salt_,
#         'sign': sign_,
#         'lts': lts_,
#         'bv': '1e9538f95b23257ede9acdc941c8e1f8',
#         'doctype': 'json',
#         'version': '2.1',
#         'keyfrom': 'fanyi.web',
#         'action': 'FY_BY_CLICKBUTTION'
#         }
#
#         try:
#             # 发送请求,得到响应数据
#             response_ = requests.post(url_, headers=headers_, data=form_data)
#             # print(response_.text)
#
#             # 数据的提取
#             res_ = response_.json()
#             res_data = jsonpath.jsonpath(res_, '$..tgt')[0]
#             print(f'翻译之后的结果是:{res_data}')
#         except:
#             print('输入不规范,请输入正确的格式')
#             continue # 是在程序末尾 可 忽略

#百度翻译
if __name__ == '__main__':
    while True:
        data_=input('请输入要翻译的内容：')
        # 确认目标URL
        url_='https://fanyi.baidu.com/v2transapi?from=zh&to=en'
        # 手动构造请求头信息
        headers_ = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
            'Cookie': 'BAIDUID=307A0146123DF94B0A1AE33E86D6653A:FG=1; BIDUPSID=307A0146123DF94B0A1AE33E86D6653A; PSTM=1622279288; __yjs_duid=1_75dff6c9bc2c4d17395c7cd6caca54d01622893940654; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BDRCVFR[F9QspfwzDnD]=788S7gSrw2CuvqEuvk-Uh7vQhP8; delPer=0; PSINO=6; H_PS_PSSID=26350; BA_HECTOR=a1a18h802h0k818h3j1gifcb40q; BCLID=7812065578775462711; BDSFRCVID=3P0OJexroG0YyvRH5z7uh2tDM_weG7bTDYLEOwXPsp3LGJLVJeC6EG0Pts1-dEu-EHtdogKKBgOTHl4F_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tR3aQ5rtKRTffjrnhPF3DpOQXP6-hnjy3bRkX4Q4WI50MP5dDROUXq4Wbttf5q3RymJ42-39LPO2hpRjyxv4y4Ldj4oxJpOJ-bCL0p5aHl51fbbvbURvL4-g3-7QtU5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-jBRIE3-oJqC--bDI93D; BCLID_BFESS=7812065578775462711; BDSFRCVID_BFESS=3P0OJexroG0YyvRH5z7uh2tDM_weG7bTDYLEOwXPsp3LGJLVJeC6EG0Pts1-dEu-EHtdogKKBgOTHl4F_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tR3aQ5rtKRTffjrnhPF3DpOQXP6-hnjy3bRkX4Q4WI50MP5dDROUXq4Wbttf5q3RymJ42-39LPO2hpRjyxv4y4Ldj4oxJpOJ-bCL0p5aHl51fbbvbURvL4-g3-7QtU5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-jBRIE3-oJqC--bDI93D; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1628580384,1629793754,1629991273; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1629991273; __yjs_st=2_YWUxZTdjNWRkNDU0ODBjODAzM2UxZmVmYjdlMjkyYTFkYzliMTExZGRhZTE2NzYyYzJjMjUxY2U4YTBlMmM4MGI5MzRjNTA3MWE3NmVjODY3ODJkYzcyZTM1OWFkZWQ3ZTM0ZGUyNDFlODdiMGI5NjNjYzYwNmE2NmIxODlkNTcwNjE3ZjgzYzk3MzgzMGFjN2UzYTM3ZTViMDMyNTQ3OGI3N2YyYzQzMTU5ZGZhMzAxY2E4NTE3ZTUxMjkxMWE0MjRiOWJkMDVlZDc1NzM3ZjBiZDczNmQ3Y2ViMzYzY2RlNTliNWY3ZjYyM2ExZDA0NzdiNWY0OTkwOGZmNDMyN183XzI1MWM2OTdm; ab_sr=1.0.1_OTA0NjY5M2Y2YzQzMTY3YjBjNzM0MTVmMzE4MjczOWM2NDEwOGVjMjhiY2FkYWFjMzY5MjFiODRmODY5YzU4MzBkOWRlMDEyMjNhYmE0ODNlYjM3ZGMwZDQ2YTc3MDU1YWY4YWQ0MGJmNjMwMzg2ZTY4ZTc0NGJmYTc2YjFlNDY2ZjliOGY0MWNjYmJhOWY2MzI5ODg2MDYyNjI0NzlhMQ==; Hm_lvt_246a5e7d3670cfba258184e42d902b31=1629993116; Hm_lpvt_246a5e7d3670cfba258184e42d902b31=1629993119',
            'Referer': 'https://fanyi.baidu.com/?aldtype=16047'
        }
        # sign值生成
        # 1、获取对应的JS代码
        with open('baidu01.js','r') as f:
            js_data=f.read()
        # 2、实例化js对象
        js_obj=execjs.compile(js_data)
        # 3、指定调用部分
        sign_=js_obj.call('e',data_)
        # print(sign_)
        # form表单
        form_data={
        'from': 'zh',
        'to': 'en',
        'query': data_,
        'transtype': 'translang',
        'simple_means_flag': '3',
        'sign': sign_,
        'token': 'e0420d1bab38e480554facbed1a7a93d',
        'domain': 'common',
        }
    # 发送网络请求,获取响应数据
        response_ = requests.post(url_, headers=headers_, data=form_data)
        # print(response_.text)

        # 数据的提取
        py_data = response_.json()
        # print(py_data)
        res_ = jsonpath.jsonpath(py_data, '$..dst')[0]
        print(f'翻译结果为:{res_}')








# 你好
'''
'from': 'zh',
'to': 'en',
'query': data_,
'transtype': 'translang',
'simple_means_flag': '3',
'sign': '232427.485594',
'token': 'e0420d1bab38e480554facbed1a7a93d',
'domain': 'common',
'''
# 阳光
'''
from: zh
to: en
query: 阳光
transtype: translang
simple_means_flag: 3
sign: 138371.458674
token: e0420d1bab38e480554facbed1a7a93d
domain: common
'''


































































































    


















































































































