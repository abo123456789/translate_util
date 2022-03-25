# -*- coding:utf-8 -*-
# @Author cc
# @TIME 2020/04/29 23:26
# coding=utf-8

from setuptools import setup, find_packages

setup(
    name='translate_util',
    version='1.0.8',
    description=(
        'translate tool support(google,baidu,iciba,youdao)'
    ),
    long_description_content_type="text/markdown",
    long_description=open('README.md').read(),
    author='cc',
    author_email='abcdef123456chen@sohu.com',
    maintainer='cc',
    maintainer_email='abcdef123456chen@sohu.com',
    license='MIT License',
    install_requires=[
        "requests>=2.22.0",
        "retrying>=1.3.3",
        "loguru>=0.3.2",
        "PyExecJS>=1.5.1"
    ],
    packages=find_packages(),
    platforms=["all"],
    url='https://github.com/abo123456789/translate_util',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ])