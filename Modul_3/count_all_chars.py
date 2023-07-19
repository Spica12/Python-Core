

def count_all(text):

    operation_dict = dict()

    for char in text:

        if char not in operation_dict.keys():
            operation_dict[char] = 1
        else:
            operation_dict[char] += 1

    return operation_dict

message = 'Hello my dear friend!'
my_dict = count_all(message)
print(my_dict)
