
def updating_line(line):
    num = line.split()
    print(int(num[-1]) + 10)


lines = [
    "результат операции: 42",
    "результат операции: 54",
    "результат работы программы: 209",
    "результат: 2"
]

for line in lines:
    updating_line(line)
