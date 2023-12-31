from collections import UserDict


contacts = [
    {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    },
    {
        "name": "Chaim Lewis",
        "email": "dui.in@egetlacus.ca",
        "phone": "(294) 840-6685",
        "favorite": False,
    },
    {
        "name": "Kennedy Lane",
        "email": "mattis.Cras@nonenimMauris.net",
        "phone": "(542) 451-7038",
        "favorite": True,
    },
    {
        "name": "Wylie Pope",
        "email": "est@utquamvel.net",
        "phone": "(692) 802-2949",
        "favorite": False,
    },
    {
        "name": "Cyrus Jackson",
        "email": "nibh@semsempererat.com",
        "phone": "(501) 472-5218",
        "favorite": True,
    },
]


class Customer(UserDict):

    def phone_info(self):
        return f"{self.get('name')} : {self.get('phone')}"

    def email_info(self):
        return f"{self.get('name')} : {self.get('email')}"
    

    customers = [Customer(element) for element in contacts]

    for customer in customers:
        print(customer.phone_info())

    for customer in customers:
        print(customer.email_info())