
def fibonacci(limit=100000):
    a, b = 0, 1
    count = 0
    while count <= limit:
        yield a
        a, b = b, a + b
        count += 1

indexes = {4, 199, 999, 99999}


for i, num in enumerate(fibonacci()):
    if i in indexes:
        print(num)
    if i > max(indexes):
        break

