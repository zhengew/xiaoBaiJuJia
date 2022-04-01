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
# 思路：
# 1.先计算括号内的乘法和除法，然后replace 表达式中的 乘除法；替换完后，同样的方式替换加法和减法，然后同样的逻辑替换到外层的小括号，
# 直到括号内的都被计算
# 2. 当表达式括号内的加减法都计算完毕以后，在按照从左到右的顺序计算加减法

# 明早先写在这个作业

# 乘法和除法
def cal_mul_div(exp):
    exp = exp.replace(' ', '')
    cal_mul_div_reg = '(-?\d+(\.\d+)?[*/]-?\d+(\.\d+)?)'
    while True:
        res = re.search(cal_mul_div_reg, exp)
        if res:
            # print(res)
            ret = res.group()
            # print(ret)
            if '*' in ret:
                a, b = ret.split('*')
                exp = exp.replace(ret, str(float(a) * float(b)))
            elif '/' in ret:
                a, b = ret.split('/')
                exp = exp.replace(ret, str(float(a) * float(b)))
        else:
            break
    return exp

def cal_add_sub(exp):
    exp = exp.replace(' ', '')
    add_sub_reg = '(-?\d+(\.\d+)?)[-+](-?\d+(\.\d+)?)'
    while True:
        res = re.search(add_sub_reg, exp)
        # print(res)
        if res:

            ret = res.group()
            # print(ret)

            if '-' in ret and not ret.startswith('-'):
                a, b = ret.split('-')
                # print(a, b)
                exp = exp.replace(ret, str(float(a) - float(b)))
            elif '+' in ret and not ret.startswith('+'):
                a, b = ret.split('+')
                exp = exp.replace(ret, str(float(a) + float(b)))

            elif ret.startswith('-') and ret.count('-') == 2:
                a, b = ret[1:].split('-')
                # print(a, b)
                exp = exp.replace(ret, str(-float(a) - float(b)))
            elif ret.startswith('-') and ret.count('-') == 1:
                a, b = ret[1:].split('-')
                exp = exp.replace(ret, str(-float(a) + float(b)))

        else:
            break
    return exp

# 计算括号内的
def cal_inner_bracker(exp):
    exp = exp.replace(' ', '')
    inner_bracker_reg = '\((-?\d+(\.\d+)?)?\)[*/]\((-?\d+(\.\d+)?)?\)'
    res = re.finditer(inner_bracker_reg, exp)

    pass # 没实现



    # print(exp)
def main():
    logging.basicConfig(level=logging.DEBUG)
    exp = '1 - 2 * ( (60-30 +(-40  /  5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
    # exp = '( (60-30 +(-40  /  5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
    # print(cal_mul_div(exp))
    # print(cal_add_sub(cal_mul_div(exp)))
    # print(cal_inner_bracker(exp))

if __name__ == '__main__':
    main()