
temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32,
                30, 28, 24, 23]

hot_days = filter(lambda x: x > 28, temperatures)
list_of_hot_days = list(hot_days)

print(max(list_of_hot_days))
print(min(list_of_hot_days))
print(round(sum(list_of_hot_days) / len(list_of_hot_days)))
