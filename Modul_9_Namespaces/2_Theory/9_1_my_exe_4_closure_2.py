# Closure Замикання

def names():

    all_names = []

    def inner(name:str)->list:
        all_names.append(name)
        return all_names
    
    return inner


if __name__ == '__main__':

    boys = names()
    girls = names()
    
    print(boys('Vitalii'))
    print(boys('Sam'))
    print(boys('Dima'))

    print(girls('Lisa'))
    print(girls('Nastya'))
    print(girls('Natasha'))

