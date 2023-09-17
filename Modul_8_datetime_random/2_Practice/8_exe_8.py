from collections import deque

MAX_LEN = 10

lifo = deque(maxlen=MAX_LEN)

def push(element):
    lifo.appendleft(element)


def pop():
    return lifo.popleft()

push('Biba')
push('Boba')
print(list(lifo))
print(pop())
push('Carl')
print(list(lifo))


fifo = deque(maxlen=MAX_LEN)

def push(element):
    lifo.append(element)

print('-----')
push('Biba')
push('Boba')
print(list(lifo))
print(pop())
push('Carl')
print(list(lifo))
