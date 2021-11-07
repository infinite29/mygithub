from lxml import etree
import time
import requests
import json
if __name__ == '__main__':
    #1、确认目标的URL
    url_='https://music.163.com/discover/toplist'
    # 手动构造一些请求有的信息参数
    headers_={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
             , 'Cookie':'_iuqxldmzr_=32; _ntes_nnid=0027fdeb458cd314df531f2a7f25fef2,1626705871116; _ntes_nuid=0027fdeb458cd314df531f2a7f25fef2; NMTID=00OPqTGtDp7WvE9gUzYi-qaIOzpuAIAAAF6vznDhA; WEVNSM=1.0.0; WNMCID=ksomrb.1626705871455.01.0; WM_TID=kInqtMdgBTxABRBFUQd6zZ%2FrX4PliDaQ; WM_NI=2AzGcRv0T0EhThHMjShxgiygbTKFS7MHT07tIAMrZ%2FZq%2FQ%2BKh1rTvoKpzsSQqn3aayGZd%2FUG4Ehhn69vCR0OYumZHeQQ6BBoh%2BvtTh%2B0PUAvcKFPGqp0bXowuDUYm0l7ejQ%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eed9b83eb1a8be93d55d97868aa2c54f978a8aaff567bcb2fcb7f83eaf96aeb5b22af0fea7c3b92af29fb6a8e25ab6f09cd1c86498b888aee959aca8a98afc6da28c85a7d23d8f989cd1b6808b9f8393d9259aafe1b2aa41acefbeb5f56589b0b694d25bb3b2fd82e4738586acd0d84df89ba889ed3efbaa8db3b3459baba3bbcb6f938ffaa3c165acf5ba95d764e9f0a0b6c47ea1958ab1c67bb4f0aeb9ee7db79c9bbaf03cb0e9ab8bd437e2a3; JSESSIONID-WYYY=Utosat8jg5SgBGO8eJAb%2BeWkJQzRIIMtyVzZEwjiy%2ByhDthaVSoMZMktBiAXB5vQpe0nKMSHHASBvhZPAcvsbHZYXoFw14ss3rfDJgocbRmstwsvUaCh2kdHgA201AYHJ9nHZaythToPrDRZTADVTgZSH%5CsKksM%5C6NKWhpcsqrmVghZB%3A1628606886162'
             ,'referer':'https://music.163.com/'
    }
    #2、发送请求获取响应
    response_=requests.get(url_,headers=headers_)
    data_=response_.text
    print(type(data_))
    #3、提取数据
    html_=etree.HTML(data_)
    print(type(html_))
    title_list = html_.xpath('//ul[@class="f-hide"]/li/a/text()')
    url_list = html_.xpath('//ul[@class="f-hide"]/li/a/@href')
    print(title_list, len(title_list))
    print(url_list, len(url_list))

    """
    xpath语法提取到的数据,,也是一个列表.....
    """
    # 4.保存
    with open('网易云01.json', 'w', encoding='utf-8') as f:
        for i in range(len(title_list)):
            dict_ = {}
            dict_[title_list[i]] = url_list[i]
            json_data = json.dumps(dict_, ensure_ascii=False) + ',\n'
            f.write(json_data)













