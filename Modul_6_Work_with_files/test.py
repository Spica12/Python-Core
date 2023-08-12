fh = open('test_file.txt', 'r')
while True:
    symbol = fh.read(1)
    if len(symbol) == 0:
        break 
    print(symbol)  
fh.close()
