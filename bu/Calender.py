"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from bu.feishu_api import FeishuApi
from protocol.http_protocol import HttpProtocol


class Calender(FeishuApi):
    def create(self, summary="测开21期测试", description="测开21期测试", permissions="private",
               color=-1, summary_alias="测开21期"):
        url = "calendar/v4/calendars"
        calender_data = {
            "summary": summary,
            "description": description,
            "permissions": permissions,
            "color": color,
            "summary_alias": summary_alias}
        r = self.feishu_req("POST", url, json=calender_data)
        return r

    def delete(self):
        pass

    def get(self, calendar_id):
        url = f"calendar/v4/calendars/{calendar_id}"
        r = self.feishu_req("get", url)
        return r

    def update(self):
        pass