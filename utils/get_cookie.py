"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import time

import yaml
from selenium import webdriver


class TestCookieLogin:
    def setup_class(self):
        self.drvier = webdriver.Chrome()
    def teardown(self):
        self.drvier.quit()

    def test_get_cookies(self):
        # 1. 访问企业微信主页/登录页面
        self.drvier.get("https://www.feishu.cn/")
        # 2. 等待20s，人工扫码操作
        time.sleep(20)
        # 3. 等成功登陆之后，再去获取cookie信息
        cookie = self.drvier.get_cookies()
        # 4. 将cookie存入一个可持久存储的地方，文件
        # 打开文件的时候添加写入权限
        with open("../config/cookie.yaml", "w") as f:
            # 第一个参数是要写入的数据
            yaml.safe_dump(cookie, f)

