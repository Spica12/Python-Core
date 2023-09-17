import random

print('------------------------------------------------ .randint()')
random_number = random.randint(0, 100)
print(random_number)

print('------------------------------------------------ .shuffle()')
mt_list = list(range(0, 10))
print(mt_list)

random.shuffle(mt_list)
print(mt_list)

print('------------------------------------------------ .choice()')
random_value_from_list = random.choice(mt_list)
print(random_value_from_list)

print('------------------------------------------------ .choices()')
random_values_from_list = random.choices(mt_list, k=2)
print(random_values_from_list)

print('------------------------------------------------ .sample()')
random_sample_values_from_list = random.sample(mt_list, k=2)
print(random_sample_values_from_list)

print('------------------------------------------------ .seed()')
# By default the random number generator uses the current system time

# Use the seed() method to customize the start number of the random 
# number generator

# If you use the same seed value twice you will get the same random
# number twice. 
random. seed(10)
print(random.random())      # 0.5714025946899135
random. seed(10)
print(random.random())      # 0.5714025946899135
