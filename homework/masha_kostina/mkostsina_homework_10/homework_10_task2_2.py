
from functools import wraps


def repeat_me(count=2):
    def my_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for i in range(count):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return my_decorator


@repeat_me(count=2)
def example(text):
    print(text)


example('print me')
