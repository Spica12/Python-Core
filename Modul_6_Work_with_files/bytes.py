"""

"""
s = b'Hello'
print(s[1]) # 101
print('------------------------ b' '  ')
byte_string = b'Hello World!'

print('------------------------ encode ')
byte_str = 'some text'.encode()

print('-------------------------------- ')

numbers = [0, 128, 255]
byte_numbers = bytes(numbers)
print(byte_numbers) # b'\x00\x80\xff'

# \x - вказує на шістнадцятковий формат запису

for num in byte_numbers:
    print(int(num))
# 0
# 128
# 255

for num in numbers:
    print(hex(num))
# 0x0
# 0x80
# 0xff

print('-------------------------------- ')
