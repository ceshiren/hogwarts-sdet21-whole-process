"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import requests

from utils.log_utils import logger


class HttpProtocol:

    @classmethod
    def request(self, method, url, **kwargs):
        logger.debug(f"请求的参数为{method}，url为{url}， 其他参数为{kwargs}")
        r = requests.request(method=method, url=url, **kwargs)
        # 如果响应结果确定都是json，那么可以直接返回r.json()
        logger.info(f"接口的响应内容为{r.json()}")
        return r.json()
