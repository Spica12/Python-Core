from faker import Factory
import json

# fake = Factory.create('uk_UA')
fake = Factory.create()
users = []

def create_users(fake, users: list, n=10):
    for _ in range(n):
        user = {}
        user['name'] = fake.name()
        user['phone_number'] = fake.phone_number()
        user['email'] = fake.email()
        user['address'] = fake.address()
        user['birthday'] = fake.date()
        users.append(user)
        print(user)
    to_json(users)


def to_json(users: list):
    with open('D:\\GoIT\\Python Core\\Modul_12_Seralization_files\\5_Youtube_add\\12_you_add_3_users.json', 'w') as fh:
        json.dump(users, fh, indent=4, ensure_ascii=False)
        print('Users were saved')


if __name__ == '__main__':
    create_users(fake, users, n=120)
    