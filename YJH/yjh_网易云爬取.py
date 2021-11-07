"""
单张图片的获取
"""
# import requests
# from fake_useragent import FakeUserAgent

# if __name__ == '__main__':
    # url_='https://p1.music.126.net/pc3zTiSctSK6XMyKYDOLBw==/109951166189648871.jpg?imageView&quality=89'
    # headers_ = {
    #     'User-Agent': FakeUserAgent().random}
    # # headers_={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
    # res=requests.get(url_,headers=headers_)
    # data_=res.content
    # with open('毛不易1.jpg','wb') as f:
#     #     f.write(data_)
"""
单首非VIP歌曲的下载
"""
# if __name__ == '__main__':
#     url_='https://m801.music.126.net/20210719233433/2206ed6821644d2e7b2389c279785db7/jdyyaac/obj/w5rDlsOJwrLDjj7CmsOj/8809151865/a372/1de7/0121/1ec7c190c8ddfc09e625a406abc04f6b.m4a'
#     headers_ = {
#         'User-Agent': FakeUserAgent().random}
#     res=requests.get(url_,headers=headers_)
#     data_=res.content
#     with open('如果呢.mp3','wb') as f:
#         f.write(data_)

"""
mv的下载
ttps://hef6l6kz.v1d.szbdyd.com:9305/fseeca82d4.a.bdydns.com/1924164272/cloudmusic/obj/core/4026923983/1765d168a505e8a29349ada6d039413c.mp4?wsSecret=684a6a0f745c09a9d4f8b37aae2aafb7&wsTime=1626708459&http_cdnfrom=bdcloud&max_age=31104000&r=csLMxLOSlEBTC8LdFx2MzAZ5vxvlU2mip0JMw3pKvt5Ynwg5%2FrygXV5lofIBDRuMUsRIDzVZRM6dGMNG547khO0JeK99xPOct8YJzf%2BrYBSYMVMhlRRGKGXoS4DfFGvx2UOz5zy5WOnFrbEJTMc8W9xnwh7GsEPu65KTb5J9rTmQ9JjUc6WP0UisfxfRyLJcjn0kIsr2llH1nyWfJY9I3Q%3D%3D&xyip=219.132.164.174&xyct=15&xysc=1&sent_http_access-control-allow-credentials=true&sent_http_cdn-source=bdcloud&sent_http_cache=state&sent_http_access-control-allow-headers=DNT%2CX-CustomHeader%2CKeep-Alive%2CUser-Agent%2CX-Requested-With%2CIf-Modified-Since%2CCache-Control%2CContent-Type%2CRange&sent_http_cdn-user-ip=14.21.96.204&sent_http_cdn-ip=113.96.164.35&sent_http_access-control-allow-methods=GET%2CPOST%2COPTIONS&sent_http_access-control-allow-origin=*&sent_http_access-control-expose-headers=Content-Range%2C%20Last-Modified
"""
# import requests
# from fake_useragent import FakeUserAgent
# if __name__ == '__main__':
#     url_='https://hef6l6kz.v1d.szbdyd.com:9305/fseeca82d4.a.bdydns.com/1924164272/cloudmusic/obj/core/4026923983/1765d168a505e8a29349ada6d039413c.mp4?wsSecret=684a6a0f745c09a9d4f8b37aae2aafb7&wsTime=1626708459&http_cdnfrom=bdcloud&max_age=31104000&r=csLMxLOSlEBTC8LdFx2MzAZ5vxvlU2mip0JMw3pKvt5Ynwg5%2FrygXV5lofIBDRuMUsRIDzVZRM6dGMNG547khO0JeK99xPOct8YJzf%2BrYBSYMVMhlRRGKGXoS4DfFGvx2UOz5zy5WOnFrbEJTMc8W9xnwh7GsEPu65KTb5J9rTmQ9JjUc6WP0UisfxfRyLJcjn0kIsr2llH1nyWfJY9I3Q%3D%3D&xyip=219.132.164.174&xyct=15&xysc=1&sent_http_access-control-allow-credentials=true&sent_http_cdn-source=bdcloud&sent_http_cache=state&sent_http_access-control-allow-headers=DNT%2CX-CustomHeader%2CKeep-Alive%2CUser-Agent%2CX-Requested-With%2CIf-Modified-Since%2CCache-Control%2CContent-Type%2CRange&sent_http_cdn-user-ip=14.21.96.204&sent_http_cdn-ip=113.96.164.35&sent_http_access-control-allow-methods=GET%2CPOST%2COPTIONS&sent_http_access-control-allow-origin=*&sent_http_access-control-expose-headers=Content-Range%2C%20Last-Modified'
#     headers_ = {
#             'User-Agent': FakeUserAgent().random}
#     res=requests.get(url_,headers=headers_)
#     data_=res.content
#     with open('交换余生.mp4','wb') as f:
#         f.write(data_)

"""
VIP歌曲:无法发送请求,
VIP歌曲的MV却可以,,,,
MP4 > MP3
是可以以音频形式存在, 文件大小还是mp4的大小,比较占用磁盘空间
"""

# import requests
# from fake_useragent import FakeUserAgent
# if __name__ == '__main__':
#     url_='https://aabjrp3nk5hmo4e2kf26v3y7mmfla888.node.ppio.cloud:35672/fseeca82d4.a.bdydns.com/1924164272/cloudmusic/obj/core/4026923983/1765d168a505e8a29349ada6d039413c.mp4?wsSecret=13974682498de92db46f028084d2b151&wsTime=1626785228&http_cdnfrom=bdcloud&max_age=31104000&r=csLMxLOSlEBTC8LdFx2MzAZ5vxvlU2mip0JMw3pKvt5Ynwg5%2FrygXV5lofIBDRuMUsRIDzVZRM6dGMNG547khO0JeK99xPOct8YJzf%2BrYBSYMVMhlRRGKGXoS4DfFGvxYOfVn9U3MByn70qUzCQ7NufdEF3VGmTPWiVKGEQZTqEcgI6DJdZGO2plRkrZW2bQkOt5ah1JEdAuvrIoCSKeCw%3D%3D&sent_http_access-control-allow-headers=DNT%2CX-CustomHeader%2CKeep-Alive%2CUser-Agent%2CX-Requested-With%2CIf-Modified-Since%2CCache-Control%2CContent-Type%2CRange&sent_http_cdn-user-ip=183.30.178.167&sent_http_access-control-allow-credentials=true&sent_http_cdn-ip=113.96.164.35&sent_http_cache=state&sent_http_cdn-source=bdcloud&sent_http_access-control-allow-origin=*&sent_http_access-control-allow-methods=GET%2CPOST%2COPTIONS&sent_http_access-control-expose-headers=Content-Range%2C%20Last-Modified'
#     headers_ = {
#             'User-Agent': FakeUserAgent().random}
#     res=requests.get(url_,headers=headers_)
#     data_=res.content
#     with open('交换余生.mp3','wb') as f:
#         f.write(data_)

"""
抽离出来的音频文件,, 文件大小就比较小了
"""
import requests
from fake_useragent import FakeUserAgent
import os
import moviepy.editor as mp #导入 MoviePy
if __name__ == '__main__':
    # 1.确认目标的url
    url_ = 'https://apd-3b9aa9e35694605145342874ebf5d0f5.v.smtcdns.com/mv.music.tc.qq.com/AK2bc93_RfGYBI2c6yYrkmwVE50h5MstapyXBJ4U_LAs/8A2CC74C8EFD52DFF38D4D7F43FB8D978F5ACCA5C5BB649AFE9F6584818966994AB6E308F60095CEA3B80DA5ABED01DAZZqqmusic_default/1049_M0120100004c5g7g0JlomR1001934004.f9814.mp4?fname=1049_M0120100004c5g7g0JlomR1001934004.f9814.mp4'

    # 构造正常的用户代理
    headers_ = {
        'User-Agent':FakeUserAgent().random
    }

    # 2.发送网络请求
    response_ = requests.get(url_,headers=headers_)

    # 4.保存
    with open('年岁.mp4','wb') as f:
        f.write(response_.content)
    #把文件复制到项目文件夹中会使定义视频文件变得更容易。MoviePy中有一个叫VideoFileClip的方法
    my_clip = mp.VideoFileClip(r"年岁.mp4")
    # 用MoviePy库进行转换，将其音频转换为普遍的MP3格式，音频格式：MP3、AAC、WMA、AC3
    my_clip.audio.write_audiofile(r"年岁.mp3")













































