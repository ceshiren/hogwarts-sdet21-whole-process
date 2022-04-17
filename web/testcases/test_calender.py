"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from web.page_object.feishu_page import FeishuPage


class TestCalender:
    def setup_class(self):
        self.feishu = FeishuPage()

    def test_new_celender(self):
        res = self.feishu.goto_calender().\
            create().\
            new_calender("测开21期")\
            .get_calender("测开21期")
        assert "测开21期" == res

    def teardown_class(self):
        self.feishu.driver.close()