# 输出的内容是有等级的：默认处理warning级别以上的所有信息
# logging.debug('debug message')          # 调试
# logging.info('info message')            # 信息
# logging.warning('warning message')      # 警告
# logging.error('error message')          # 错误
# logging.critical('critical message')    # 批判性的
'''
# 实现能计算类似 等类似公式的计算器程序
# exp = 1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )

思路:
先匹配小括号里的内容
然后先计算乘除法
在计算加减法
用循环用正则
调用函数
'''
import  re
import logging

def cal_mul(exp):
    mul_reg = '(-?\d+\.\d+|-?\d+)[*](-?\d+\.\d+|-?\d+)'
    res = re.search(mul_reg, exp)

    return float(res.group(1)) * float(res.group(2))
# 除法
def cal_div(exp):
    div_reg = '(-?\d+\.\d+|-?\d+?)[/](-?\d+\.\d+|-?\d+?)'
    res = re.search(div_reg, exp)
    logging.debug(f'{res.group(1)}, {res.group(2)}, {float(res.group(1)) / float(res.group(2))}')
    return float(res.group(1)) / float(res.group(2))
# 加法
def cal_add(exp):
    add_reg = '(-?\d+\.\d+|-?\d+?)[+](-?\d+\.\d+|-?\d+?)'
    res = re.search(add_reg, exp)
    return float(res.group(1)) + float(res.group(2))

def cal_sub(exp):
    sub_reg = '(-?\d+\.\d+|-?\d+?)[-](-?\d+\.\d+|-?\d+?)'
    res = re.search(sub_reg, exp)
    print(res.group(1), res.group(2))
    return float(res.group(1)) - float(res.group(2))

# 计算括号内的
def cal_inner_bracker(exp):
    sum = 0
    inner_reg = '\([^()]+\)'
    res = re.finditer(inner_reg, exp)
    for i in res:
        # print(i.group())
        ret = re.search('\((?P<tag>.*?)\)', i.group()).group('tag').replace(' ', '')
        print(ret)
        # if '/' in ret:
        #     return cal_div(ret)
def main():
    logging.basicConfig(level=logging.DEBUG)
    exp = '1 - 2 * ( (60-30 +(-40  /  5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
    # reg = '\([^()]+\)'
    # ret = re.findall(reg, exp)
    # print(ret)
    # ret =  cal_mul('5*2')
    # ret = cal_div('-5.2/-2.1')
    # ret = cal_add('2+-1')
    # ret = cal_sub('1-1.3')
    res = cal_inner_bracker(exp)
    print(res)
if __name__ == '__main__':
    main()