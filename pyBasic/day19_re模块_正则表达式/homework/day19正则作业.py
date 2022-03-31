import re
# 1.匹配整数或者小数(包括正数和负数)
# (-)?\d+(\.\d+)?
# 2.匹配年月日，日期格式2022-03-16
# '(([1-9]\d{3})-(1[0-2]|0?[1-9])-([1-2]\d|[3][0-1]|0?[1-9]|)){1}'

# 分组命名匹配
# '([1-9]\d{3})(?P<sub>[^\d])(1[0-2]|0?[1-9])(?P=sub)([1-2]\d|[3][0-1]|0?[1-9]|)'

# 3.匹配QQ号
# 728250419
# [1-9]\d{3,10}

# 4. 11位电话号码
# 1[3-9]\d{9}

# 5. 长度为 9-10位的用户密码:还包含数字字母下划线
#
# 6. 匹配验证码: 4位数字字母组成
# \w{4}

# 7.匹配邮箱地址
# zhengew@foxmainl.com
# \w+@{1}\w+\.com[.cn]?



# 8.从类似
''''
<a>abcd</a>
<b>defdgg</a>
<h1>sgdd</h1>
'''
# 这样的字符串中匹配出 abcd defdgg sgdd 内容?
s = '<a>abcd</a><b>defdgg</b><h1>sgdd</h1>'
import re
regs1 = '<\w+>(\w+)</\w+>'
res = re.findall(regs1, s)
print(res)

# 匹配 a b h1
res = re.findall('<(\w+)>\w+</\w+>', s)

print(res)
# 9.
# 1-2*((60-30+(-40/5)(9-25/3+7/399/42998+10568/14))-(-43)/(16-3*2))
# 1> 从上面的算式中匹配出最内层的小括号以及小括号内的表达式
import re
s = '1-2*((60-30+(-40/5)(9-25/3+7/399/42998+10568/14))-(-43)/(16-3*2))'
reg = '\([^()]+\)'  # 卧槽 这个是转义 括号用的 \(\) 在正则中转义分组符号
res = re.findall(reg, s)
print(res)
# 10. 从类似 9-25/3+7/399/42998+10568/14 的表达式中匹配出从左到右第一个乘法或除法
'\d+[\.\d+]?[*/]-?\d+[\.\d+]?'
s = '9-25/3+7/399/42998+10568/14'
reg = '(\d+[*/]\d+)'
res = re.search(reg, s)
if res:
    print(res.group(1))

# 练习题:
#1. a 开头有至少一个字母组成的字符串
# a[a-zA-Z]+

#2. 以1开头，中间3-5位数字，x结尾，中间值不能超过5位
# 1\d{3,5}?x


# 找到lianjia.html中
reg = '<div class="title">.*?data-sl="">(?P<name1>.*?)</a>.*?data-el="region">(?P<name2>.*?)</a>.*?<span class="divide">/</span>(?P<name3>.*?)<span'
with open('lianjia.html', mode='r', encoding='utf-8') as f:
    contents = f.read()
    res = re.search(reg, contents, flags=re.S)
    print(res.group('name1'), res.group('name2'), res.group('name3'))