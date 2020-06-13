
translate utils support google,baidu,iciba,youdao
### [introduction]

* support version: python 3.0+

### down install

* pip install:
```shell
pip install translate-util
```

### DEMO

```python
    from translate_util.translate_tool import translate_other2cn,translate_other2en
    
    # translate other language to chinese (default use google)
    print(translate_other2cn('china'))
    
    # translate other language to english (default use google)
    print(translate_other2en('中国'))
    
    # other translate demo
    content = 'china'
    for plat in ['google', 'baidu', 'iciba', 'youdao']:
        print(f'{plat}:{translate_other2cn(content, plat)}')

    content = '中国'
    for plat in ['google', 'baidu', 'iciba', 'youdao']:
        print(f'{plat}:{translate_other2en(content, plat)}')
```

### OTHER SUPPORT
any customization demand,contact me with email