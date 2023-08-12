message = "Hello, Привіт, "

print(message.encode())             # b'Hello, \xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd1\x96\xd1\x82, '
print(message.encode('utf-16'))     # b'\xff\xfeH\x00e\x00l\x00l\x00o\x00,\x00 \x00\x1f\x04@\x048\x042\x04V\x04B\x04,\x00 \x00'
print(message.encode('cp1251'))     # b'Hello, \xcf\xf0\xe8\xe2\xb3\xf2, '


print(b'\xff\xfeH\x00e\x00l\x00l\x00o\x00,\x00 \x00\x1f\x04@\x048\x042\x04V\x04B\x04,\x00 \x00'.decode('utf-16'))   # Hello, Привіт,

folder = Path('tmp')

with open(folder/'utf-8.txt', 'wb') as f:
    f.write(message.encode())

with open(folder/'utf-16.txt', 'wb') as f:
    f.write(message.encode('utf-16'))

with open(folder/'cp1251.txt', 'wb') as f:
    f.write(message.encode('cp1251'))


with open(folder/'cp1251.txt', 'rb') as f:
    print(f.read(message.decode('cp1251'))