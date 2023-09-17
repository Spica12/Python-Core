from datetime import datetime, timedelta

cur_date = input('Enter date: ')

print(datetime.strptime(cur_date, '%d %m %Y'))