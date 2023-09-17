from functools import reduce


def max_product(A):

    neg_num = 0
    pos_idx = None
    neg_idx = None
    max_neg_idx = None

    for i, a in enumerate(A):

        if a < 0:
            neg_num += 1

            if neg_idx is None or A[neg_idx] < a:
                neg_idx = i
            
            if max_neg_idx is None or a < A[max_neg_idx]:
                max_neg_idx = i

        else:
            if pos_idx is None or a < A[pos_idx]:
                pos_idx = i


    skip_idx = (neg_idx if neg_num % 2 else pos_idx if pos_idx is None else max_neg_idx)

    return reduce(lambda product,  a: product * a, (a for i, a in enumerate(A) if i != skip_idx), 1)


print([3, 2, 5, 4])
print(max_product([3, 2, 5, 4]))
