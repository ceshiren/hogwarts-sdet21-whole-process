"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import time

from selenium.webdriver.common.by import By

from utils.log_utils import logger
from web.page_object.base_page import BasePage
from web.page_object.new_calender import NewCalender


class Calender(BasePage):
    def create(self):
        self.find(By.CSS_SELECTOR, ".sidebar-more-trigger").click()
        self.find(By.CSS_SELECTOR, ".larkc-svg-icon.sidebar-more-popup-icon.icon-add").click()
        return NewCalender(self.driver)

    def get_my_calendars(self):
        time.sleep(3)
        calender_webelements = self.finds(By.CSS_SELECTOR, ".calendar-item")
        calendar_names = [ele.text for ele in calender_webelements]
        logger.info(f"我的日历列表为{calendar_names}")
        return calendar_names

    def get_calender(self, calender_name):
        """
        使用xpath 的文本定位的方式，去定位新添加的元素
        :return:
        """
        ele = self.find(By.XPATH, f"//*[text()='{calender_name}']")
        logger.info(f"寻找的日历的名称为{ele.text}")
        return ele.text