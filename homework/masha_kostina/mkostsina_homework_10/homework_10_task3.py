
from functools import wraps


def calc_decorator(func):
    @wraps(func)
    def wrapper(first, second):
        if first < 0 or second < 0:
            operation = '*'
        elif first > second:
            operation = '-'
        elif first < second:
            operation = '/'
        elif first == second:
            operation = '+'

        result = func(first, second, operation)

        return result

    return wrapper


@calc_decorator
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second


first, second = map(int, input("Введите два числа: ").split())

print(calc(first, second))
