text = 'afshkdjfsa sdfkSDFDFsdfhkas fsdf df sdfskdf sdfjsd sdfsdl'

dict_counter = {} # {'L':1, 'O':2}

for char in text:

    # try:
    #     count = dict_counter[char] # Отримаємо значення по ключу
    # except KeyError:
    #     count = 0
    
    #  або 
    count = dict_counter.get(char, 0)

    count += 1
    dict_counter[char] = count

print(dict_counter)