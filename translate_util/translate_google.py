# -*- coding:utf-8 -*-
# @Author cc
# @TIME 2020/5/25 16:02
import re

import requests

from translate_util.base_translate import BaseTranslate


class GoogleTranslate(BaseTranslate):

    def trans_text_other2cn(self):
        return self.trans_text(self.content, tl='zh-CN')

    def trans_text_other2en(self):
        return self.trans_text(self.content, tl='en')

    def trans_text(self, st: [str, bytes], sl='auto', tl='zh-CN') -> str:
        """
        将字符串翻译成指定国家语言
        :param st: 待翻译的字符串
        :param sl: 待翻译的语言 默认auto
        :param tl: 翻译成的语言
        :return: 翻译后的字符串
        """
        url = "https://www.google.com.hk/async/translate"

        payload = f"async=translate,sl:{sl},tl:{tl},st:{st.encode('utf-8')},id:1672056488960,qc:true,ac:true,_id:tw-async-translate,_pms:s,_fmt:pc"
        headers = {
            'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
            'DNT': '1',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
            'sec-ch-ua-arch': '"x86"',
            'sec-ch-ua-full-version': '"108.0.5359.125"',
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-ch-ua-full-version-list': '"Not?A_Brand";v="8.0.0.0", "Chromium";v="108.0.5359.125", "Google Chrome";v="108.0.5359.125"',
            'sec-ch-ua-bitness': '"64"',
            'sec-ch-ua-model': '',
            'sec-ch-ua-wow64': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'Accept': '*/*',
            'X-Client-Data': 'CKW1yQEIhbbJAQiktskBCMS2yQEIqZ3KAQjb08oBCLD+ygEIlaHLAQjv8swBCN75zAEI5PrMAQjxgM0BCLKCzQEI7ILNAQjIhM0BCO+EzQEIt4XNAQ==',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'host': 'www.google.com.hk',
            'Cookie': '1P_JAR=2022-12-26-12; NID=511=eVLI1bG9nhyOZtqU14JBHm5Be00epdxfR4XmfQeehYyIkzgpXi6dbpNY75ZMVyS7aOjoM2oZ5WdoR8eNq6wi1-e_J0NeoyI0dtsHW-_8Ik4PGrqvuGHdcvVC03zTOEK2TY1FZL85Wimo_ZPIE3hGIrmGPSiel6-rRRW9lD30UPs'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        res_text = response.content.decode()
        print(res_text)
        res_array = re.findall(r'id="tw-answ-target-text">(.*?)</span>', res_text,
                               flags=re.IGNORECASE)
        return res_array[0]


if __name__ == '__main__':
    for source_text in ['china', 'je suis un']:
        _rs = GoogleTranslate(content=source_text).trans_text_other2cn()
        print(_rs)
    for source_text in ['31 maggio 2021', '中国']:
        res = GoogleTranslate(content=source_text).trans_text_other2en()
        print(res)
