'''
元字符
    # \d \s \w \t \n \D \S \W
    # [] [^]
    # () |

量词
    # {} 表示任意的次数，任意次数范围，至少多少次
    # ? + * 表示 [0,1] [1, ) [0, )

贪婪和非贪婪匹配
    # 总是在量词范围内尽量多匹配 - 贪婪
    # 总是在量词范围内尽量少匹配 - 惰性
    # .*?x  匹配任意内容，任意次数，遇到x就停止
    # .+?x  匹配任意内容至少1次，遇到x就停止

转义符问题
    # . 有特殊的意义，取消特殊的意义 \.
    # 取消一个元字符的特殊意义有两种方法
        # 在这个元字符前面加 \
        # 对一部分字符生效，把这个元字符放在字符组里
            # [.()*+?]
'''

# 练习：18位或者15位身份证号
    # 15位：1-9  15       ^[1-9]\d{14}$

    # 18位： 1-9 16 0-9/X   ^[1-9]\d{16}[\dX]$

    # 18位或15位    ^([1-9]\d{16}[\dX]|[1-9]\d{14})$
    # 或者 ^[1-9]\d{14}(\d{2}[\dX])?$