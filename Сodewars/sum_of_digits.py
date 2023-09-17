"""
Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. If that value has more 
than one digit, continue reducing in this way until a single-digit 
number is produced. The input will be a non-negative integer.

Examples
    16  -->  1 + 6 = 7
   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
"""

def digital_root(n):
    print(n)
    sum = 0

    if n <= 9:
        return n
    else:
        for digital in str(n):
            sum += int(digital)
        return digital_root(sum)

    # if n > 9:
    #     for digital in str(n):
    #         sum += int(digital)
    #     print(n, sum)

    #     if sum > 9:
    #         n = digital_root(sum)
    # else:
    #     return n






answwer = digital_root(16)
print(answwer, 'right answer is 7')
print(digital_root(942), 'right answer is 6')
print(digital_root(132189), 'right answer is 6')
print(digital_root(493193), 'right answer is 2')