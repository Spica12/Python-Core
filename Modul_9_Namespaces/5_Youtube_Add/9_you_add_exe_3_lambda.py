import math

def get_length(d):
    result = d * math.pi

    return result


get_lambda_length = lambda d: d * math.pi


if __name__ == '__main__':
    length_1 = get_length(10)
    length_2 = get_lambda_length(10)
    print(length_1, length_2, sep='\n')