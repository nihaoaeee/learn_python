# from splinter.browser import Browser
from time import sleep
import traceback

import requests
from splinter import Browser


# from splinter.driver.webdriver.firefox import WebDriver as FirefoxWebDriver


class Buy_Tickets(object):
    # 定义实例属性，初始化
    def __init__(self, username, passwd, order, passengers, dtime, starts, ends):
        self.driver = None
        self.username = username
        self.passwd = passwd
        # 车次，0代表所有车次，依次从上到下，1代表所有车次，依次类推
        self.order = order
        # 乘客名
        self.passengers = passengers
        # 起始地和终点
        self.starts = starts
        self.ends = ends
        # 日期
        self.dtime = dtime
        # self.xb = xb
        # self.pz = pz
        # self.login_url = 'https://kyfw.12306.cn/otn/login/userLogin'
        self.login_url = 'https://kyfw.12306.cn/otn/resources/login.html'
        self.initMy_url = 'https://kyfw.12306.cn/otn/view/index.html'
        self.ticket_url = 'https://kyfw.12306.cn/otn/leftTicket/init'
        self.driver_name = 'firefox'
        self.executable_path = 'C:\Program Files\Mozilla Firefox\firefox.exe'

    # 登录功能实现
    def login(self):
        self.driver.visit(self.login_url)
        self.driver.find_by_id('J-userName').fill(self.username)
        self.driver.find_by_id('J-password').fill(self.passwd)
        self.driver.find_by_id('J-login').click()
        sleep(1)
        print('请输入验证码...')
        while True:
            if self.driver.url == self.initMy_url:
                break
            else:
                sleep(2)

    # 买票功能实现
    def start_buy(self):
        self.driver = Browser()
        # 窗口大小的操作
        self.driver.driver.set_window_size(700, 500)
        self.login()
        # self.driver.visit(self.ticket_url)
        # try:
        #     print('开始购票...')
        #     # 加载查询信息
        #     self.driver.cookies.add({"_jc_save_fromStation": self.starts})
        #     self.driver.cookies.add({"_jc_save_toStation": self.ends})
        #     self.driver.cookies.add({"_jc_save_fromDate": self.dtime})
        #     self.driver.reload()
        #     count = 0
        #     if self.order != 0:
        #         while self.driver.url == self.ticket_url:
        #             self.driver.find_by_text('查询').click()
        #             count += 1
        #             print('第%d次点击查询...' % count)
        #             try:
        #                 self.driver.find_by_text('预订')[self.order - 1].click()
        #                 sleep(1.5)
        #             except Exception as e:
        #                 print(e)
        #                 print('预订失败...')
        #                 continue
        #     else:
        #         while self.driver.url == self.ticket_url:
        #             self.driver.find_by_text('查询').click()
        #             count += 1
        #             print('第%d次点击查询...' % count)
        #             try:
        #                 for i in self.driver.find_by_text('预订'):
        #                     i.click()
        #                     sleep(1)
        #             except Exception as e:
        #                 print(e)
        #                 print('预订失败...')
        #                 continue
        #     print('开始预订...')
        #     sleep(1)
        #     print('开始选择用户...')
        #     for p in self.passengers:
        #
        #         self.driver.find_by_text(p).last.click()
        #         sleep(0.5)
        #         if p[-1] == ')':
        #             self.driver.find_by_id('dialog_xsertcj_ok').click()
        #     print('提交订单...')
        #     # sleep(1)
        #     # self.driver.find_by_text(self.pz).click()
        #     # sleep(1)
        #     # self.driver.find_by_text(self.xb).click()
        #     # sleep(1)
        #     self.driver.find_by_id('submitOrder_id').click()
        #     sleep(2)
        #     print('确认选座...')
        #     self.driver.find_by_id('qr_submit_id').click()
        #     print('预订成功...')
        # except Exception as e:
        #     print(e)


if __name__ == '__main__':
    # 用户名
    username = 'LIGUOXI'
    # 密码
    password = 'QAZ123'
    # 车次选择，0代表所有车次
    order = 2
    # 乘客名，比如passengers = ['丁小红', '丁小明']
    # 学生票需注明，注明方式为：passengers = ['丁小红(学生)', '丁小明']
    passengers = ['丁彦军']
    # 日期，格式为：'2018-01-20'
    dtime = '2018-01-19'
    # 出发地(需填写cookie值)
    starts = '%u5434%u5821%2CWUY'  # 吴堡
    # 目的地(需填写cookie值)
    ends = '%u897F%u5B89%2CXAY'  # 西安

    # xb =['硬座座']
    # pz=['成人票']

    Buy_Tickets(username, password, order, passengers, dtime, starts, ends).start_buy()
    # cj = browser_cookie3.firefox()
    # get_key_url = "https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=%E5%8C%97%E4%BA%AC,BJP&ts=%E8%A1%A1%E6%B0%B4,HSP&date=2023-09-21&flag=N,N,Y"
    # r_ = requests.get(get_key_url, cookies=cj)
    # print(r_)
