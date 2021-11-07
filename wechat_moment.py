import time


from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Wechat_Moment():
    def __init__(self):
        desired_caps = {
            'platformName': 'Android',
            'deviceName': '127.0.0.1:7555',
            'platformVersion': '6.0.1',
            'appPackage': 'com.tencent.mm',
            'appActivity': 'com.tencent.mm.ui.LauncherUI'
        }
        # 定义在朋友圈的时候滑动位置
        self.start_x = 300
        self.start_y = 800
        self.end_x = 300
        self.end_y = 300

        # 启动微信
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        # 设置等待
        self.wait = WebDriverWait(self.driver, 500)
        print('微信启动...')


    def login(self):
        # 获取到登录按钮后点击

        # login_btn = self.driver.find_element_by_id('com.tencent.mm:id/fam')
        login_btn=self.wait.until(EC.element_to_be_clickable((By.ID, "com.tencent.mm:id/fam")))
        login_btn.click()
        # 获取使用微信号登录按钮
        # change_login_btn = self.driver.find_element_by_id('com.tencent.mm:id/d5u')
        change_login_btn=self.wait.until(EC.element_to_be_clickable((By.ID, "com.tencent.mm:id/d5u")))
        change_login_btn.click()
        # 获取输入账号元素并输入
        # account = self.driver.find_element_by_class_name('android.widget.EditText')
        account =self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@resource-id="com.tencent.mm:id/d5j"]/android.widget.EditText')))
        account.send_keys("yanjiangua")
        # 获取密码元素并输入
        # password =self.driver.find_element_by_class_name('android.widget.EditText')
        password=self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@resource-id="com.tencent.mm:id/d62"]/android.widget.EditText')))
        password.send_keys("qwe8501667")

        # 登录
        login = self.wait.until(EC.element_to_be_clickable((By.ID, "com.tencent.mm:id/d5n")))
        login.click()

        # 点击权限申请
        know_btn=self.wait.until(EC.element_to_be_clickable((By.ID, "com.tencent.mm:id/doz")))
        know_btn.click()
        # 点击允许
        self.wait.until(EC.element_to_be_clickable((By.ID, "com.android.packageinstaller:id/permission_allow_button"))).click()
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable((By.ID, "com.android.packageinstaller:id/permission_allow_button"))).click()
        # 点击去掉通讯录提示框
        no_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "com.tencent.mm:id/doz")))
        no_btn.click()
        # 同意微信隐私
        self.wait.until(EC.element_to_be_clickable((By.ID, "weuiAgree"))).click()
        self.wait.until(EC.element_to_be_clickable((By.ID, "button"))).click()

        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'android.view.View'))).click()
        time.sleep(2)
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'android.view.View'))).click()
        print('登录成功...')


    def find_xiaoshuaib(self):
        # 获取到搜索按钮后点击
        search_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "com.tencent.mm:id/iq")))
        # 等搜索建立索引再点击
        time.sleep(10)
        search_btn.click()
        # 获取搜索框并输入
        search_input = self.wait.until(EC.presence_of_element_located((By.ID, "com.tencent.mm:id/kh")))
        search_input.send_keys("黄涛")
        print('搜索黄涛...')
        # 点击头像进入
        xiaoshuaib_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "com.tencent.mm:id/py")))
        xiaoshuaib_btn.click()
        # 点击右上角...进入
        menu_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "com.tencent.mm:id/jy")))
        menu_btn.click()
        # 再点击头像
        icon_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "com.tencent.mm:id/e0c")))
        icon_btn.click()
        # 点击朋友圈
        moment_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "com.tencent.mm:id/d86")))
        moment_btn.click()
        print('进入朋友圈...')

    def get_data(self):
        while True:
            # 获取 ListView
            items = self.wait.until(EC.presence_of_all_elements_located((By.ID, 'com.tencent.mm:id/eew')))
            # 滑动
            self.driver.swipe(self.start_x, self.start_y, self.end_x, self.end_y, 2000)
            #遍历获取每个List数据
            for item in items:
                moment_text = item.find_element_by_id('com.tencent.mm:id/kt').text
                day_text = item.find_element_by_id('com.tencent.mm:id/eke').text
                month_text = item.find_element_by_id('com.tencent.mm:id/ekf').text
                print('抓取到黄涛朋友圈数据： %s' % moment_text)
                print('抓取到黄涛发布时间： %s月%s' % (month_text, day_text))

if __name__ == '__main__':
    wc_moment = Wechat_Moment()
    wc_moment.login()
    wc_moment.find_xiaoshuaib()
    wc_moment.get_data()











