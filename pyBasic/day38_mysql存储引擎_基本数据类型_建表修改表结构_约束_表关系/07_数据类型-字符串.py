''' 字符串
char
varchar

'''

# char(18)      最多只能表示255个字符
    # 定长存储，节省时间，浪费空间
    # 'alex'    'alex              '
# varchar(18)   最多能表示65535个字符
    # 变长存储,下面更节省空间，存取速度慢
    # 'alex'    'alex4'

# 适合使用char
    # 身份证号
    # 手机号
    # qq号
    # username 12 - 18
    # password 32
    # 银行卡号

# 适合使用varchar
    # 评论
    # 朋友圈
    # 微博

# create table t6(
#     c1 char,
#     v1 varchar(1),
#     c2 char(8),
#     v2 varchar(8)
# );