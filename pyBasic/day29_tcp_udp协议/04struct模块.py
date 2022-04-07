import struct

num1 = 129469649
num2 = 123
num3 = 8

ret1 = struct.pack('i', num1)
print(ret1)
ret2 = struct.pack('i', num2)
print(ret2)
ret3 = struct.pack('i', num3)
print(ret3)

print(struct.unpack('i', ret1))
print(struct.unpack('i', ret2))
print(struct.unpack('i', ret3))

# b'\xd1\x8c\xb7\x07'
# b'{\x00\x00\x00'
# b'\x08\x00\x00\x00'
# (129469649,)
# (123,)
# (8,)