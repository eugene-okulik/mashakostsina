
import os
from datetime import datetime, timedelta

base_path = os.path.dirname(__file__)
eugene_path = os.path.dirname(os.path.dirname(base_path))
data_path = os.path.join(eugene_path, 'eugene_okulik', 'hw_13', 'data.txt')


with open(data_path, 'r', encoding='utf-8') as data_file:
    lines = data_file.readlines()
for line in lines:
    date, task = line.strip().split(' - ')
    _, date_str = date.split(maxsplit=1)
    new_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")
    if "распечатать эту дату, но на неделю позже" in task:
        print(new_date + timedelta(weeks=1))
    elif "распечатать какой это будет день недели" in task:
        print(new_date.strftime("%A"))
    elif "распечатать сколько дней назад была эта дата" in task:
        today = datetime.now()
        delta = today - new_date
        print(delta.days, "дней назад")
