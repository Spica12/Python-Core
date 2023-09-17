import time


# Використовується для внутрішніх потреб програми
# Наприклал, для вимірювання часу виконання функції

time_one = time.time()

count = 1
while count < 100_000_000:
    count += 1

time_two = time.time() # unic time stamp from 01 01 1970 in sec

print(time_two - time_one)  # 13.629354476928711