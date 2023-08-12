import re

text = "Ima.Fool@iana.org Ima.Fool@iana.o Fool1@iana.org first_last@iana.org first.middle.last@iana.or a@test.com " \
       "abc111@test.com.net "


pattern = r'[\w.]+@(\w+\.)+\w{2,}'

print(re.findall(pattern, text))

pattern = r'([\w.]+@(\w+\.)+\w{2,})'

print(re.findall(pattern, text))

pattern = r'([\w.]+@(?:\w+\.)+\w{2,})'

print(re.findall(pattern, text))