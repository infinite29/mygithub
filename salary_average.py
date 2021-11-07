#! /usr/bin/env python
# -*- coding: utf-8 -*-
#@author：严健华
#@time：2021/10/5-11:59
#@email：yanjianhua29@163.com
import time
import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook


class JobSpider:
    # 初始化方法
    def __init__(self):
        self.search_key = input('输入你搜索的职位：')
        self.session = requests.Session()
        self.headers = {
          'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
          'cookie': '__uuid=1633406048070.86; __tlog=1633406048404.48%7C00000000%7C00000000%7C00000000%7C00000000; __s_bid=e223eda1fc0581103b871cc2976733c85a74; user_roles=0; need_bind_tel=false; acw_tc=3ccdc16816334066669975834e1df92b2cf19f61a2e6d0488ea1be3655d413; fe_se=-1633406668386; Hm_lvt_a2647413544f5a04f00da7eee0d5e200=1633406048,1633406708; imApp_0=1; UniqueKey=886697128d4044521a667e00ad0d9493; lt_auth=s%2BkOPnwGyg3x7SXRjDNdtq5K2t37WT3J8XwM0B1WgoDqXPy24PfhRwqOqbQExAMhxEx9c8ULN7P9%0D%0AMej4wXNM60MXwGmul4Cxufik0H4HUeVgIsW2vezHg%2FXSQp4ilEAC8nJbpEIL%2BQ%3D%3D%0D%0A; user_photo=5f8fa3a679c7cc70efbf444e08u.png; user_name=%E4%B8%A5%E5%81%A5%E5%8D%8E; new_user=false; c_flag=4e542dfdb971c2e2043399978efaa491; inited_user=92f679cff84a24209c8b51e2f0bf75ee; JSESSIONID=F514BE34C51131946FC1E94B08417AE2; Hm_lpvt_a2647413544f5a04f00da7eee0d5e200=1633406807; __session_seq=8; __uv_seq=8; imClientId=1a4a1311351ea266a423b1a082f29d34; imId=1a4a1311351ea2664f703fb47c2e479d; imClientId_0=1a4a1311351ea266a423b1a082f29d34; imId_0=1a4a1311351ea2664f703fb47c2e479d; fe_im_socketSequence_new_0=2_2_2; fe_im_connectJson_0=%7B%220_886697128d4044521a667e00ad0d9493%22%3A%7B%22socketConnect%22%3A%220%22%2C%22connectDomain%22%3A%22liepin.com%22%7D%7D',
        }
        self.session.headers.update(self.headers)

    # 获取数据方法
    def get_data(self):

        data = []
        for i in range(2):  # 获取2页数据
            params_ = {
                    "key": self.search_key,  # 搜索关键字
                    # "key": '数据分析',  # 搜索关键字
                    # "d_sfrom": "search_prime",
                    # "ckId": "ec63c9bb647d9895223ea11d322fc6fd",# 深圳地区
                    "ckId": "2c40e1636772a3d72c81b39a79f3666b",# 广州地区
                    "headId": "60f49f200e9ff00cec3fe6c153b69910",
                    # "headId": "60f49f200e9ff00cec3fe6c153b69910",
                    # "d_pageSize": "40",  # 每页数据条数
                    # "dq": "050090",  # 深圳地区
                    "dq": "050020",  # 广州地区
                    "currentPage": str(i)  # 当前页页码数
                  }
            # res = self.session.get('https://www.liepin.com/zhaopin/', params=params_)
            # res = self.session.get('https://www.liepin.com/zhaopin/?headId=a3e65363a9947d0f20ee3adea6b56cb2&dq=050090', params=params_) # 深圳地区职位
            res = self.session.get('https://www.liepin.com/zhaopin/?headId=a3e65363a9947d0f20ee3adea6b56cb2&dq=050020', params=params_) # 广州地区职位
            if res.status_code == 200:
                print('第{}页数据获取成功'.format(i + 1))
                soup = BeautifulSoup(res.text, 'html.parser')
                # print(soup)
                job_items = soup.find_all('div', class_='job-list-item')
                # print(job_items)
                # print(type(job_items))
                for item in job_items:
                    # print(item)
                    job_info = item.find('div', class_='job-card-left-box')
                    conditions = job_info.find('div', class_='job-detail-box') #获取该职位的基本信息
                    # print(conditions)
                    job_url=conditions.find('a')['href'] # 获取该职位的详情页URL
                    # print(job_url)
                    job_res = self.session.get(job_url)
                    soup1 = BeautifulSoup(job_res.text, 'html.parser')
                    job_profile=soup1.find('dl', class_='paragraph').text
                    job_profile=job_profile.replace('职位介绍','') # 去掉职位介绍
                    # print(job_profile)
                    job_title=conditions.find('div', class_='ellipsis-1')['title'] #职位名称
                    salary = conditions.find('span', class_='job-salary').text  # 薪资范围
                    area = conditions.find('span', class_='ellipsis-1').text # 地区
                    working_exp = conditions.find_all('span', class_='labels-tag')[0].text  # 经验要求
                    edu_level= conditions.find_all('span', class_='labels-tag')[1].text  # 学历要求
                    company_name=conditions.find('span', class_='company-name ellipsis-1').text # 公司名
                    company_type=conditions.find('div', class_='company-tags-box ellipsis-1').text # 公司类型
                    # 用字典存储每条招聘信息
                    result = {
                    'job_name': job_title,
                    'salary': salary,
                    'area': area,
                    'edu_level': edu_level,
                    'working_exp': working_exp,
                    'company_name': company_name,
                    'company_type': company_type,
                    'job_profile':job_profile
                    }
                    # 将每条招聘信息存到列表中
                    data.append(result)
            else:
                print('第{}页数据获取失败'.format(i + 1))
                time.sleep(1)
        return data
    # 处理数据方法
    def process_data(self):
        data = self.get_data()
        total = 0
        count = 0
        rows = [['公司名', '公司类型', '地区', '职位', '薪资', '平均年薪', '学历要求', '经验要求','职位介绍']]
        for item in data:
            company_name = item['company_name']
            company_type = item['company_type']
            # company_type = None
            area = item['area']
            job_name = item['job_name']
            salary = item['salary']
            edu_level = item['edu_level']
            working_exp = item['working_exp']
            job_profile=item['job_profile']

            if salary != '面议':
                if '薪' in salary:
                    salary_range, salary_times_str = salary.split(
                        'k·')  # 分割成两部分
                    salary_times = int(salary_times_str.strip('薪'))  # 一年发多少薪
                else:
                    salary_range = salary.strip('k')
                    salary_times = 12

                if '-' in salary_range:
                    salary_min_str, salary_max_str = salary_range.split(
                        '-')  # 分割薪资范围
                    salary_min = int(salary_min_str) * 1000  # 最低月薪
                    salary_max = int(salary_max_str) * 1000  # 最高月薪
                    salary_value = (salary_min + salary_max) / 2  # 平均月薪
                else:
                    salary_value = int(salary_range) * 1000  # 给定月薪

                salary_avg = salary_value * salary_times  # 计算平均年薪
                total += salary_avg
                count += 1
            else:
                salary_avg = '面议'
            # 按公司名，公司类型，地区，职位，薪资，平均年薪，学历要求，经验要求,职位介绍排列
            row = [company_name, company_type, area, job_name, salary, salary_avg, edu_level, working_exp,job_profile]
            rows.append(row)

        print(f'{self.search_key} 的平均年薪是{total / count}元')
        return rows

    def save_data(self):
        # 处理后的数据
        rows = self.process_data()
        # 新建工作簿
        wb = Workbook()
        # 选择默认的工作表
        sheet = wb.active
        # 给工作表重命名
        sheet.title = 'python职位信息'
        # 将数据一行一行写入
        for row in rows:
            sheet.append(row)

        # 保存文件
        wb.save(f'猎聘{self.search_key}职位信息表1-广州.xlsx')

spider = JobSpider()
# spider.get_data()
spider.save_data()


