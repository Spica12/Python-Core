from re import sub

text = """
I’d chosen this topic because It’s a little bit more interesting than talking about a top-manager or writing a letter of complaint about a hole in my new sweater. We always decide to change something in our life, but sometimes the changes can be much more important than we expect. 
To my mind when something happens we may not understand that it is important. But in the future we will begin to understand what it means for us.
Until 2021, I worked in a managerial position.  It was the beginning of June. I thought that everything would be stable and I was preparing for my own wedding. One day I came to work and found out that we will be fired due to a reduction at work.  It was terrible for me because I liked my job.  I didn’t know what to do next. Finally I continue to work in this company but in a different position. I can’t say that it is better, but it isn’t worse. I lost touch with my colleagues, but I made new colleagues.
I have realized that I have much more free time now and I can try to use it for myself. I needed to learn English because we have started using a new program. This program has only English language. Now I am learning English for the second year and I see this progress. It’s amazing! Also in this program I need to use a programming language and write some macroses. I have understood that I like it and It’s not hard for me. Now I have started learning a programming language. But that's not all because I am going to begin working at an IT company as a Python Developer in the future. 
To sum up everything that happens in our life affects us and our decisions in the future. It has both positive and negative points, doesn’t it?
Thank you for your attention!
"""

# First step - it is normalize
normalized_text = text.lower()

# Second step - remove all symbols from text

# 1. replace
normalized_text = text.lower()
sym_to_exclude = (',', '.', '!')
for sym in sym_to_exclude:
    normalized_text.replace(sym, '')
print(normalized_text)

# 2. isalphanum()
normalized_text = text.lower()
for sym in normalized_text:
    if not sym.isalnum():
        normalized_text = normalized_text.replace(sym, '')
print(normalized_text)

# 3. sub - the best option
normalized_text = text.lower()
pattern = r'[^a-zA-Z0-9 ]'
normalized_text = sub(pattern, '', normalized_text)
print(normalized_text)

# Third step - count words, unique word, 

words_list = normalized_text.split()
unique_words_list = set(words_list)



n_words = len(words_list)
print(f'{n_words = }')



unique_words = len(set(words_list))
print(f'{unique_words = }')



words_quantity = {}
for word in unique_words_list:
    words_quantity[word] = normalized_text.count(word)

print(words_quantity)


words_quantity_list = list(words_quantity.items())


def sort_by_quantity(element):
    return element[1]


print()
words_quantity_list.sort(key=sort_by_quantity)
print(words_quantity_list)