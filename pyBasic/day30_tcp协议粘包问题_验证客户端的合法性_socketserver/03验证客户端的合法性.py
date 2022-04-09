# # 生成一个随机字符串
# import os
# ret = os.urandom(16) # 生成指定长度的随机字符串
# print(ret)
#
# import hashlib
# sha = hashlib.sha1('密钥'.encode('utf-8'))
# sha.update('随机字符串'.encode('utf-8'))
# result = sha.hexdigest()
# print(result)

import os
import hmac # 替代hashlib模块的

h = hmac.new(b'alex_sb',os.urandom(32),digestmod='MD5')
ret = h.digest()
print(ret)

print(os.urandom(32))