from collections import deque


def_list = list(range(2, 7))
print(def_list)

my_q = deque(def_list, 10)
print(my_q)
print(deque(def_list, 3))

for i in range(10):
    my_q.append(i)
    print(my_q)