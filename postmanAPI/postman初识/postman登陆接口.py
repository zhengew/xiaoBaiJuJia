import hashlib

def get_md5(args):
    m = hashlib.md5(args.encode('utf-8'))
    return m.hexdigest()

print(get_md5('12345678'))