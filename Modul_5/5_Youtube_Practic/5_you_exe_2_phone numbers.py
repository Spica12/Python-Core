# 0681231212
from re import search

pattern = r'^\+?3?8?[- (]?0\d{2}[- )]?\d{3}[- ]?\d{2}[- ]?\d{2}'


phone_numbers = ['+380681231234',
                 '123534',
                 '068123458123123',
                 '380681231234',
                 '+38 068 749 34 44',
                 '+38068 123 12 34',
                 '+38(068) 1231234',
                 '+38(068)123 12 34',
                 '068-123-45-87',
                 '1 2 3 4',
                 '+390681231234']


for number in phone_numbers:

    result = search(pattern, number)

    if result is None:
        print(f'Negative - {number}')
    else:
        print(f'Positive - {result.group()}')