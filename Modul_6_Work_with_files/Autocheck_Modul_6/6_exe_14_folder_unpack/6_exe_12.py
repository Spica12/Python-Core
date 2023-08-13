"""
Функція get_credentials_users із попереднього завдання повертає нам список рядків username:password:

['andry:uyro18890D', 'steve:oppjM13LL9e']
Реалізуйте функцію encode_data_to_base64(data), яка приймає у параметрі data зазначений список, виконує кодування кожної пари username:password у формат Base64 та повертає список із закодованими парами username:password у вигляді:

['YW5kcnk6dXlybzE4ODkwRA==', 'c3RldmU6b3Bwak0xM0xMOWU=']

---------------------------------------------------------
import base64


def encode_data_to_base64(data):

"""
import base64


def encode_data_to_base64(data):
    data_base64 = list()

    for element in data:
        element_bytes = element.encode('utf-8')
        base64_bytes = base64.b64encode(element_bytes)
        data_base64.append(base64_bytes.decode('utf-8'))     

    return data_base64


users_password = ['andry:uyro18890D', 'steve:oppjM13LL9e']

users_password_base64 = encode_data_to_base64(users_password)
print(users_password_base64)