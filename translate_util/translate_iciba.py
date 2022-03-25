# -*- coding:utf-8 -*-
# @Author cc
# @TIME 2020/5/25 15:29

from requests import Session

from translate_util.base_translate import BaseTranslate


class IcibaTranslate(BaseTranslate):
    s = Session()
    url = 'http://fy.iciba.com/ajax.php'

    def trans_text_en2cn(self):
        params = {
            'a': 'fy',
            'f': 'auto',
            't': 'zh-CN',
            'w': self.content
        }
        r = self.s.request('get', self.url, params=params, )
        # self.logger.info(r.text)
        rs = r.json()['content'].get('out') if r.json()['content'].get('out') else r.json()['content'].get('word_mean')
        return rs[0].replace('n. ', '').replace(';', '') if isinstance(rs, list) else rs

    def trans_text_other2cn(self):
        return self.trans_text_en2cn()

    def trans_text_other2en(self):
        params = {
            'a': 'fy',
            'f': 'auto',
            't': 'en',
            'w': self.content
        }
        r = self.s.request('get', self.url, params=params, )
        # self.logger.info(r.text)
        rs = r.json()['content'].get('out') if r.json()['content'].get('out') else r.json()['content'].get('word_mean')
        return rs[0].replace('n. ', '').replace(';', '') if isinstance(rs, list) else rs


if __name__ == '__main__':
    for source_text in ['china', '저는 중국사람입니다']:
        _rs = IcibaTranslate(content=source_text).trans_text_other2cn()
        print(_rs)
    for source_text in ['中国', '저는 중국사람입니다']:
        res = IcibaTranslate(content=source_text).trans_text_other2en()
        print(res)
