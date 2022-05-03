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

    # String
        # set
            # 设置key value
            # 如果key存在则覆盖，不存在则新建
            # EX second 设置key的存活时间，单位是秒
            # PX 毫秒 设置key的存活时间，单位是毫秒
            # NX 如果键不存在，则新建，如果不存在，则返回nil
            # XX 只有键存在，才能操作
        # get
            # 获取key对应的value,只能获取一个，如果key存在，则返回值，如果key不存在，则返回nil
        # mset
            # 批量创建 key value 对应关系,会覆盖已存在的key
        # mget
            # 批量获取key,如果不存在，则返回nil
        # getset
            # 给指定的key设置新value,并返回原来的value,如果key不存爱，则返回nil
        # strlen
            # 返回value的长度
        # append
            # 如果key存在，则追加，如果key不存在，则新建
        # incr
            # 将key中存在的数加1，只能对数字有效
        # decr
            # 将key中存在的数减1，只能对数字有效
        # incrby
            # 将key中存在的数值，指定增加多少，只对数字有效
        # decrby
            # 将key中存在的数值，减少指定的值，只能对数字有效
        # getrange
            # 切片，同python类似，不能使用步长
        # incrbyfloat
            # 将key中存在的数值，增加指定的浮点数
        # lrem
            # 删除列表中的value
            # count > 0 从表头往表尾的方向查找，删除指定的个数
            # count = 0, 删除全部
            # count < 0, 从表尾的位置往表头的方向查找，删除指定的个数
        # let
            # 替换指定索引位置的value，如果索引超出范围，则报错
        # ltrim
            # 列表的切片

    # hash
        # {'db':{'redis':redis.conf, 'mysql':'mysql.cnf', 'nginx':'nginx.conf'}}
        # hset
            # 给hash增加 key-value 值
        # hlen
            # 获取hash的长度
        # hget
            # 获取某个hash里面key的value
        # hgetall
            # 获取所有的键值对
        # hmset
            # 批量增加键值对
        # hmget
            # 批量获取键值对
        # hsetnx
            # 给指定的hash增加键值对，如果原来的field存在，则操作无效,如果不存在，则新增
        # hkeys
            # 获取hash表中所有的field
        # hvals
            # 获取hash表中所有的value
        # hdel
            # 删除hash表中的一个或者多个 key-value
        # hexists
            # 判断hash表中的field是否存在，如果存在则为1，不存在则为0
        # hincrby
            # 给hash表中的key 增加指定的数值，只限于数字
        # hincrbyfloat
            # 给hash表中的key 增加指定的浮点数，只限于数字

    # set
        # sadd
            # 给集合添加值，如果值存在，则什么都不操作，如果值不存在，则添加
        # smembers
            # 获取集合所有的成员
        # scard
            # 获取集合的个数
        # sdiff
            # 获取两个集合的差集,前面存在后面不存在的值
        # sinter
            # 获取两个集合的交集
        # sunion
            # 获取两个集合的并集
        # sismember
            # 判断元素是否在集合中，如果存在，则为1，如果不存在，则为0
        # smove
            # 将指定的元素从一个集合移动到另一个集合中，
            # 如果原集合存在，则移动，如果不存则，则忽略
            # 如果目标集合存在，则直接移动，如果目标集合不存在，则新建集合并移动
        # spop
            # 随机删除指定个数的元素，并把删除的元素打印出来
        # srandmember
            # 随机获取指定个数的元素
            # 默认随机获取1个
            # 如果conunt > 0
                # 如果count > 集合元素个数，则全部取出
                # 如果count < 集合元素个数，则随机取出count个元素
            # 如果count < 0
                # 则随机count的绝对值次取出值
        # srem
            # 删除指定的1个或者多个元素

    # zset 有序集合
        # zadd key [NX|XX] [CH] [INCR] score member [score member ...]
        # 用法同 set











'''
