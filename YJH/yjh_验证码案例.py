"""
1.进入官网: https://www.12306.cn/index/
2.点击登录
3.点击账号登录
4.账号密码的填写(忽悠)
5.验证码的点击:
    简单逻辑:
        -- 把这个验证码图片发送给超级鹰后台
        -- 返回给我们结果的坐标
        -- 根据坐标进行点击(ActionChains进行点击)

6.到了拥有验证码图片的登录页面
7.进行网页截图                           不能: 验证码的url,,,发送请求,,去获取,,(不能够去对验证码图片url进行请求,,刷新)
8.页面截图是整张, 抠图,得到对应的验证码图片,
    -- 得到验证码图片的坐标,,进行抠图
    -- 抠图需要先拿到坐标范围(左上角的坐标,右下角的坐标)
    -- from PIL import Image 进行范围截图
    -- 拿到了验证码图片
9.把图片交给超级鹰,得到对应的结果坐标
10.验证码类型9004: 返回1-4个坐标结果

11.通过结果里面是否有 "|" 字符 判断 是单个坐标 多个坐标
单个坐标: 33,129
多个坐标: 33,129 | 44,124 :[[33,129],[44,124]]


"""
import time
from selenium.webdriver import Chrome, ActionChains
# 图片的裁剪
from PIL import Image
import requests
from hashlib import md5
from selenium.webdriver import ChromeOptions

class Chaojiying_Client(object):

    def __init__(self, username, password, soft_id):
        self.username = username
        password = password.encode('utf8')
        self.password = md5(password).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }

    def PostPic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files,
                          headers=self.headers)
        return r.json()

    def ReportError(self, im_id):
        """
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()




if __name__ == '__main__':
    # 创建浏览器对象
    options_ = ChromeOptions()
    # 添加参数,进行隐藏
    options_.add_experimental_option('excludeSwitches', ["enable-automation"])  # 不需要死记硬背

    chrome_obj = Chrome(options=options_)

    # 进入官网
    chrome_obj.get('https://www.12306.cn/index/')

    # 浏览器最大化
    chrome_obj.maximize_window()
    time.sleep(2)
    # 登记登录,进入登录页面
    chrome_obj.find_element_by_xpath('//*[@id="J-header-login"]/a[1]').click()  # 进行点击
    time.sleep(0.5)
    # 点击账号登录的页面,,当前页面,就有了验证码..
    chrome_obj.find_element_by_xpath('/html/body/div[2]/div[2]/ul/li[2]/a').click()
    time.sleep(1)
    #输入用户名及密码
    user_obj=chrome_obj.find_element_by_xpath('//*[@id="J-userName"]')
    user_obj.send_keys('13237195262')
    time.sleep(1)
    pwd_obj=chrome_obj.find_element_by_xpath('//*[@id="J-password"]')
    pwd_obj.send_keys('qwe8501667')
    # 页面截图:格式png
    chrome_obj.save_screenshot('login.png')
    # 页面截图是整张, 抠图,得到对应的验证码图片,左上角, 右下角的坐标
    code_obj = chrome_obj.find_element_by_xpath('//*[@id="J-loginImg"]')
    location_ = code_obj.location
    print('验证码图片的坐标是:', location_)

    # 得到验证码图片的长和宽,相加得到右下角坐标,确认截图(抠图)范围
    size_ = code_obj.size
    print('验证码的尺寸:', size_)  # 高+y height 188 宽+x width300

    # 确认图片的坐标范围(左上角的坐标x,y,右下角的坐标x+width,y+height)
    # img_range = (2.5 * int(location_['x']), 2.5 * int(location_['y']), 2.5 * (int(location_['x'] + size_['width'])),
    #              2.5 * (int(location_['y'] + size_['height']))) #2.5为分辨率缩放比例
    img_range = (int(location_['x']), int(location_['y']), (int(location_['x'] + size_['width'])),
                 (int(location_['y'] + size_['height'])))

    # 图片的裁剪 from PIL import Image
    img_obj = Image.open('login.png')  # 参数是要被裁剪的完整的图片

    # 进行裁剪
    res_ = img_obj.crop(img_range)  # 参数是坐标范围

    # 保存结果: 格式使用png
    res_.save('12306.png')

    # 把验证码图片交给打码平台
    chaojiying = Chaojiying_Client('yanjianhua', 'qwe8501667', '921347')  # 用户中心>>软件ID 生成一个替换 96001
    im = open('12306.png', 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    print('结果坐标:', chaojiying.PostPic(im, 9004)['pic_str'])  # 1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()
    str_ = chaojiying.PostPic(im, 9004)['pic_str']
    # str_='99,82|124,138'
    # 进行判断
    list_a = []  # 保存最终的坐标结果 "33,129 | 44,124" >  [[33,129],[44,124]]
    if "|" in str_:
        """多个坐标"""
        res_ = str_.split("|")
        for i in res_:
            list_ = []
            demo_ = i.split(',')
            list_.append(demo_[0])
            list_.append(demo_[1])
            list_a.append(list_)
    else:
        """单个坐标"""
        res_ = str_.split(',')
        list_ = []
        list_.append(res_[0])
        list_.append(res_[1])
        list_a.append(list_)
    print('坐标列表:', list_a)
    # 根据坐标,进行点击,[['181', '154']] x坐标, y的坐标 [['263', '140'], ['265', '86']]
    for i in list_a:  # 坐标结果是字符串,需要进行整型转换
        # x_ = int(int(i[0])/2.5)
        # y_ = int(int(i[1])/2.5)
        x_ = int(i[0])
        y_ = int(i[1])
        # 进行精确点击,得到的坐标结果是以验证码为准,,需要手动更换参照对象
        action_ = ActionChains(chrome_obj)
        #        更改(移动)(验证码节点(左上角)为基准x=0,y=0)    点击      实现
        action_.move_to_element_with_offset(code_obj, x_, y_).click().perform()
        time.sleep(0.3)  # 正常行为的等待
    # 点击立即登录按钮
    chrome_obj.find_element_by_xpath('//*[@id="J-login"]').click()
    time.sleep(1.5)
    # 滑动验证码的点击
    # 1.找到这个按钮
    click_obj = chrome_obj.find_element_by_xpath('//*[@id="nc_1__scale_text"]/span')
    # 第一次：//*[@id="nc_1__scale_text"]/span
    # 第二次：//*[@id="nc_1__scale_text"]/span
    # 2.按住:动作(需要使用动作链)
    action_obj = ActionChains(chrome_obj)  # 参数是浏览器对象,
    action_obj.click_and_hold(click_obj)  # 点击并且按住,参数为具体的节点(按钮)

    # 3.滑动(x横向移动,y竖向移动) 在这之前可以得到他的长和宽
    action_obj.move_by_offset(300, 0).perform()
    #            定位                 #  启动

    # 4.松开点击
    action_obj.release()  # 释放
