'''

# 网络编程
# 概念

# B/S C/S 架构
    # C/S   client server
    # B/S   borwser server

# OSI七层协议
    # 应用层
    # 表示层
    # 会话层
    # 传输层
        # tcp 协议：效率低 面向连接 可靠 全双工通信
            # 三次握手
                # 客户端向服务端发送syn请求，
                # 服务端向客户端返回ack并发送syn请求，
                # 客户端接收到请求后再回复ack表示建立连接，
                # socket源码由客户端的connect + 服务端的accept
            # 四次挥手
                # 客户端向服务端fin请求
                # 服务端回复ack确认
                # 服务端向客户端发送fin请求
                # 客户端回复ack确认

                # 由客户端的close和服务端的close

            # 为什么握手的时候是三次，挥手的时候是四次？
                # 因为握手的时候 # 服务端向客户端返回ack并发送syn请求 这两条可以连在一起发，
                # 挥手的时候，这两条不可以一起发，因为服务端回复ACK确认，只代表同意了客户端向服务端发送的数据发送完了，
                # 并不代表着服务端向客户端发送的数据发送完了
                            # 服务端回复ack确认
                            # 服务端向客户端发送fin请求
            # 三次握手四次挥手参考连接 https://www.cnblogs.com/Eva-J/articles/8066842.html

        # udp 协议：效率高 无连接的 不可靠的
        # 四层交换机 四层路由器
    # 网络层
        # ip协议(ipv4 ipv6)
        # 路由器、交换机
    # 数据链路层
        # arp协议 地址解析协议 通过ip找到mac地址
        # 交换机、网卡：单播 广播 组播
    # 物理层
'''