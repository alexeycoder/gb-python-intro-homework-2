# Реализуйте алгоритм перемешивания списка.

import random
import common

# consts:

WARN_NAN = 'Некорректный ввод: введено нечисловое значение. Пожалуйста попробуйте снова.'
WARN_OUT_OF_RANGE = 'Ошибка: Количество элементов должно быть натуральным числом! Пожалуйста попробуйте снова.'


def swap_items(lst: list, index_a, index_b):
    temp = lst[index_a]
    lst[index_a] = lst[index_b]
    lst[index_b] = temp


def shuffle_list(lst: list):
    last_index = len(lst) - 1
    if last_index < 1:
        return

    for idx in range(last_index + 1):
        swap_with_idx = random.randint(0, last_index)
        swap_items(lst, idx, swap_with_idx)


def generate_alphabet_list(list_length):
    resulted_lst = []

    idx_la = ord('a')  # 97
    idx_lz = ord('z')  # 122
    idx_ua = ord('A')  # 65
    idx_uz = ord('Z')  # 90
    cur_char_idx = idx_la
    i = 0
    while i < list_length:
        i += 1
        resulted_lst.append(chr(cur_char_idx))
        if cur_char_idx == idx_lz:
            cur_char_idx = idx_ua
        elif cur_char_idx == idx_uz:
            cur_char_idx = idx_la
        else:
            cur_char_idx += 1
    return resulted_lst


# main flow:

user_answer = True

while(user_answer):
    common.console_clear()
    common.print_title('Реализация алгоритма перемешивания списка'
                       '\n(демонстрация на примере исходного списка с упорядочеными элементами)')
    n = common.get_user_input_int('Введите количество элементов списка: ',
                                  WARN_NAN, WARN_OUT_OF_RANGE, lambda x: x > 0)

    common.write_emphasized('\nПример I')

    list_to_shuffle = list(range(-n//2 + 1, -n//2 + n + 1))
    print('\nИсходный список:')
    print(list_to_shuffle)
    print('\nСписок после перемешивания:')
    shuffle_list(list_to_shuffle)
    print(list_to_shuffle)

    common.write_emphasized('\nПример II')

    list_to_shuffle = generate_alphabet_list(n)
    print('\nИсходный список:')
    print(list_to_shuffle)
    print('\nСписок после перемешивания:')
    shuffle_list(list_to_shuffle)
    print(list_to_shuffle)

    print()
    user_answer = common.ask_for_repeat()
