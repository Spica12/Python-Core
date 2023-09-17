"""
You might know some pretty large perfect squares. But what about the NEXT one?

Complete the findNextSquare method that finds the next integral perfect square 
after the one passed as a parameter. Recall that an integral perfect square is 
an integer n such that sqrt(n) is also an integer.

If the parameter is itself not a perfect square then -1 should be returned. 
You may assume the parameter is non-negative.

Examples:(Input --> Output)

121 --> 144
625 --> 676
114 --> -1 since 114 is not a perfect square
"""

def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    num = sq ** 0.5
    if num == int(num):
        return (num + 1) ** 2
    else:
        return -1


print(find_next_square(121), 'need 144')
print(find_next_square(625), 'need 676')
print(find_next_square(114), 'need -1 since 114 is not a perfect square')