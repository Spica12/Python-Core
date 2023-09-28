import pickle

# 1. dump
# 2. load

a = (1, 2, 4)
b = pickle.dumps(a)

print(b)    # b'\x80\x04\x95\t\x00\x00\x00\x00\x00\x00\x00K\x01K\x02K\x04\x87\x94.'


c = pickle.loads(b)
print(c)    # (1, 2, 4)

print(a == c)   # True
print(a is c)   # False


print('---------------------------------------')
a = (1, 3, 5)

file_name = '12_you_theory_1_bin_serelisation'
extension = '.bin'
path = "D:\\GoIT\\Python Core\\Modul_12_Seralization_files\\3_Youtube_theory\\"
file_full_name = path + file_name + extension


with open(file_full_name, 'wb') as fh:
    pickle.dump(a, fh)


with open(file_full_name, 'rb') as fh:
    c = pickle.load(fh)

print(c)        # (1, 3, 5)
print(a == c)   # True
print(a is c)   # False


