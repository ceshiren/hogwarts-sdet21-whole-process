"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
# 飞书api，代表一些和具体业务产品使用的全局的接口信息，比如token
from protocol.http_protocol import HttpProtocol
from utils.file_tools import FileTool


class FeishuApi:

    def __init__(self):
        # 返回一个标准的dict结构
        env_data = FileTool.read_yaml("env")
        default_env = env_data["default"]
        # 获取到配置文件中的基地址
        self.base_url = env_data[default_env]

    def feishu_req(self, method, url , **kwargs):
        """
        一些与飞书产品强相关，但是和具体业务逻辑五官的封装
        :return:
        """
        # **kwargs 代表接口的不定长参数，比如headers

        if kwargs.get("headers"):
        # 如果传递过来的请求有头信息，那么我们就在头信息中做追加
        #     headers:{"user-agent": "phone"}
            kwargs["headers"]["Authorization"] = f"Bearer {self.get_token()}"
        else:
            # 如果传递过来的请求没有header
            kwargs["headers"] = {"Authorization": f"Bearer {self.get_token()}"}
        # 传递塞入headers 的请求信息
        r = HttpProtocol.request(method, self.base_url+url, **kwargs)
        return r




    def get_token(self):
        url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
        body_data = {
            "app_id": "cli_a16851154ab8100d",
            "app_secret": "gKcy0rkIVl7gV4AY5itwRrcNkVzlURp6"
        }
        r = HttpProtocol.request("post", url, json=body_data)
        token = r.get("tenant_access_token")
        return token
