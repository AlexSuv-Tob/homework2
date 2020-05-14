word = input('Введите слова через пробел').split(' ')
j = 0
for i in range(len(word)):
    print(j + 1, word[j][0:10])
    j += 1
