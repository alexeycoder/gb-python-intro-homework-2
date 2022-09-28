# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

import common

# consts:

WARN_NAN = 'Некорректный ввод: введено нечисловое значение. Пожалуйста попробуйте снова.'
WARN_OUT_OF_RANGE = 'Ошибка: Число должно быть натуральным! Пожалуйста попробуйте снова.'

# main flow:

user_answer = True

while(user_answer):
    common.console_clear()
    common.print_title('Подсчёт суммы заданного числа первых элементов последовательности (1 + 1/n)\u207F'
                       '\n(начиная с n = 1)')

    n = common.get_user_input_int('Введите число элементов последовательности: ',
                                  WARN_NAN, WARN_OUT_OF_RANGE, lambda x: x > 0)

    lst = [(1 + 1/i)**i for i in range(1, n+1)]

    print(f'\nПоследовательность (1 + 1/n)\u207F: ', end='')
    common.write_highlighted(', '.join([f'{item:.3g}' for item in lst]))
    print(f'Сумма первых {n} элементов = ', end='')
    common.write_highlighted(f'{sum(lst):.2f}')

    print()
    user_answer = common.ask_for_repeat()
