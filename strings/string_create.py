this_is_string = 'Hi there'
the_same_string = "Hi there"
print(this_is_string == the_same_string)    # True

print('-------------------------------------')

text = """The first line 
And second line
Last third line"""

song = '''Jingle bells, jingle bells
Jingle all the way
Oh, what fun it is to ride
In a one horse open sleigh'''

print('-------------------------------------')

one_line_text = "Textual data in Python is handled with str objects, or strings. Strings are immutable sequences of Unicode code points. String literals are written in a variety of ways: single quotes, double quotes, triple quoted."
print(one_line_text)


one_text_line = "Textual data in Python is handled with str objects, or strings. "\
                "Strings are immutable sequences of Unicode code points. "\
                "String literals are written in a variety of ways: single quotes, double quotes, triple quoted."
print(one_line_text)

print('-------------------------------------')

print(('spam ' 'eggs') == 'spam eggs')  # True
