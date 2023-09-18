"""
Є список contacts, елементи якого - словники контактів наступного виду:

    {
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}
Словник містить ім'я користувача, його email, телефонний номер та 
властивість - обраний контакт чи ні.

Створіть функцію get_favorites(contacts), яка повертатиме список, який містить 
лише обрані контакти. Використовуйте при цьому функцію filter, щоб відфільтрувати 
по полю favorite лише обрані контакти.
-----------------------------------------------------------------------------
def get_favorites(contacts):
"""

def get_favorites(contacts):
    return [contact for contact in filter(lambda contact: contact if contact['favorite'] == True else None, contacts)]


contacts = {
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}
