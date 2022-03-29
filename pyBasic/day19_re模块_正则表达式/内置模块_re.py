''' 内置模块 re 正则表达式
re.findall() 查找所有
re.search()
'''

import re

ret = re.findall('\d+', '1990ash1970abc')
print(ret) # ['1990', '1970']

ret = re.search('\d+8', '1990ash1970abc')
print(ret) # <re.Match object; span=(0, 4), match='1990'>
# print(ret.group()) # AttributeError: 'NoneType' object has no attribute 'group'
if ret:
    print(ret.group()) # 1990