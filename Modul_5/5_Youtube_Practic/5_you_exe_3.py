import re

# Don't work

pattern = r'^[0-2][0-5][0-5]'


ips = ['0.0.0.0',
       '0000',
       '128.10.13.41',
       '123.45.85',
       '123,123,123,123',
       '123456165243',
       '345.520.18.17']


for ip in ips:

    result = re.search(pattern, ip)

    if result is None:
        print(f'Negative - {ip}')
    else:
        print(f'Positive - {result.group()}')