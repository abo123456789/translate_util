# -*- coding:utf-8 -*-
# @Author cc
# @TIME 2020/5/25 15:46

from translate_util.base_translate import BaseTranslate
from translate_util.common_request import send_request


class YoudaoTranslate(BaseTranslate):

    def trans_text_en2cn(self):
        """
        type 枚举值
        ZH_CN2EN 中文　»　英语
        ZH_CN2JA 中文　»　日语
        ZH_CN2KR 中文　»　韩语
        ZH_CN2FR 中文　»　法语
        ZH_CN2RU 中文　»　俄语
        ZH_CN2SP 中文　»　西语
        EN2ZH_CN 英语　»　中文
        JA2ZH_CN 日语　»　中文
        KR2ZH_CN 韩语　»　中文
        FR2ZH_CN 法语　»　中文
        RU2ZH_CN 俄语　»　中文
        SP2ZH_CN 西语　»　中文
        :param content: 
        :return: 
        """
        url = f'http://fanyi.youdao.com/translate?&doctype=json&from=AUTO&to=zh-CHS&i={self.content}'
        r = send_request('get', url, proxies=self.proxies)
        rs = []
        for result in r.json()['translateResult'][0]:
            rs.append(result['tgt'])
        return ''.join(rs)

    def trans_text_other2cn(self):
        return self.trans_text_en2cn()

    def trans_text_other2en(self):
        url = f'http://fanyi.youdao.com/translate?&doctype=json&from=AUTO&to=en&i={self.content}'
        r = send_request('get', url, )
        rs = []
        for result in r.json()['translateResult'][0]:
            rs.append(result['tgt'])
        return ''.join(rs)


if __name__ == '__main__':
    for source_text in ['china', '저는 중국사람입니다']:
        rs = YoudaoTranslate(content=source_text).trans_text_other2cn()
        print(rs)

    for source_text in ['中国', '저는 중국사람입니다']:
        res = YoudaoTranslate(content=source_text).trans_text_other2en()
        print(res)
