'''
nosql not only sql
用户画像：
热点数据：经常被使用的数据

# 安装：
    # yum安装, 要先配置epel源
        # yum install -y redis
    # 可以编译安装
        # wget http://download.redis.io/releases/redis-7.0.0.tar.gz
        # tar xf redis-7.0.0.tar.gz
        # cd redis-7.0.0/
        # make

# redis 可执行文件
    # redis-benchmark # 性能测试
    # redis-check-aof # 检查修复aof文件
    # redis-check-rdb # 检查修复rdb文件
    # redis-cli       # redis的客户端
    # redis-sentinel  # redis的集群
    # redis-server    # redis的服务端
    # redis-trib.rb   # 集群管理
# 启动redis
    # redis-server 默认端口 6379，默认启动会占用终端
        # root@ubuntu:/# ss -tnlp   # 查看端口占用情况
        # LISTEN  0       511              [::1]:6379            [::]:*     users:(("redis-server",pid=7383,fd=7))

# 性能测试
    # redis-benchmark
# 连接
    # redis-cli
    # -h <hostname>      Server hostname (default: 127.0.0.1).
    # -p <port>          Server port (default: 6379).
    # -s <socket>        Server socket (overrides hostname and port).
    # -a <password>      Password to use when connecting to the server.
    # -n <db>            Database number. 指定redis的库
    # redis命令不区分大小写

# redis的数据类型
    # string
    # hash
    # list
    # set
    # zset
# 命令相关
    # ping
        # 用来测试redis是否联通，返回值是pong
    # info
        # 获取系统的信息
        # info [section] # 可指定获取某一部分的信息
    # echo
        # 打印内容
    # quit
        # 退出
    # select
        # 切换redis的库，总共有16个，0~15
    # del
        # 删除一个或多个key,不存在的key忽略掉
    # exists
        # 判断key是否存在，存在是1，不存在是0
    # expire key seconds
        # 给指定的key设置存活时间，当key过期以后，就自动删除
    # ttl
        # 查看key的存活时间，-2 是key不存在, -1永久生效
    # keys
        # 查找所有符合pattern的key，支持通配符
    # move key db
        # 移动当前的key到指定的db里面，成功返回1，失败返回0
    # pexpire key milliseconds
        # 给一个key设置过期时间，单位是毫秒
    # pttl key
        # 查看key的存活时间，单位是毫秒
    # randomkey
        # 随机获取一个key，但是不删除,如果数据库为空，则返回空
    # rename key newkey
        # 重命名key,如果不存在，则报错,如果目标存在则覆盖
    # renamenx key newkey
        # 重命名key,如果key不存在，则报错，如果目标key存在则不变
    # type
        # 查看key所存储的数据类型，如果没有这个key，则返回none







'''
