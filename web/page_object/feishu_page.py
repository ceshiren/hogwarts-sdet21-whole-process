"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from selenium.webdriver.common.by import By

from web.page_object.base_page import BasePage
from web.page_object.calender import Calender


class FeishuPage(BasePage):
    _BASE_URL = "https://www.feishu.cn/"
    def goto_calender(self):
        self.find(By.CSS_SELECTOR, ".headerExtra_productList").click()
        self.find(By.CSS_SELECTOR, "[title='日历']").click()
        # self.driver.window_handles 代表当前所有窗口 [-1] 代表最新的一个窗口
        # 切换到当前最新的窗口上面
        self.driver.switch_to.window(self.driver.window_handles[-1])
        return Calender(self.driver)
