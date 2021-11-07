#! /usr/bin/env python
# -*- coding: utf-8 -*-
#@author：严健华
#@time：2021/10/23-9:24
#@email：yanjianhua29@163.com

"""
1.ffmpeg这个工具进行视频的合成: 终端合成
    -- 写入视频文件的名称
    -- 如果文件名称存在特殊字符,可能会导致视频合成失败..
    -- 空格, / \ & : |
"""
import os
import requests
from lxml import etree
import re

if __name__ == '__main__':
    # 主页url的获取
    # url_ = input('请输入视频主页url:')
    url_ = 'https://www.bilibili.com/bangumi/play/ep312847?from=search&seid=18423628987931500171&spm_id_from=333.337.0.0'
    # url_ = 'https://www.bilibili.com/bangumi/play/ep424605'
    # print("主页的url:", url_)

    # 手动构造请求头参数
    headers_ = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30',
        'Cookie': "b_ut=-1; i-wanna-go-back=1; _uuid=679560DA-9B9A-0283-29AF-22F41FBF7A2749140infoc; buvid3=C7659720-2614-4FB3-9D20-AC2143DD5CA1148820infoc; b_nut=1633789449; buvid_fp=C7659720-2614-4FB3-9D20-AC2143DD5CA1148820infoc; LIVE_BUVID=AUTO9016337894845817; blackside_state=1; rpdid=|(umYk~)kY|R0J'uYJRku|))l; CURRENT_BLACKGAP=0; bp_t_offset_503093758=581802940002450789; CURRENT_QUALITY=0; CURRENT_FNVAL=80; bp_video_offset_503093758=582929643072948602; fingerprint=bbe25a7d8d027ebfd36a286558e9decf; buvid_fp_plain=ECB0A7BB-841A-4741-8FB1-0BF189409803167642infoc; SESSDATA=f858e159%2C1650378672%2C104e2%2Aa1; bili_jct=8cfb6b57b2f70bfd0f649f2e845a656a; DedeUserID=15589240; DedeUserID__ckMd5=0799419a1777f201; sid=586pd6d6; PVID=1; innersign=0",
        'Referer': 'https://search.bilibili.com/'
    }

    # 对主页发送请求,获取响应数据
    response_ = requests.get(url_, headers=headers_)
    data_str = response_.text

    # 解析video url 以及 audio url
    html_obj = etree.HTML(data_str)
    url_str = html_obj.xpath('//script[contains(text(),"window.__playinfo__")]/text()')[0]
    # print(url_str)
    video_url = re.findall(r'"indexRange":"995-9450"},"frameRate":"29.412","codecid":7,"baseUrl":"(.*?)"', url_str)[0]
    # video_url = re.findall(r'"SegmentBase":{"Initialization":"0-995","indexRange":"996-4303"},"frameRate":"24.390","codecid":7,"baseUrl":"(.*?)"', url_str)[0] #国王排名
    audio_url = re.findall(r'"indexRange":"920-9399"},"frameRate":"","codecid":0,"baseUrl":"(.*?)"', url_str)[0]
    # audio_url = re.findall(r'"SegmentBase":{"Initialization":"0-919","indexRange":"920-4239"},"frameRate":"","codecid":0,"baseUrl":"(.*?)"', url_str)[0] #国王排名
    print("纯视频url:", video_url)
    print("纯音频url:", audio_url)

    # 提取视频名称
    name_  = html_obj.xpath('//div[@class="media-right"]/a/@title')[0]
    print('视频名称为:', name_)
    # 视频名称特殊字符的处理
    name_ = name_.replace('/', '')
    name_ = name_.replace('&', '')
    name_ = name_.replace(':', '')
    name_ = name_.replace('|', '')
    name_ = name_.replace(' ', '')

    # 请求video,audio数据
    headers_url = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30',
        'Referer': url_
    }

    # 多媒体文件的响应对象
    response_video = requests.get(video_url, headers=headers_url, stream=True)
    print('视频响应码',response_video.status_code)
    response_audio = requests.get(audio_url, headers=headers_url, stream=True)
    print('音频响应码',response_audio.status_code)

    video_size = int(int(response_video.headers['content-length']) / 1024)
    audio_size = int(int(response_audio.headers['content-length']) / 1024)

    # 提取字节数据
    data_video = response_video.content
    data_audio = response_audio.content

    # 保存: video文件.mp4 audio文件.mp3 > 视频文件.mp4
    new_name = name_ + '!'

    with open(f'{new_name}.mp4', 'wb') as f:
        f.write(data_video)
        print(f'{new_name}纯视频文件下载成功...,大小为:{video_size}KB, {int(video_size/1024)}MB...')

    with open(f'{new_name}.mp3', 'wb') as f:
        f.write(data_audio)
        print(f'{new_name}音频文件下载成功...,大小为:{audio_size}KB, {int(audio_size/1024)}MB...')

    # 视频的合成
    os.system(f'ffmpeg -i "{new_name}.mp4" -i "{new_name}.mp3" -c copy "{name_}.mp4" -loglevel quiet')

    # 视频合成结果打印
    mv_size = int(int(os.stat(f'{name_}.mp4').st_size) / 1024)
    print(f'{name_}视频合成成功...,大小为:{mv_size}KB,{int(mv_size/1024)}MB...')

    # 移除纯视频,纯音频文件
    os.remove(f'{new_name}.mp4')
    os.remove(f'{new_name}.mp3')
