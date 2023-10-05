from faker import Faker
"""
---------------------------------------------------------------------
|   Faker Method    |   Purpose                                     |
---------------------------------------------------------------------
|   name()          |   It is used to generate a fake name          |
|   address()       |   It is used to generate a fake address       |
|   email()         |   It is used to generate a fake email         |
|   url()           |   It is used to generate a fake url address   |
|   phone_number()  |   It is used to generate a fake phone number  |
|   country()       |   It is used to generate a country name       |
|   text()          |   It is used to generate a fake text          |
|   sentence()      |   It is used to generate a fake large text    |
|   date()          |   It is used to generate a dummy date value   |
|   time()          |   It is used to generate a dummy time value   |
|   year()          |   It is used to generate a dummy year value   |
---------------------------------------------------------------------
"""


fake = Faker()
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


if __name__ == '__main__':
    create_users(fake, users, n=12)
