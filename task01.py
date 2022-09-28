#  Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

import common

# consts:

WARN_NAN = 'Некорректный ввод: введено нечисловое значение. Пожалуйста попробуйте снова.'


# methods:

def float_to_completed_integer(real_number: float) -> int:
    magnitude = int(1)
    temp = float(real_number)
    while not temp.is_integer():
        magnitude *= 10
        temp = real_number * magnitude
    return int(temp)


def get_digits_sum(any_number):
    no_point_number = float_to_completed_integer(any_number)
    sum = 0
    while no_point_number > 0:
        sum += no_point_number % 10
        no_point_number //= 10
    return sum


# main flow:

user_answer = True

while(user_answer):
    common.console_clear()
    common.print_title('Сумма цифр вещественного числа')

    fnum = common.get_user_input_float(
        'Введите любое число: ', WARN_NAN, None, lambda _: True)

    dsum = get_digits_sum(fnum)

    print(f'\nСумма цифр числа {fnum} = ', end='')
    common.write_highlighted(dsum)
    print()

    user_answer = common.ask_for_repeat()
