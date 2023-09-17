from datetime import datetime


def for_generator():
    my_list = list()

    for i in range(0, 1_000_000):
        my_list.append(i)

def comprehensions_generator():
    my_list = [i for i in range(0, 1_000_000)]

times = []
comprehensions_times = []
n = 100

for i in range(0, n):

    time_start = datetime.now().timestamp()
    for_generator()
    time_end = datetime.now().timestamp()
    result = time_end - time_start
    times.append(result)
    print(result)

    time_start = datetime.now().timestamp()
    comprehensions_generator()
    time_end = datetime.now().timestamp()
    result = time_end - time_start
    comprehensions_times.append(result)
    print(result)


average_result_times = sum(times) / n
average_result_comrehensions_times = sum(comprehensions_times) / n

print(average_result_times, ' sec')
print(average_result_comrehensions_times, ' sec')