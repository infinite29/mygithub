import requests
import jsonpath
import json
if __name__ == '__main__':
    #1、确认URL

    page=int(input('输入的页数：'))
    for i in range(page):
        url_=f'https://movie.douban.com/j/search_subjects?type=tv&tag=%E5%9B%BD%E4%BA%A7%E5%89%A7&sort=recommend&page_limit=20&page_start={20*i}'
    #手动构造用户代理数据

        headers_={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
                  'Cookie':'bid=TKF0d8mx9J4; gr_user_id=49370ec8-2200-4c14-bbaf-8874889c0145; __gads=ID=fcd59e082308ff67-2292cda316c9002a:T=1622352956:RT=1622352956:S=ALNI_MbJ5udFKLA3ih7lVi1-jBb8BizV6Q; viewed="6518605_1068920_4820710_6082808_4913064_1007305"; __yadk_uid=a4NRqUceFP11TlqXJh0ab1ZqGivci8oO; ll="118291"; __utma=30149280.1619024959.1622352906.1622462920.1627394559.4; __utmc=30149280; __utmz=30149280.1627394559.4.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; __utmb=30149280.1.10.1627394559; __utma=223695111.182711047.1622354138.1622463444.1627394559.3; __utmb=223695111.0.10.1627394559; __utmc=223695111; __utmz=223695111.1627394559.3.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; ap_v=0,6.0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1627394559%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; _vwo_uuid_v2=D19D81EE282A00B4439FEA3C87C5367CC|973314561d278c4a199254f962010547; _pk_id.100001.4cf6=faa33f18d5916e7b.1622354138.3.1627394824.1622464085.'
                  }
    #2、发送请求获取响应
        respose_=requests.get(url_,headers=headers_)
        data_=respose_.json()

    # 3、提取相应的数据
        title_=jsonpath.jsonpath(data_,'$..title')
        episodes_info_=jsonpath.jsonpath(data_,'$..episodes_info')
        rate_=jsonpath.jsonpath(data_,'$..rate')
    # 4、保存数据
        with open(f'douban_movie.json','a',encoding='utf-8') as f:
        # 把数据取出来,,构建单独的字典,键值对,,写入文件
            for i in range(len(title_)):
                dict_title=dict_episodes_info=dict_rate={}  # 每一次循环,都有一个空字典
                dict_title['剧名'] = title_[i]
                dict_episodes_info['更新情况'] = episodes_info_[i]
                dict_rate['评分'] = rate_[i]
                json_data= json.dumps(dict_title, ensure_ascii=False)+','
                json_data= json.dumps(dict_episodes_info, ensure_ascii=False) + ','
                json_data= json.dumps(dict_rate, ensure_ascii=False) + '\n'
                f.write(json_data)































































