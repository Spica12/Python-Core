"""

У цьому нам допоможуть магічні методи, які відповідають 
за синтаксис with ... as ...:.

__enter__ викликається, коли інтерпретатор заходить у контекст 
          і те, що він поверне, буде записано в змінну після as;

__exit__ викликається, коли інтерпретатор виходить із блоку 
         менеджера контексту. Буде викликаний в будь-якому випадку.
"""

class Session:

    def __init__(self, addr, port=8080):
        self.connected = True
        self.addr = addr
        self.port = port

    def __enter__(self):
        print(f'connected to {self.addr}:{self.port}')

    def __exit__(self, exception_type, exception_value, traceback):
        self.connected = False
        if exception_type is not None:
            print('Some error!')
        else:
            print('No problem')


# Об'єкт класу Session буде менеджером контексту.
# Ми можемо створити його та використовувати повторно за потребою

localhost_session = Session('localhost')

with localhost_session as session:
    print(session is localhost_session)
    print(localhost_session.connected)

print(localhost_session.connected)
