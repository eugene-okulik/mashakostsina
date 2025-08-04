
import random


def get_salary(salary):
    bonus = random.choice([True, False])
    if bonus:
        new_salary = salary + random.randrange(1, 5000)
    else:
        new_salary = salary

    return f'{salary}, {bonus} - ${new_salary}'


print(get_salary(int(input("Введите зарплату: ", ))))
