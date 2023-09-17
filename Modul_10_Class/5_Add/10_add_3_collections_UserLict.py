from collections import UserDict, UserList


class Phones(UserList):

    def set_phone(self, phone):

        if len(phone) == 12:
            new_phone = '+' + phone
        elif len(phone) < 12:
            new_phone = '+38' + phone
        
        self.data.append(new_phone)

    def get_phones(self):
        return self.data
    


phone_list = Phones()

phone_list.set_phone('09845612312')
phone_list.set_phone('380631257896')

print(phone_list.get_phones())      # ['+3809845612312', '+380631257896']

# {'name': name, 'phones': [phone, phone, phone]}