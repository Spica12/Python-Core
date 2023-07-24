text = 'afshkdjfsa sdfkSDFDFsdfhkas fsdf df sdfskdf sdfjsd sdfsdl'
alphabet = 'abcdefghijklmnoqprstuvwxyz'

# words = text.split()
# print(words)

words = []
start = 0

for index, char in enumerate(text):

    if not char.lower() in alphabet:
        # print(index, char)
        word = text[start:index]
        words.append(word.strip())
        start = index 

print(words)