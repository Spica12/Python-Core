# --------------------------------- add(elem)
# Додає елемент в множину
numbers = {1, 2, 3}
numbers.add(4)

print(numbers)      # {1, 2, 3, 4}

# --------------------------------- remove(elem)
# видаляє елемент з множини, 
# викликає виняток, якщо немає такого
numbers = {1, 2, 3}
numbers.remove(6)

print(numbers)      

# Traceback (most recent call last):
#   File "d:\GoIT\Python Core\Conteiners\set_methods.py", line 12, in <module>
#     numbers.remove(6)
# KeyError: 6

# --------------------------------- discard(elem)
# видаляє елемент з множини, 
# і НЕ викликає виняток, якщо немає такого
numbers = {1, 2, 3}
numbers.discard(4)

print(numbers)      # {1, 2, 3}

