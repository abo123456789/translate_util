
translate utils support google,baidu,iciba,youdao
##### [introduction]

* support version: python 3.0+

### down install

* pip install:
```shell
pip install translate_util
```

### DEMO

##### 1.发布消费字符串类型任务
```python
    content = 'china'
    for plat in ['google', 'baidu', 'iciba', 'youdao']:
        print(f'{plat}:{translate_other2cn(content, plat)}')

    content = '中国'
    for plat in ['google', 'baidu', 'iciba', 'youdao']:
        print(f'{plat}:{translate_other2en(content, plat)}')
```