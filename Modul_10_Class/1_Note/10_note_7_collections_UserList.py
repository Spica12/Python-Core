
"""
Часто для роботи потрібно створити об'єкти, які поводяться як стандартні 
контейнери Python, але з модифікованою поведінкою. Ви, звичайно, можете 
спробувати наслідувати dict, str, list, але це може призвести до ряду 
непередбачених помилок. Правильний спосіб отримати модифікований контейнер — 
це використовувати пакет collections та класи UserList, UserDict, UserString, 
які в ньому є.

Всі ці класи поводяться точно як вбудовані контейнери з тією лише відмінністю, 
що самі дані лежать у полі data у цих класів і ви можете використовувати це 
поле на свій розсуд.

self.data - дані лежать у полі data у цих класів


"""



from collections import UserList

class CountableList(UserList):

    def sum(self):
        return sum(map(lambda x: int(x), self.data))
    

countable = CountableList([1, '2', 3, 4])
countable.append('5')
print(countable.sum())      # 15