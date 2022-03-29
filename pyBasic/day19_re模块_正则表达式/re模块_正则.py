''' 内置模块 re模块
模块和时间工作时间的关系
    re 模块和正则表达式的关系: 有了re模块就可以在python语言操作正则表达式
正则表达式 ****
re模块 -- regex 正则表达式

1.什么是正则表达式？
一套规则， 匹配字符串的

2.能做什么？
1>检测一个输入的字符串是否合法  -- web开发项目 表单验证
 用户输入一个内容的时候，我们要提前做检测；能够提高程序的效率并且减轻服务器的压力
2>从一个大文件中检测所有合法的字符串 -- 日志分析\爬虫
 能够高校的从一大段文字中快速找到符合规则的内容

3. 正则规则:
1> 所有规则中的字符，就可以刚好匹配到字符串中的内容
2> 字符组 []：
    a, 描述的是一个位置上能出现的所有的可能性
    b, 接收范围，可以描述多个范围，连着写就可以了。
 [abc] 一个中括号只表示一个字符位置, 匹配 a或者b或者c
 [0-9] 根据ascii进行范围的比对，从小到大
 [a-z] 小写字母
 [A-Z] 大写字母
 [a-zA-Z] 大小写字母
 [0-9a-z] 所有的数字和小写字母
 [0-9a-zA-Z] 所有的数字和大小写字母

3> 在正则表达式中能够帮助我们表示匹配内容的符号都是正则中的 元字符
[0-9] - >               \d 匹配0-9之间任意一位数字 digit
[0-9a-zA-Z_] - >        \w 匹配所有的数字字母下划线 word
空白(空格 tab \n \enter) ->
空格 - > 空白
tab - > \t
enter回车 - > \n
空格 tab \n \enter - >   \s 匹配所有空白 包括 空格 制表符 换行 回车

元字符：
[]
\d 匹配所有数字
\w 匹配所有数字字母下划线
\s 匹配所有空白
\t 匹配tab
\n 匹配换行
# 取反
\W 非数字字符下划线
\D 非数字
\S 非空白

[\d\D]  - > 匹配数字和非数字，也就是 匹配所有
[\w\W] [\s\S] 同上

.  - > 匹配除了换行符的所有
# [^] 非字符组和[]字符组一起记忆
[^\d] -> 匹配所有的非数字
[^1] - > 陪所有的非1
^ 匹配一个字符串的开始
$ 匹配一个字符串的结尾
^a.$ - > 表示只能匹配 a开头的两位字符串，多一位就匹配不上
a表达式｜b表达式  ->  匹配a表达式或b表达式中的内容,如果匹配a成功了，不会继续和b匹配，所以，如果两个规则有重叠的部分，总是把长的放在前面
() 分组 -> 约束 | 描述的内容的范围问题。 www\.(baidu|taobao)\.com

4> 记忆元字符: 都是表示能匹配哪些内容，一个元字符总是表示一个字符位置上的内容
# \d \w \s \t \n \D \W \S
# [] [^] .
# ^ $
# () |

5> 量词 控制元字符匹配多少次
{n} 表示匹配n次
{n, } 表示至少匹配n次
{n, m} 表示至少匹配n次，至多m次
? 表示匹配0次或1次 {0, 1}
+ 表示匹配1次或多次 {1, }
* 表示匹配0次或多次 {0,}

匹配0次问题？
 # 整数 \d+
 # 小数 [0-9]+\.[0-9]+ 或者 \d+\.\d+
 # 整数或小数 \d+\.?\d*  有问题，会匹配 122.

 # 分组的作用（标准的整数或小数）: \d+(\.\d+)?    通过? 控制分组里的内容要么出现，要么不出现

练习：
1.手机号 1开头 第二位3-9，11位数字
1[3-9]\d{9}
2.判断用户输入的内容是否合法，如果用户输入的对就能查到结果，如果输入的额不对就不能查到结果
^1[3-9]\d{9}$    合法，即 约束内容是否合法
3.从一个大文件中找到所有符合规则的内容
1[3-9]\d{9}


7>
贪婪匹配:
 # 在量词范围允许的情况下，尽量多的匹配内容，例如\d{3, 9}  会匹配任意9位数字
 \d{3, }6  贪心算法和回溯算法
 # .*x  表示匹配任意字符，任意多次数 遇到最后一个x才停下来

非贪婪(惰性)匹配: ? 非贪婪标志符号
 #用法: 元字符 量词 ?
 # .*?x  表示匹配任意字符，任意多次数 但是一旦遇到x就停下来


8> 转义符 \
 # 原本有特殊意义的字符，到了表达它本身意义的时候，需要转义
 # 有一些特殊意义的内容，放在字符组中，会取消它的特殊意义
    [.()*+?] -> 只能表示 .
    [().*+?] -> 所有的内容在字符组中会取消它的特殊意义
    [a\-c]  - 在字符组中表示范围，如果不希望它表示范围，需要转义，或者放在字符组的最前面或最后面

'''

