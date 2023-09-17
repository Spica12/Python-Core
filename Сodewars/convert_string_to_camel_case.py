"""
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"

"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

"The_Stealth-Warrior" gets converted to "TheStealthWarrior"
"""

def to_camel_case(text):
    new_string =''
    text = text.replace('_', ' ').replace('-', ' ').split()

    for indx, word in enumerate(text):
        
        if indx == 0:
            new_string += word
        else:
            new_string += word.capitalize()

    return new_string


print(to_camel_case('the-stealth-warrior'))
print(to_camel_case('The_Stealth_Warrior'))
print(to_camel_case('The_Stealth-Warrior'))
