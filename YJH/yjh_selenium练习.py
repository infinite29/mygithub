import time
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ChromeOptions
# if __name__ == '__main__':
#     chrome_obj=Chrome()
#     # time.sleep(1.5)
#     chrome_obj.get('https://www.hao123.com/?tn=88093251_83_hao_pg')
    # data_=chrome_obj.page_source
    # # print(data_)
    # with open('hao123.html','w',encoding='utf-8') as f:
    #     f.write(data_)
    # chrome_obj.maximize_window()
    # chrome_obj.save_screenshot('hao123.png')
    # time.sleep(1.5)
    # chrome_obj.back()
    # time.sleep(1.5)
    # chrome_obj.forward()
    # chrome_obj.execute_script('window.open("https://www.bilibili.com/")')
    # windows_=chrome_obj.window_handles
    # print(windows_)
    # time.sleep(1.5)
    # chrome_obj.switch_to_window(windows_[0])
    # time.sleep(1.5)
    # chrome_obj.switch_to_window(windows_[1])
    # time.sleep(1.5)
    # chrome_obj.close()
    # time.sleep(1.5)
    # chrome_obj.quit()

#无头界面
# if __name__ == '__main__':
#     options_=Options()
#     # 设置无头界面
#     # 第一种
#     # options_.add_argument('--headless')
#     # 第二种
#     # options_.headless=True
#     # 第三种
#     options_.set_headless()
#     chrome_obj=Chrome(options=options_)
#     chrome_obj.get('https://www.hao123.com/?tn=88093251_83_hao_pg')
#     data_=chrome_obj.page_source
#     print(data_)

#反检测
# if __name__ == '__main__':
#     # 创建选项对象
#     options_=ChromeOptions()
#     # 添加参数，进行隐藏
#     options_.add_experimental_option('excludeSwitches',['enable-automation'])
#     chrome_obj=Chrome(options=options_)
#     chrome_obj.get('https://www.hao123.com/?tn=88093251_83_hao_pg')
#     data_=chrome_obj.page_source
#     print(data_)

#元素定位

if __name__ == '__main__':
    #创建浏览器对象
    chrome_obj=Chrome()
    #进入hao123主页
    chrome_obj.get('https://www.hao123.com/?tn=88093251_83_hao_pg')
    #定位到搜索对象
    input_obj=chrome_obj.find_element_by_xpath('//*[@id="search"]/form/div[2]/input')
    #发送关键字
    input_obj.send_keys('B站')
    #点击百度一下按钮
    click_obj=chrome_obj.find_element_by_xpath('//*[@id="search"]/form/div[3]/input')
    click_obj.click()
























































