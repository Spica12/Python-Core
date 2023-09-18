

def func(text):
    if text in ('bad', 'mad', 'vodka', 'beer'):
        return False
    return True


words = list(filter(func, ['apple', 'vodka', 'potato', 'beer']))
print(words)    # ['apple', 'potato']


bad_words = ('bad', 'mad', 'vodka', 'beer')
words = list(filter(lambda i: i not in bad_words, ['apple', 'vodka', 'potato', 'beer']))
print(words)    # ['apple', 'potato']
