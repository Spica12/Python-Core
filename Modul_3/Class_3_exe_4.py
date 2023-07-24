

def actual_price(item, discount: float = 0):

    return item * (1- discount)


price_bread = 10
price_butter = 70
price_sugar = 40

print(f'Previous price {price_bread}, new price {actual_price(price_bread, 0.5)}')

print(f'Previous price {price_butter}, new price {actual_price(price_butter, 0.2)}')

print(f'Previous price {price_sugar}, new price {actual_price(price_sugar, 0.1)}')
