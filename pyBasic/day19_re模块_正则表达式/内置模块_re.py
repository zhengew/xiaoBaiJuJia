''' 内置模块 re 正则表达式
re.findall() 查找所有，列表
re.search() 取值
'''

import re
#
# ret = re.findall('\d+', '1990ash1970abc')
# print(ret) # ['1990', '1970']
#
# ret = re.search('\d+8', '1990ash1970abc')
# print(ret) # <re.Match object; span=(0, 4), match='1990'>
# # print(ret.group()) # AttributeError: 'NoneType' object has no attribute 'group'
# if ret:
#     print(ret.group()) # 1990

# 预习一个现象  - 与分组有关
# findall 还是按照完整的正则进行匹配，只显示括号里匹配到的内容
# ret = re.findall("9(\d)\d", '17940ash93010uru')
# print(ret)

# search 还是按照完整的正则进行匹配，显示也是显示匹配到的第一个内容，
# 但是我们可以通过给group方法传参来获取具体分组中的内容
# ret = re.search("9(\d)(\d)", '17940ash93010uru')
# if ret:
#     print(ret.group())
#     print(ret.group(1))


''' 
1.总结:
findall
    # 取所有符合条件的，优先显示分组中的

search: 只取第一个符合条件的，没有优先显示这件事儿
    # 得到的结果是一个变量
        # 变量.group() 的结果 完全和 变量.group(0) 的结果一致
        # 变量.group(n) 的形式来指定获取第n个分组中匹配到的内容
'''

'''
2.为什么在search中不需要分组优先，而在 findall中需要？
'''
# 1>findall 加上括号，是为了对真正需要的内容进行提取
# ret = re.findall('<\w+>(\w+)</\w+)', '<h>abcdefg23</h>')
# print(ret) # ['abcdefg23']

#2> search
# ret = re.search('(<\w+>)(\w+)(</\w+>)', '<h>abcdefg23</h>')
# print(ret) # ['abcdefg23']
# if ret:
#     print(ret.group())
#     print(ret.group(1))
#     print(ret.group(2))

# 表达式 exp = '2-3*(5+6)'
# 计算 a+b 或者是 a-b 的结果？
# exp = '2-3*(5+6)'
# ret = re.search('(\d+)[+](\d+)', exp)
# print(ret)
# print(ret.group(1), ret.group(2))

'''
如果我们要查找的内容在一个复杂的环境中，我们要查找的内容并没有一个突出的与众不同的特点，
甚至会和不需要的杂乱的数据混合在一起，这个时候我们就需要把所有的数据都统计出来，然后对这个
数据进行筛选，把我们真正需要的数据对应的正则表达式用()圈起来，
这样我们就可以筛选出真正需要的数据了。
'''

ret = re.findall('1(\d)(\d)', '123')
print(ret) # [('2', '3')]
ret = re.findall('1(?:\d)(\d)', '123')
print(ret) # ['3']


''' 总结2:'''
# 1. 什么是爬虫？
     # 通过代码获取到一个网页的源码
     # 要的是源码中嵌着的网页上的内容
import requests
ret = requests.get('http://www.baidu.com')
print(ret.content.decode('utf-8'))
# 2. 分组和findall的现象
    # 为什么要分组？ 把想要的内容放分组里

# 3。如何取消分组优先
    # 如果在写正则的时候由于不得已的原因，导致不要的内容也得写在分组里，
    # (?:) 取消这个分组的优先显示

