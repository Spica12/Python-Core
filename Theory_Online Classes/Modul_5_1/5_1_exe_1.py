

def delete_string(data):
    result = list()

    for element in data:
        if element.isdigit():
            result.append(element)

    return result


def transform_number(data):
    result = list()

    for i in data:
        result.append(int(i))

    return result


numbers = ["123", "456", "321", "10", "75", "abc", "23c"]


only_numbers = delete_string(numbers)
digits = transform_number(only_numbers)
print(only_numbers)

print(f'Difference {max(digits) - min(digits)}')
print(f'Average value {sum(digits) / len(digits)}')


