text = "The main search site in the world is https://www.google.com The main social network for people in the " \
        "world is https://www.facebook.com But programmers have their own social network http://github.com There " \
        "they share their code. some url to check https://www..youtube.com/ www.facebook.com https://www.app.facebook.com My site: https://krabaton.info"

alphabet = 'abcdefghijklmnoprstuvwxyz'
# print(len(alphabet))

words = list()
start = 0

for index, char in enumerate(text):
    if not char.lower() in alphabet:
        word = text[start:index]
        words.append(word.strip())
        start = index

print(words)