# Задача 41: Пользователь вводит с клавиатуры M чисел.
# Посчитайте, сколько чисел больше 0 ввёл пользователь.
# 0, 7, 8, -2, -2 -> 2
# 1, -7, 567, 89, 223-> 3

def positive_number(array):
    count = 0
    for i in range(0, len(array)):
        if array[i] > 0: count += 1         
    print("Количество чисел > 0 в массиве - ", count)

def get_list_on_keyboard():
    list_ok = []
    is_valid_number = False
    print("Введите целые числа (любой другой символ окончание ввода): ")
    str_number = input("Следующее число: ")
    is_valid_number = str_number.isdigit()
    if is_valid_number == True:
        list_ok.append(int(str_number))
    else:
        return list_ok
    while is_valid_number == True:
        str_number = input("Следующее число: ")
        is_valid_number = str_number.isdigit()
        if is_valid_number == True:
            list_ok.append(int(str_number))
    print("Сгенерирован массив - ", list_ok)            
    return list_ok

my_list = get_list_on_keyboard()
positive_number(my_list)
