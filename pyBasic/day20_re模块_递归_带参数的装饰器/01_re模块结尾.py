# 1.re 模块结尾
# 2.带参数的装饰器、递归函数

''' re 模块方法:
findall
search

split
sub
subn
match
compile
finditer
'''

import re

'''
1.split 分隔
'''
# res1 = re.split('\d+', 'alex123wusir')
# res2 = re.split('(\d+)', 'alex123wusir')
# res3 = re.split('\d(\d)\d', 'alex123wusir')
# print(res1) # ['alex', 'wusir']
# print(res2) # ['alex', '222', 'wusir']
# print(res3) # ['alex', '2', 'wusir']

'''
2.sub 替换
'''
ret = re.sub('\d', 'H', 'aelx123wusir456', count=1)
print(ret) # aelxH23wusir456

'''
3. subn
'''
ret = re.subn('\d', 'H', 'aelx123wusir456')
print(ret) # ('aelxHHHwusirHHH', 6)

'''
4.match 
相当于search 在 正则表达式中加了 ^

用户输入的内容匹配的时候，要求用户输入11位手机号码， ^手机号正则$
match('^手机号正则$', '手机号码') 规定这个字符号必须是什么样的
findall('^手机号正则$', '手机号码') 用来寻找这个字符串中是不是含有满足条件的子内容

'''
ret = re.match('\d+', '123eval123taibai456')
print(ret) # 123
print(ret.group())
ret = re.match('^\d+', '123eval123taibai456')


''' ***
5.compile  -- 节省代码时间的工具
 # 假如同一个正则表达式要被使用多次
 # 节省了多次解析同一个正则表达式的时间
'''
ret = re.compile('\d+')
res1 = ret.search('alex123456')
res2 = ret.findall('alex123456')
print(res1)
print(res2)
'''
6.finditer -- 节省空间
'''
ret = re.finditer('\d+', 'sgksllll0183156')
for i in ret:
    print(i.group())


'''
先 compile（如果没有重复使用一个正则，也不能节省时间）
再 finditer(在结果特别多的时候使用),既节省时间又节省空间
'''
ret = re.compile('\d+')
res = ret.finditer('abc123d456')
for i in res:
    print(i.group())





''' 了解时间和空间
功能:

性能:
    # 时间: 
        # 你要完成一个代码所需要执行的代码行数;
        # 你在执行代码的过程中，底层程序是如何工作的;
    # 空间:
        # 是占用了宝贵的内存条资源
        # 影响程序的执行效率
用户体验

列表不能用 insert
列表不能用 pop(0)
'''
