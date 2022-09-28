# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

import common
import random
import os

# consts:

SETTINGS_FILE_PATH = 'file.txt'
WARN_WRONG_DATA = 'Файл ' + SETTINGS_FILE_PATH + \
    'содержит некорректные данные (нечисловые значения или ненатуральные числа).'

WARN_NAN = 'Некорректный ввод: введено нечисловое значение. Пожалуйста попробуйте снова.'

# methods:


def calc_product_of_items(source_list, positions):
    product = 1
    for pos in positions:
        product *= source_list[pos - 1]
    return product


def read_positions(file_path, warn_wrong_data):
    if not os.path.isfile(file_path):
        common.print_error(f'Не найден файл {file_path}.')
        return None

    lines = None

    try:
        text_file = open(file_path, 'r')
    except OSError as ex:
        common.print_error(
            f'Не удалось открыть файл {file_path} для чтения.\n{ex}')
        return None
    else:
        with text_file:
            lines = list(filter(None, (line.strip() for line in text_file)))
            # игнорируем пустые строки, чтобы избежать лишнего искл при конв в int
            # text_file.readlines()

    if lines is None:
        common.print_error(f'Не удалось прочитать файл {file_path}')
        return None

    if len(lines) == 0:
        common.print_error(f'Файл {file_path} не содержит данных.')
        return None

    try:
        pos_lst = list(map(int, lines))  # [int(line) for line in lines]
        if (all(pos_item > 0 for pos_item in pos_lst)):
            return pos_lst
    except:
        pass

    print(warn_wrong_data)
    return None


def create_random_list(size):
    return [random.randint(-size, size) for i in range(size)]


def set_brighter(text) -> str:
    return f'{common.escape_codes.BRIGHT_WHITE}{text}{common.escape_codes.RESET}'


def set_background(text) -> str:
    return f'{common.escape_codes.BRIGHT_WHITE}{common.escape_codes.BG_DARK_PURPLE}{common.escape_codes.BOLD}{text}{common.escape_codes.RESET}'


def print_list(lst, positions_to_highlight):
    lst_str = [(set_background(item) if (idx + 1) in positions_to_highlight
                else set_brighter(item))
               for idx, item in enumerate(lst)]
    print(', '.join(lst_str))


    # main flow:
user_answer = True

while(user_answer):
    common.console_clear()
    common.print_title(f'Вычисление произведения элементов списка на позициях, заданных в файле {SETTINGS_FILE_PATH}'
                       '\n(список формируется из N элементов, заполненных случайными числами из промежутка [-N, N])')

    positions_lst = read_positions(SETTINGS_FILE_PATH, WARN_WRONG_DATA)

    if positions_lst is None:
        user_answer = common.ask_for_repeat()
        continue

    max_pos = max(positions_lst)

    positions_as_string = ', '.join(map(str, positions_lst))
    print(f'Успешно прочитано позиций из файла: {len(positions_lst)} ({positions_as_string}).'
          f'\nКрайняя правая позиция: {max_pos}.')

    warn_out_of_range = f'Требуется ввести количество элементов не менее {max_pos}! Пожалуйста попробуйте снова.'

    n = common.get_user_input_int(f'Введите количество элементов списка (не меньше {max_pos}): ',
                                  WARN_NAN, warn_out_of_range, lambda x: x >= max_pos)

    lst = create_random_list(n)
    product = calc_product_of_items(lst, positions_lst)

    print('\nСформированный список: ', end='')
    print_list(lst, positions_lst)

    print(
        f'Произведение элементов на заданных позициях = {set_brighter(product)}')

    print()
    user_answer = common.ask_for_repeat()
