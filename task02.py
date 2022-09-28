# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

import common

# consts:

WARN_NAN = 'Некорректный ввод: введено нечисловое значение. Пожалуйста попробуйте снова.'
WARN_OUT_OF_RANGE = 'Ошибка: Число должно быть натуральным! Пожалуйста попробуйте снова.'


# methods:

def calc_fact(number):
    if number == 0:
        return 1
    fact = 1
    i = 2
    while i <= number:
        fact *= i
        i += 1
    return fact


# main flow:

user_answer = True

while(user_answer):
    common.console_clear()
    common.print_title('Формирование списка произведений чисел от 1 до N')

    n = common.get_user_input_int('Введите натуральное число N: ',
                                  WARN_NAN, WARN_OUT_OF_RANGE, lambda x: x > 0)

    lst = [calc_fact(i) for i in range(1, n+1)]

    print(f'\nВывод: {n} -> ', end='')
    common.write_highlighted(lst)

    print()
    user_answer = common.ask_for_repeat()
