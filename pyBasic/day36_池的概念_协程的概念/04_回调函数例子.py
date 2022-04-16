from concurrent.futures import ThreadPoolExecutor
import requests
import os

def get_page(url):    # 访问网页,获取网页源代码   线程池中的线程来操作
    print('<进程%s> get %s' %(os.getpid(),url))
    respone=requests.get(url)
    if respone.status_code == 200:
        return {'url':url,'text':respone.text}

def parse_page(res):   # 获取到字典结果之后,计算网页源码的长度,把https://www.baidu.com : 1929749729写到文件里   线程任务执行完毕之后绑定回调函数
    res=res.result()
    print('<进程%s> parse %s' %(os.getpid(),res['url']))
    parse_res='url:<%s> size:[%s]\n' %(res['url'],len(res['text']))
    with open('db.txt','a') as f:
        f.write(parse_res)

if __name__ == '__main__':
    urls=[
        'https://www.baidu.com',
        'https://www.python.org',
        'https://www.openstack.org',
        # 'https://help.github.com/',
        'http://www.sina.com.cn/'
    ]
    # 获得一个线程池对象 = 开启线程池
    tp = ThreadPoolExecutor(4)
    # 循环urls列表
    for url in urls:
        # 得到一个futrue对象 = 把每一个url提交一个get_page任务
        res = tp.submit(get_page, url)
        # 给futrue对象绑定一个parse_page回调函数
        res.add_done_callback(parse_page)       # 谁先回来谁就先写结果进文件

# 不用回调函数:
    # 按照顺序获取网页 百度 python openstack git sina
    # 也只能按照顺序写
# 用上了回调函数
    # 按照顺序获取网页 百度 python openstack git sina
    # 哪一个网页先返回结果,就先执行那个网页对应的parserpage(回调函数)


# 会起池\会提交任务
# 会获取返回值\会用回调函数

# 1.所有的例题 会默
# 2.进程池(高计算的场景,没有io(没有文件操作\没有数据库操作\没有网络操作\没有input)) : >cpu_count*1  <cpu_count*2
#   线程池(一般根据io的比例定制) : cpu_count*5
# 5*20 = 100并发
