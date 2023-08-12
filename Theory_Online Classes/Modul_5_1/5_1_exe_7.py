symbols = "0123456789ABCDEF"
code = [
        '0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111',
        '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111'
        ]

MAP = {}

for key, value in zip(symbols, code):
    MAP[ord(key)] = value

    # MAP[ord(key.lower())] = value

print(MAP)

result = '34 DE 5C B0'.translate(MAP)
print(result)