"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import os

import yaml


class FileTool:

    @classmethod
    def get_interface_dir(cls):
        # 获取api_object的文件夹路径
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    @classmethod
    def read_yaml(cls, file_name):
        # 获取api_object的文件夹路径
        _path = cls.get_interface_dir()
        # 拼接yaml文件所在的绝对路径 sep 相当于 win的 \ linux的/ sep.join 需要的参数是一个列表
        yaml_file = os.sep.join([_path, "config", file_name + ".yaml"])
        # 打开 yaml文件 并使用yaml.safe_load 将内容返回出去
        with open(yaml_file, encoding="utf-8") as f:
            return yaml.safe_load(f)


if __name__ == '__main__':
    # print(FileTool.read_yaml("corp_info"))
    print(__file__)
    print(__name__)