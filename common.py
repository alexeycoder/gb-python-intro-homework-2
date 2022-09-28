# My Common Types and Methods Library

import os

# consts:


class escape_codes:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    ITALIC = '\033[3m'      # курсив, может не работать, в ubuntu ok
    UNDERLINE = '\033[4m'
    RED = '\033[31m'
    YELLOW = '\033[33m'
    WHITE = '\033[37m'
    CYAN = '\033[46m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'
    BG_DARK_PURPLE = '\033[48;5;90m'


# methods:

def console_clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def ask_for_repeat():
    answer = input('Желаете повторить (Y/n)? ')
    return len(answer) == 0 or answer[0].lower() == 'y'


def print_title(title):
    lines = title.split(sep='\n')
    longest_line = max(lines, key=len)
    border = len(longest_line) * '\u2550'
    print(f'{escape_codes.BRIGHT_CYAN}{escape_codes.BOLD}{border}\n{title}\n{border}{escape_codes.RESET}')


def print_error(message):
    print(f'{escape_codes.RED}\u2757 {message}{escape_codes.RESET}')


def write_highlighted(text, end='\n'):
    print(f'{escape_codes.BRIGHT_YELLOW}{text}{escape_codes.RESET}', end=end)


def write_emphasized(text, end='\n'):
    print(f'{escape_codes.BOLD}{escape_codes.ITALIC}{text}{escape_codes.RESET}', end=end)


def get_user_input_int(prompt: str, warn_nan: str, warn_out_of_range: str, func_chech_if_valid) -> int:
    not_a_number = False
    out_of_range = False
    while True:
        if not_a_number:
            not_a_number = False
            print_error(warn_nan)
        if out_of_range:
            out_of_range = False
            print_error(warn_out_of_range)

        try:
            num = int(input(prompt))
            out_of_range = not func_chech_if_valid(num)
            if not out_of_range:
                return num
        except:
            not_a_number = True


def make_decimal_separator_invariant(expected_float_str: str) -> str:
    expected_float_str = expected_float_str.replace(',', '.')
    num_of_extra_dots = expected_float_str.count('.') - 1
    if num_of_extra_dots > 0:
        expected_float_str = expected_float_str.replace(
            '.', '', num_of_extra_dots)
    return expected_float_str


def get_user_input_float(prompt: str, warn_nan: str, warn_out_of_range: str, func_chech_if_valid):
    not_a_number = False
    out_of_range = False
    while True:
        if not_a_number:
            not_a_number = False
            print_error(warn_nan)
        if out_of_range:
            out_of_range = False
            print_error(warn_out_of_range)

        try:
            inp = input(prompt)
            inp = make_decimal_separator_invariant(inp)
            num = float(inp)
            out_of_range = not func_chech_if_valid(num)
            if not out_of_range:
                return num
        except:
            not_a_number = True
