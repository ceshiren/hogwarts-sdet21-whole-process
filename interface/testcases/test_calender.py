"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from jsonpath import jsonpath

from interface.bu.Calender import Calender


class TestCalender():
    def setup_class(self):
        self.calender = Calender()

    def test_create(self):
        create_calender = self.calender.create("测试21期111111")
        calender_id = create_calender['data']['calendar']['calendar_id']
        r = self.calender.get(calender_id)
        res = jsonpath(r, "$..summary")
        assert "测试21期111111" == res[0]
