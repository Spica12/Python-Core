"""
Є список, кожен елемент якого є словником з контактами користувача наступного виду:

    {
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}
Словник містить ім'я користувача name, його email, телефонний номер phone та 
властивість favorite - обраний контакт чи ні.

Розробіть дві функції для серіалізації та десеріалізації списку контактів за допомогою 
пакета pickle та зберігання отриманих даних у бінарному файлі.

Перша функція write_contacts_to_file приймає два параметри: filename - ім'я файлу, 
contacts - список контактів. Вона зберігає вказаний список у файл, використовуючи метод 
dump пакету pickle.

Друга функція read_contacts_from_file читає та повертає зазначений список contacts з 
файлу filename, використовуючи метод load пакету pickle.
------------------------------------------------------------
import pickle


def write_contacts_to_file(filename, contacts):
    
        


def read_contacts_from_file(filename):
"""
import pickle


def write_contacts_to_file(filename, contacts):
    with open(filename, 'wb') as file:
        pickle.dump(contacts, file)
        


def read_contacts_from_file(filename):
    with open(filename, 'rb') as file:
        contacts = pickle.load(file)

    return contacts