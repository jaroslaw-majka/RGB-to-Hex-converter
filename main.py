# 0. Check if the number is greater than 15
    # if True:
        # 1. Divide the decimal number by 16 using modulo operator
            # 1.1. Store the value in a list
        # 2. Divide the decimal again using floor division
            # 2.1. Take the result and check against step 0
    # if False:
        # 1. Store in a list
        # 2. Convert list elements into String and present the outcome
from typing import Tuple


def sanity_check(color):
    if color > 255:
        return 255
    elif color < 0:
        return 0
    else:
        return color


def rgb_input() -> Tuple[int, int, int]:
    r_color = sanity_check(int(input('Please provide R color: ')))
    g_color = sanity_check(int(input('Please provide G color: ')))
    b_color = sanity_check(int(input('Please provide B color: ')))
    return r_color, g_color, b_color


def hex_list_builder(rgb_colors):
    hex_container = '0123456789ABCDEF'
    hex_list = []
    # TODO Transform below code into recurrence function.
    for color in rgb_colors:
        if color > 15:
            while color != 0:
                hex_list.append(hex_container[color % 16])
                color = color // 16
        else:
            hex_list.append(hex_container[color])
    print(hex_list)


if __name__ == '__main__':
    hex_list_builder(rgb_input())
