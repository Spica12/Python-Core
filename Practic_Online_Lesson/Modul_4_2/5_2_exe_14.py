import re

text = "Ima.Fool@iana.org Ima.Fool@iana.o Fool1@iana.org first_last@iana.org first.middle.last@iana.or a@test.com " \
       "abc111@test.com.net "


pattern = r'[\w.]+@(\w+\.)+\w{2,}'

print(re.findall(pattern, text))


def find_emails(string):
    result = list()

    pattern = r'[\w.]+@(\w+\.)+\w{2,}'

    iterator = re.finditer(pattern, string)

    for match in iterator:
        result.append(match.group())

    return result


print(find_emails(text))