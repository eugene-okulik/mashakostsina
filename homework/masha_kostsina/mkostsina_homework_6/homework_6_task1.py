
a = input().split()
new_text = []

for i in a:
    if i[-1] == "," or i[-1] == ".":
        new_i = i[:-1] + 'ing' + i[-1]
    else:
        new_i = i + 'ing'

    new_text.append(new_i)

print(*new_text)
