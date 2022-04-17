"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import time

from selenium import webdriver

from utils.file_tools import FileTool
from utils.log_utils import logger


class BasePage:
    _BASE_URL=""
    def __init__(self, base_driver=None):
        """
        1. 打开浏览器
        2. 输入被测网址
        :param base_driver:
        """

        # 避免driver 的重复实例化
        if base_driver:
            self.driver = base_driver
        else:
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(3)
        if self._BASE_URL:
            # 如果baseURl 存在的话就打开
            self.driver.get(self._BASE_URL)
            # 通过cookie登录
            self.__login_by_cookie()

    def __login_by_cookie(self):
        cookies = FileTool.read_yaml("cookie")
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        time.sleep(2)
        self.driver.refresh()

    def find(self, by, locator=None):
        if locator:
            logger.debug(f"元素定位为：{by}-{locator}")
            return self.driver.find_element(by, locator)
        else:
            logger.debug(f"元素定位为：{by}")
            return self.driver.find_element(*by)


    def finds(self, by, locator=None):
        if locator:
            logger.debug(f"元素定位为：{by}-{locator}")
            return self.driver.find_elements(by, locator)
        else:
            logger.debug(f"元素定位为：{by}")
            return self.driver.find_elements(*by)
