from re import search

result = search('^Hello', 'Hello world')
print(result)   # <re.Match object; span=(0, 5), match='Hello'>

result = search('world$', 'Hello world')
print(result)   # <re.Match object; span=(6, 11), match='world'>

result = search('^world$', 'Hello world')
print(result)   # None

result = search('^world$', 'world')
print(result)   # <re.Match object; span=(0, 5), match='world'> 

result = search('l*', 'world')
print(result)   # 