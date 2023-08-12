import re
# from re import search, findall, sub

pattern = r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)'

result = re.search(pattern, 'Here you can search  for some info: https://www.google.com sdfsdf gdfgafasd https://www.asd.com')
print(result) # <re.Match object; span=(36, 58), match='https://www.google.com'>

print(result.group())   # https://www.google.com
print(result.span()[0])   # 36
print(result.span()[1])   # 58

result = re.findall(pattern, 'Here you can search  for some info: https://www.google.com sdfsdf gdfgafasd https://www.asd.com')
print(result)