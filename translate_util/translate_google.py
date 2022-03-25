# -*- coding:utf-8 -*-
# @Author cc
# @TIME 2020/5/25 16:02

from translate_util.base_translate import BaseTranslate
from translate_util.common_request import send_request


class GoogleTranslate(BaseTranslate):
    def trans_text_en2cn(self):
        url = f'http://translate.google.cn/translate_a/single?client=gtx&dt=t&dj=1&ie=UTF-8&sl=auto&tl=zh&q={self.content}'
        r = send_request('get', url, proxies=self.proxies)
        # self.logger.info(r.text)
        rs = []
        for result in r.json()['sentences']:
            rs.append(result['trans'])
        return ''.join(rs)

    def trans_text_other2cn(self):
        return self.trans_text_en2cn()

    def trans_text_other2en(self):
        url = f'http://translate.google.cn/translate_a/single?client=gtx&dt=t&dj=1&ie=UTF-8&sl=auto&tl=en&q={self.content}'
        r = send_request('get', url, proxies=self.proxies)
        # self.logger.info(r.text)
        rs = []
        for result in r.json()['sentences']:
            rs.append(result['trans'])
        return ''.join(rs)


if __name__ == '__main__':
    for source_text in ['china', '저는 중국사람입니다']:
        _rs = GoogleTranslate(content=source_text).trans_text_other2cn()
        print(_rs)
    for source_text in ['中国', '저는 중국사람입니다']:
        res = GoogleTranslate(content=source_text).trans_text_other2en()
        print(res)
