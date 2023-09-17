"""
You are given an array (which will have a length of at least 3, but 
could be very large) containing integers. The array is either entirely 
comprised of odd integers or entirely comprised of even integers except 
for a single integer N. Write a method that takes the array as an argument 
and returns this "outlier" N.

Examples
[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)
"""

def find_outlier(integers):
    numbers_odd = list()
    numbers_even = list()

    for integer in integers:
        if integer % 2 == 0:
            numbers_odd.append(integer)
        else:
            numbers_even.append(integer)
    
    if len(numbers_odd) == 1:
        return numbers_odd[0]
    elif len(numbers_even) == 1:
        return numbers_even[0]
    else:
        return None



example_one = [2, 4, 0, 100, 4, 11, 2602, 36]
example_two = [160, 3, 1719, 19, 11, 13, -21]

print(find_outlier(example_one), 'return 11, rhe only odd number')
print(find_outlier(example_two), 'return 160, rhe only even number')