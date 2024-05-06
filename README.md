![avatar](https://github.com/translate/translate/workflows/Test/badge.svg)  
translate utils support google
### [introduction]

* support version: python 3.0+

### down install

* pip install:
```shell
pip install translate-util
```

### DEMO

```python
    from translate_util.translate_tool import translate_other2cn,translate_other2en,translate_text
    
    # translate other language to chinese (default use google)
    print(translate_other2cn('china'))
    
    # translate other language to english (default use google)
    print(translate_other2en('中国'))
    
    # translate other language to de ,support any language
    print(translate_text('china', tl='de'))
    
    
```

### OTHER SUPPORT
any customization demand,contact me with email