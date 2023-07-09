name = 'Alice'
age = 30

# 1
message = 'My name is %s. I am %d years old.' % (name, age)
print(message)
# 2
message = 'My name is {}. I am {} years old.'.format(name, age)
print(message)
# 3
message = f'My name is {name}. I am {age} years old.'
print(message)
# 4
message = 'My name is ' + name + '. I am ' + str(age) + ' years old.'
print(message)