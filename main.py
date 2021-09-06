# 0. Check if the number is greater than 16
    # if True:
        # 1. Divide the decimal number by 16 using modulo operator
            # 1.1. Store the value in a list
        # 2. Divide the decimal again using floor division
            # 2.1. Take the result and check against step 0
    # if False:
        # 1. Store in a list
        # 2. Convert list elements into String and present the outcome

def sanity_check(color):
    if color > 255:
        return 255
    elif color < 0:
        return 0
    else:
        return color


if __name__ == '__main__':
    r_color = int(input('Please provide R color: '))
    g_color = int(input('Please provide G color: '))
    b_color = int(input('Please provide B color: '))
