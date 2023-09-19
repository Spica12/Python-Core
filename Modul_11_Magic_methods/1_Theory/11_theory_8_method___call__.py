# Викликати клас як функцію

class Product:
    # def __init__(self, value_one, value_two):
    #     self.one = value_one
    #     self.value_two = value_two

    def __call__(self, value_one, value_two):
        return value_one * value_two

test = Product()

print(test(2, 5))   # 10