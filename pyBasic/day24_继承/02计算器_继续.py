from functools import reduce

exp = (1+3*4*5/6)-4
# 计算两个数的乘法或者除法
def mul_div(exp):
    if '*' in exp:
        a, b = exp.split('*')
        return float(a)*float(b)
    if '/' in exp:
        a, b = exp.split('/')
        return float(a) / float(b)

def exp_fmt(exp):
    while re.search('[+-]{2,}',exp):
        exp = exp.replace('--','+')
        exp = exp.replace('+-','-')
        exp = exp.replace('-+','-')
        exp = exp.replace('++','+')
    return exp

def remove_addsub(exp):
    print(exp)
    ret = re.findall('[-+]?\d+(?:\.\d+)?',exp)
    print(ret)
    res = reduce(lambda a,b:float(a)+float(b),ret)
    return res
    # count = 0
    # for i in ret:
    #     count += float(i)
    # print(count)

# 计算表达式中的所有的乘除法
import re
def remove_muldiv(exp):
    while True:
        ret = re.search('\d+(\.\d+)?[*/]-?\d+(\.\d+)?',exp)
        if ret:
            son_exp = ret.group()   # 3*4  12*5
            res = mul_div(son_exp)
            print(res)  # 12  60
            exp = exp.replace(son_exp,str(res))
            print('-->',exp)  # exp = 1+12.0*5/6
        else:
            break
    return exp

# 计算乘除法
# ret = remove_muldiv('1+3*4*5/6-4-7')
# print(ret)

# 计算加减法
# exp = '1+2.238-++317+-428-5+6'
# exp = exp_fmt(exp)
# ret = remove_addsub(exp)
# print(ret)

# 计算一个带着加减乘除四则运算的表达式
# 把去括号这个事情做上

# 臧运达