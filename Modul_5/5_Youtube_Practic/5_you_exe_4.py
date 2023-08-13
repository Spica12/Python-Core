
bad_words = ['bad', 'mad', 'vodka']

while True:

    user_input = input()

    for word in bad_words:
        user_input = user_input.replace(word, '*'*len(word))

    print(f'Me: {user_input}')