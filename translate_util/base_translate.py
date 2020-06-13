# -*- coding:utf-8 -*-
# @Author cc
# @TIME 2020/5/25 16:25
import abc
from loguru import logger


class BaseTranslate(metaclass=abc.ABCMeta):
    def __init__(self, content: str, proxies: str = None):
        """
        :param content: 带翻译的内容
        :param proxies: 代理IP(5.34.178.48:8080)
        """
        self.content = content
        self.proxies = proxies
        self.logger = logger

    def trans_text_en2cn(self):
        pass

    def trans_text_other2cn(self):
        pass

    def trans_text_other2en(self):
        pass
