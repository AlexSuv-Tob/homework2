given = list(input('Введите значения списка: '))

j = 0
for i in range(int(len(given) / 2)):
    given[j], given[j + 1] = given[j + 1], given[j]
    j += 2

print(given)