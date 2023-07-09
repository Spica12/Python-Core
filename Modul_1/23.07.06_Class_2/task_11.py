
# Результат пошуку згенерував n записів (вводиться користувачем). 
# Скільки сторінок потрібно для відображення цих записів, якщо на 1 
# сторінку виводиться 10 записів.

count_of_record = int(input('Enter count of record: '))

RECORD_PER_PAGE = 10

pages = (count_of_record - 1) // 10 + 1
# for example
# +1 for not full page
# 64 // 10 --> 6 + 1 --> 7
# 63 // 10 --> 6 + 1 --> 7

# 60 // 10 --> 6 + 1 --> 7 but if 60 count we need 6 pages
# for it we use -1 
# (60 - 1) --> 59 // 10 --> 5 + 1 --> 6
# (64 - 1) --> 63 // 10 --> 6 + 1 --> 7

print(f'Pages is equal to {pages}')