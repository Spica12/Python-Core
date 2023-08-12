text = """
This is a sample paragraph. It contains some words, like sample, paragraph, and words.
Let's count the frequency of each word in this paragraph!
"""

stop_words = ['freq', 'stop', 'this', 'start']

def find_stop_word(text, stop_words, is_space=False):

    if is_space:
        new_text = text.split(' ')
        for word in new_text:
            for stop in stop_words:
                word = word.replace(',', '').replace('.', '').replace('!', '')
                if stop.lower() in word.lower() and len(stop) == len(word):
                    return True
    elif not is_space:
        for stop in stop_words:
            if stop.lower() in text.lower():
                return True
    else:              
        return False


print(find_stop_word(text, 'freq', is_space=True))  # False
print(find_stop_word(text, 'freq', is_space=False)) # True



