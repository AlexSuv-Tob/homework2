my_list = [8, 7, 5, 5, 5, 3, 2]
user_number = int(input('Введите новый элемент рейтинга: '))

#если значения нет в списке
if not my_list.count(user_number):
    #если введенное значение максимальное или минимальное
    if user_number > my_list[0]:
        my_list.insert(0, user_number)
    elif user_number < my_list[-1]:
        my_list.append(user_number)
    #если значение не MAX и не MIN и не встречается в списке
    else:
        for x, i in enumerate(my_list):
            if user_number > i:
                my_list.insert(x, user_number)
                break
#если значение есть в списке
else:
    for j, i in enumerate(my_list):
        if user_number >= i:
            my_list.insert(j, user_number)
            break

print(my_list)
