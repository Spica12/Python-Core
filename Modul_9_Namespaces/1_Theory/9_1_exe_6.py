# Карування


# def greeting(greet, name):
#     print(f'{greet}, {name}')


# greeting('Hello', 'Vitalii')


def greeting(greet):

    def inner(name):
        print(f'{greet}, {name}')

    return inner


new_greeting = greeting('Hello')

new_greeting('Vitalli')
new_greeting('Sam')