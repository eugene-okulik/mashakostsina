
from functools import wraps


def repeat_me(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        count = kwargs.pop('count', 1)
        result = None
        for i in range(count):
            result = func(*args, **kwargs)
        return result

    return wrapper


@repeat_me
def example(text):
    print(text)


example('print me', count=2)
