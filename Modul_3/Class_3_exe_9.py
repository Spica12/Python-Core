def to_seconds(seconds=0, minutes=0, hours=0, days=0, weeks=0):

    seconds_in_minute = 60
    seconds_in_hour = 60 * seconds_in_minute
    seconds_in_day = 24 * seconds_in_hour
    seconds_in_week = 7 * seconds_in_day

    return seconds +\
        minutes * seconds_in_minute +\
        hours * seconds_in_hour +\
        days * seconds_in_day +\
        weeks * seconds_in_week

print(to_seconds(minutes=7, hours=2, weeks=3))