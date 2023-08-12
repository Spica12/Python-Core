import re

string = "Exclude from this [string the groups of] characters [located between] brackets [, ]."

pattern = r'(\[.*?\])'

print(re.findall(pattern, string))

