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
    for color in rgb_colors:
        if color > 15:
            hex_list.append(hex_container[(color // 16) % 16] + hex_container[color % 16])
        else:
            hex_list.append('0' + hex_container[color])
    return hex_list


def output_formatter():
    return '#' + ''.join([notation for notation in hex_list_builder(rgb_input())])


if __name__ == '__main__':
    print(output_formatter())
