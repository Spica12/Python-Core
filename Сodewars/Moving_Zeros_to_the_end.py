"""
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
"""


def move_zeros(lst):
    for indx in range(len(lst)):

        if lst[indx] == 0:
            lst.remove(0)
            lst.append(0)

    return lst



my_list = [1, 0, 1, 2, 0, 1, 3]
result = move_zeros(my_list)
print(result) # returns [1, 1, 2, 1, 3, 0, 0]