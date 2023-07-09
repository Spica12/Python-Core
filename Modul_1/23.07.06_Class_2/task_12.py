# Скласти програму, яка переводить час із секунд, визначаючи повну 
# кількість годин хвилин і секунд (наприклад, час 5000 секунд це 1 
# година 23 хвилини 20 секунд 5000=13600+2360+20).

time = int(input('Enter time in seconds: '))

# 1 minute = 60 seconds
# 1 hour = 60 minutes --> 60 * 60 --> 3600 seconds

# 5000 // 3600 --> 1 % 60 --> 1
# 5000 // 60 --> 83 % 60 --> 23
# 5000 % 60 --> 20
print((time // 3600), (time // 3600) % 60)
print((time // 60), (time // 60) % 60)
print(time % 60)

hours = (time // 3600) % 60
minutes = (time // 60) % 60
seconds = time % 60

print(f"{time} seconds = {hours} hours, {minutes} minutes, {seconds} seconds")