# -*- coding:utf-8 -*-
# @Author cc
# @TIME 2020/5/25 16:46
import traceback

from retrying import retry
from translate_util.translate_baidu import BaiduTranslate
from translate_util.translate_google import GoogleTranslate
from translate_util.translate_iciba import IcibaTranslate
from translate_util.translate_youdao import YoudaoTranslate


@retry(stop_max_attempt_number=3)
def translate_en2cn(content, platform='google'):
    """
    根据翻译平台将中文翻译成英文
    :param content: 带翻译的平台
    :param platform: 使用的翻译平台 google,baidu,iciba,youdao
    :return: 
    """
    try:
        if platform == 'google':
            return GoogleTranslate(content=content).trans_text_en2cn()
        elif platform == 'baidu':
            return BaiduTranslate(content=content).trans_text_en2cn()
        elif platform == 'iciba':
            return IcibaTranslate(content=content).trans_text_en2cn()
        elif platform == 'youdao':
            return YoudaoTranslate(content=content).trans_text_en2cn()
        else:
            return GoogleTranslate(content=content).trans_text_en2cn()
    except:
        raise Exception(traceback.format_exc())


@retry(stop_max_attempt_number=3)
def translate_other2cn(content, platform='google'):
    """
    根据翻译平台将其它语言翻译成中文
    :param content: 带翻译的平台
    :param platform: 使用的翻译平台 google,baidu,iciba,youdao
    :return:
    """
    try:
        if platform == 'google':
            return GoogleTranslate(content=content).trans_text_other2cn()
        elif platform == 'baidu':
            return BaiduTranslate(content=content).trans_text_other2cn()
        elif platform == 'iciba':
            return IcibaTranslate(content=content).trans_text_other2cn()
        elif platform == 'youdao':
            return YoudaoTranslate(content=content).trans_text_other2cn()
        else:
            return GoogleTranslate(content=content).trans_text_other2cn()
    except:
        raise Exception(traceback.format_exc())


@retry(stop_max_attempt_number=3)
def translate_other2en(content, platform='google'):
    """
    根据翻译平台将其它语言翻译成英文
    :param content: 带翻译的平台
    :param platform: 使用的翻译平台 google,baidu,iciba,youdao
    :return:
    """
    try:
        if platform == 'google':
            return GoogleTranslate(content=content).trans_text_other2en()
        elif platform == 'baidu':
            return BaiduTranslate(content=content).trans_text_other2en()
        elif platform == 'iciba':
            return IcibaTranslate(content=content).trans_text_other2en()
        elif platform == 'youdao':
            return YoudaoTranslate(content=content).trans_text_other2en()
        else:
            return GoogleTranslate(content=content).trans_text_other2en()
    except:
        raise Exception(traceback.format_exc())


if __name__ == '__main__':
    content = 'china'
    for plat in ['google', 'baidu', 'iciba', 'youdao']:
        print(f'{plat}:{translate_other2cn(content, plat)}')

    content = '中国'
    for plat in ['google', 'baidu', 'iciba', 'youdao']:
        print(f'{plat}:{translate_other2en(content, plat)}')
