# -*- coding:utf-8 -*-
# @Author cc
# @TIME 2020/5/21 12:24
import execjs
import requests
import re

from loguru import logger

from translate_util.base_translate import BaseTranslate

JS_CODE = """
function a(r, o) {
    for (var t = 0; t < o.length - 2; t += 3) {
        var a = o.charAt(t + 2);
        a = a >= "a" ? a.charCodeAt(0) - 87 : Number(a),
        a = "+" === o.charAt(t + 1) ? r >>> a: r << a,
        r = "+" === o.charAt(t) ? r + a & 4294967295 : r ^ a
    }
    return r
}
var C = null;
var token = function(r, _gtk) {
    var o = r.length;
    o > 30 && (r = "" + r.substr(0, 10) + r.substr(Math.floor(o / 2) - 5, 10) + r.substring(r.length, r.length - 10));
    var t = void 0,
    t = null !== C ? C: (C = _gtk || "") || "";
    for (var e = t.split("."), h = Number(e[0]) || 0, i = Number(e[1]) || 0, d = [], f = 0, g = 0; g < r.length; g++) {
        var m = r.charCodeAt(g);
        128 > m ? d[f++] = m: (2048 > m ? d[f++] = m >> 6 | 192 : (55296 === (64512 & m) && g + 1 < r.length && 56320 === (64512 & r.charCodeAt(g + 1)) ? (m = 65536 + ((1023 & m) << 10) + (1023 & r.charCodeAt(++g)), d[f++] = m >> 18 | 240, d[f++] = m >> 12 & 63 | 128) : d[f++] = m >> 12 | 224, d[f++] = m >> 6 & 63 | 128), d[f++] = 63 & m | 128)
    }
    for (var S = h,
    u = "+-a^+6",
    l = "+-3^+b+-f",
    s = 0; s < d.length; s++) S += d[s],
    S = a(S, u);
    return S = a(S, l),
    S ^= i,
    0 > S && (S = (2147483647 & S) + 2147483648),
    S %= 1e6,
    S.toString() + "." + (S ^ h)
}
"""


class BaiduTranslate(BaseTranslate):
    sess = requests.Session()
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }

    def __init__(self, content, proxies=None, sl='auto'):
        self.token = None
        self.gtk = None
        self.content = content
        self.proxies = proxies
        self.sl = sl

        # 获得token和gtk
        # 必须要加载两次保证token是最新的，否则会出现998的错误
        self._loadMainPage()
        self._loadMainPage()
        self.logger = logger

    def _loadMainPage(self):
        """
            load main page : https://fanyi.baidu.com/
            and get token, gtk
        """
        url = 'https://fanyi.baidu.com'

        try:
            r = self.sess.get(url, headers=self.headers)
            self.token = re.findall(r"token: '(.*?)',", r.text)[0]
            self.gtk = re.findall(r"window.gtk = '(.*?)';", r.text)[0]
        except Exception as e:
            raise e

    def _langdetect(self, query):
        """
            post query to https://fanyi.baidu.com/langdetect
            return json
            {"error":0,"msg":"success","lan":"en"}
        """
        url = 'https://fanyi.baidu.com/langdetect'
        data = {'query': query}
        try:
            r = self.sess.post(url=url, data=data)
        except Exception as e:
            raise e
            # print(e)

        json = r.json()
        if 'msg' in json and json['msg'] == 'success':
            return json['lan']
        return None

    def _dictionary(self, query):
        """
            max query count = 2
            get translate result from https://fanyi.baidu.com/v2transapi
        """
        url = 'https://fanyi.baidu.com/v2transapi'

        sign = execjs.compile(JS_CODE).call('token', query, self.gtk)

        lang = self._langdetect(query)
        data = {
            'from': lang,
            'to': 'zh',
            'query': query,
            'simple_means_flag': 3,
            'sign': sign,
            'token': self.token,
        }
        try:
            r = self.sess.post(url=url, data=data)
        except Exception as e:
            raise e

        if r.status_code == 200:
            json = r.json()
            if 'error' in json:
                raise Exception('baidu sdk error: {}'.format(json['error']))
                # 998错误则意味需要重新加载主页获取新的token
            return json
        return None

    def _dictionary_by_lang(self, query, tolang):
        """
            max query count = 2
            get translate result from https://fanyi.baidu.com/v2transapi
        """
        url = 'https://fanyi.baidu.com/v2transapi'

        sign = execjs.compile(JS_CODE).call('token', query, self.gtk)

        lang = self._langdetect(query)
        data = {
            'from': lang,
            'to': tolang,
            'query': query,
            'simple_means_flag': 3,
            'sign': sign,
            'token': self.token,
        }
        try:
            r = self.sess.post(url=url, data=data)
            # self.logger.info(r.text)
        except Exception as e:
            raise e

        if r.status_code == 200:
            json = r.json()
            if 'error' in json:
                raise Exception('baidu sdk error: {}'.format(json['error']))
                # 998错误则意味需要重新加载主页获取新的token
            return json["trans_result"]["data"][0]['dst']
        else:
            raise Exception('token 失效')
        return None

    def trans_text_en2cn(self):
        ret1 = self._dictionary_by_lang(self.content, tolang="zh")
        return ret1

    def trans_text_other2cn(self):
        return self.trans_text_en2cn()

    def trans_text_other2en(self):
        ret1 = self._dictionary_by_lang(self.content, tolang="en")
        return ret1


if __name__ == '__main__':
    for source_text in ['china', '저는 중국사람입니다']:
        res = BaiduTranslate(content=source_text).trans_text_other2cn()
        print(res)

    for source_text in ['中国', '저는 중국사람입니다']:
        res = BaiduTranslate(content=source_text).trans_text_other2en()
        print(res)
