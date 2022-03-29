''' re模块
'''
import re

'''
1.分组命名
    ret = re.search(?P<名字>正则表达式)  注意啊：是大写的P
    ret.group('名字') 来获取分组名匹配的内容
'''

'''
2. 分组命名的引用
'''
# exp = '<a>abcdefggheig</a>sfsgsgsggsg</a>'
# ret = re.search('<(?P<tag>\w+)>.*?</(?P=tag)>', exp)
# print(ret)

'''
3. 分组的索引
re.search(r'<(\w+)>.*?</\1>', exp)
用处不大...
'''
exp = '<a>abcdefggheig</a>sfsgsgsggsg</a>'
ret = re.search(r'<(\w+)>.*?</\1>', exp)
print(ret)


# 面试题: 匹配整数
ret=re.findall(r"\d+\.\d+|(\d+)","1-2*(60+(-40.35/5)-(-4*3))")
print(ret) # ['1', '2', '60', '', '5', '4', '3'] # 通过分组过滤 小数
ret = filter(lambda n:n, ret)  # 通过filter过滤空
print(list(ret)) # ['1', '2', '60', '5', '4', '3']

''' 总结

1> 分组命名 (?P<组名>正则)  (?P=组名)
2> 有的时候我们要匹配的内容是包含在不想要的内容之中的，只能先把不想要的内容匹配出来，然后再想办法从结果中去除。
    例如通过filter函数过滤.
'''