''' 内置模块 logging

为什么要写log?
    # log 是为了排错
    # log 用来做数据分析

购物商城 - 数据库里
    # 什么时间购买了什么商品？
    # 把哪些商品加入了购物车

做数据分析的内容，- 记录到日志
# 1, 一个用户什么时间在什么地点 登陆了购物程序
# 2, 搜索了哪些信息，多长时间被展示出来
# 3, 什么时候关闭了软件
# 4, 对哪些商品进行了查看


log 日志:
# 1. 用来记录用户的行为 - 数据分析
# 2. 用来记录用户的行为 - 操作审计
# 3. 排查代码中的错误
'''

import logging
# 输出的内容是有等级的：默认处理warning级别以上的所有信息
# logging.debug('debug message')          # 调试
# logging.info('info message')            # 信息
# logging.warning('warning message')      # 警告
# logging.error('error message')          # 错误
# logging.critical('critical message')    # 批判性的

def cal_mul():pass
def cal_div():pass
def cal_add():pass
def cal_sub():pass
def cal_mul():pass
def cal_inner_bracker():pass

def main(wxp):
    exp = '(1+2)*(3-4)/5'
    pass

main('(1+2)*(3-4)/5')

''' 注意：
1. 无论你希望日志里打印哪些内容，都得你自己写，没有自动生成日志这种事儿
'''

'''
2.设置日志的格式：
basicConfig(*,
                filename: Optional[str] = ...,
                filemode: str = ...,
                format: str = ...,
                datefmt: Optional[str] = ...,
                level: Union[int, str, None] = ...,
                stream: IO[str] = ...) -> None
'''

'''
2.1. 输出到屏幕
'''
# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s[line:%(lineno)d] -%(module)s:  %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S %p',
# )
# logging.warning('warning merssage test2') # 2022-03-30 21:00:10 PM - root - WARNING[66] -内置模块_logging:  warning merssage test2
# logging.error('warning merssage test2')


'''
2.2. 输出到文件,并且设置信息的等级
'''
# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s[line:%(lineno)d] -%(module)s:  %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S %p',
#     filename='tmp.log',
#     level = logging.DEBUG,
# )
# logging.warning('warning 信息错误 merssage test2') # 2022-03-30 21:00:10 PM - root - WARNING[66] -内置模块_logging:  warning merssage test2
# logging.error('warning merssage test2')

# 2.3 问题：
# 乱码
# 同时向文件和屏幕输出
# fh = logging.FileHandler('tmp.log', encoding='utf-8')
# fh2 = logging.FileHandler('tmp2.log', encoding='utf-8')
# sh = logging.StreamHandler()
# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s[line:%(lineno)d] -%(module)s:  %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S %p',
#     level = logging.DEBUG,
#     handlers = [fh,fh2,sh],
# )
# logging.warning('warning 信息错误 merssage test2') # 2022-03-30 21:00:10 PM - root - WARNING[66] -内置模块_logging:  warning merssage test2
# logging.error('warning merssage test2')


'''
3. 如何做日志的切分
'''
from logging import handlers
import time
rh = handlers.RotatingFileHandler('myapp.log', maxBytes=1024,backupCount=5) # 按照大小做切割
fh = handlers.TimedRotatingFileHandler(filename='x2.log', when='s', interval=5, encoding='utf-8')

sh = logging.StreamHandler()
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s[line:%(lineno)d] -%(module)s:  %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %p',
    level = logging.DEBUG,
    handlers = [rh, fh, sh],
)
for i in range(1,10):
    time.sleep(1)
    logging.error('KeyboardInterrupt error %s'%str(i))
