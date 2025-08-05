
import datetime

my_date = "Jan 15, 2023 - 12:05:33"

new_date = datetime.datetime.strptime(my_date, '%b %d, %Y - %H:%M:%S')

print(new_date.strftime('%B'))
print(new_date.strftime('%d.%m.%Y, %H:%M'))
