import hashlib

def get_md5(username, password):
    m = hashlib.md5(username.encode('utf-8'))
    m.update(password.encode('utf-8'))
    return m.hexdigest()

ret = get_md5('test1', '123456')
print(ret)