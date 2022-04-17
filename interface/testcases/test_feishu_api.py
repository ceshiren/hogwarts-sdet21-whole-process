"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from interface.bu.feishu_api import FeishuApi


def test_get_token():
    feishu = FeishuApi()
    feishu.get_token()