byte_array = bytearray(b'Kill Bill')
byte_array[0] = ord('B')
byte_array[5] = ord('K')
print(byte_array)   # bytearray(b'Bill Kill')

# Основна відмінність - це змінність
# Друга відмінність - система сприймає масив байтів як послідовність чисел від 0 до 255, а не як послідовність символів в ASCII кодуванні.


