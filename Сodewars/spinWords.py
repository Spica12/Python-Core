"""
Write a function that takes in a string of one or more words, and 
returns the same string, but with all five or more letter words 
reversed (Just like the name of this Kata). Strings passed in 
will consist of only letters and spaces. Spaces will be included 
only when more than one word is present.

Examples:

spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
spinWords( "This is a test") => returns "This is a test" 
spinWords( "This is another test" )=> returns "This is rehtona 
test"
"""

def spinWords(sentence):

    count = 0
    text = ['']

    for char in sentence:
        # print(count, char)

        if char == ' ':
            count += 2
            text.append(' ')
            text.append('')
        else:
            text[count] += char

    # print(text)

    i = 0
    new_sentence = ''
    for word in text:
        # print(word)
        
        if len(word) >= 5:
            new_sentence += word[::-1]
        else:
            new_sentence += word
    
        i += 1

    return new_sentence


print("Hey fellow warriors", '-->', spinWords("Hey fellow warriors"))
print("his is a test", '-->', spinWords("his is a test"))
print("This is another test", '-->', spinWords("This is another test"))
