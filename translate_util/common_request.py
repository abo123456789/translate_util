# -*- coding: utf-8 -*-
# @Time    : 2020/6/12 23:04
# @Author  : CC
# @Desc    : common_request.py
import requests
from retrying import retry


def send_request(method, url, headers=None, params=None, data=None, proxies=None, timeout=10, max_attempt_number=3):
    if isinstance(proxies, str):
        proxies = {"https": proxies, "http": proxies}

    @retry(stop_max_attempt_number=max_attempt_number)
    def _send_request():
        response = requests.request(method, url, headers=headers, params=params, data=data, proxies=proxies,
                                    timeout=timeout)
        return response

    return _send_request()


if __name__ == '__main__':
    res = send_request("get", "https://www.baidu.com/")
    print(res.status_code)
