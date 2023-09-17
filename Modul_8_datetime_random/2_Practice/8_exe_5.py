from collections import Counter
# from pathlib import Path

def num_counter(filename, n):
    with open(filename, 'r') as file:
        data = file.read()

    counter = Counter([int(i) for i in data.split(',')])
    order = counter.most_common(len(counter))
    print(order)

    return [i for i, _ in order[:n]], [i for i, _ in order[-n:]]


most, least = num_counter('8_exe_5.txt', 10)
print(most)
print(least)