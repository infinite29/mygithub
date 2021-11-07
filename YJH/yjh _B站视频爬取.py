# import os
import os

import requests
from lxml import etree
import re

if __name__ == '__main__':
    # 主页url的获取
    url_ = input('请输入视频主页url:')
    print("主页的url:", url_)

    # 手动构造请求头参数
    headers_ = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'Cookie': "buvid3=D9B58E55-B60C-4663-D709-9FB17207432F58160infoc; CURRENT_FNVAL=80; _uuid=395F4501-0913-A8C9-5EC3-7C6A09FE467660435infoc; blackside_state=1; rpdid=|(u)mY))RJkk0J'uYk)Y|~mmR; fingerprint=310b96c7e29d155d62d58087a4546599; buvid_fp=D9B58E55-B60C-4663-D709-9FB17207432F58160infoc; buvid_fp_plain=78F0BD93-AECA-49EC-A237-8897483E8172148800infoc; DedeUserID=15484907; DedeUserID__ckMd5=f7646e9fa1b7f128; SESSDATA=4f1c1c65%2C1644222729%2C9e988*81; bili_jct=71f4063a948209325f8409ead183919e; CURRENT_QUALITY=80; bsource=search_baidu; CURRENT_BLACKGAP=1; sid=a0wikcep; innersign=1; PVID=3",
        'Referer': 'https://search.bilibili.com/all?keyword=iu&from_source=webtop_search&spm_id_from=333.5'
    }

    # 对主页发送请求,获取响应数据
    response_ = requests.get(url_, headers=headers_)
    data_str = response_.text

    # 解析video url 以及 audio url
    html_obj = etree.HTML(data_str)
    url_str = html_obj.xpath('//script[contains(text(),"window.__playinfo__")]/text()')[0]
    video_url = re.findall(r'"video":\[{"id":\d+,"baseUrl":"(.*?)"', url_str)[0]
    audio_url = re.findall(r'"audio":\[{"id":\d+,"baseUrl":"(.*?)"', url_str)[0]
    print("纯视频url:", video_url)
    print("纯音频url:", audio_url)

    # 提取视频名称
    res_ = html_obj.xpath('//title/text()')[0]
    name_ = re.findall(r'(.*?)_哔哩哔哩', res_)[0]
    print('视频名称为:', name_)

    # 请求video,audio数据
    headers_url = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'Referer': url_
    }

    response_video = requests.get(video_url, headers=headers_url)
    response_audio = requests.get(audio_url, headers=headers_url)

    # 提取字节数据
    data_video = response_video.content
    data_audio = response_audio.content

    # 保存: video文件.mp4 audio文件.mp3 > 视频文件.mp4
    new_name = name_ + '!'

    with open(f'{new_name}.mp4', 'wb') as f:
        f.write(data_video)

    with open(f'{new_name}.mp3', 'wb') as f:
        f.write(data_audio)

    # 视频的合成
    os.system(f'ffmpeg -i "{new_name}.mp4" -i "{new_name}.mp3" -c copy "{name_}.mp4"')

    # 移除纯视频,纯音频文件
    os.remove(f'{new_name}.mp4')
    os.remove(f'{new_name}.mp3')