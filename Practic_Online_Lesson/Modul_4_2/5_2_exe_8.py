import re

string = "Exclude from this [string the groups of] characters [located between] brackets [, ]."


def clean_up(string):
    pattern = r'(\[.*?\])'
    return re.sub(pattern, '', string)

# print(re.findall(pattern, string))

print(clean_up(string))