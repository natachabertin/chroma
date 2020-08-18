from exceptions import DigitOutOfRange
from hex_color import HexColor
from render import Page


def sum_hex(hex_value, amount):
    dec_result = int(hex_value, base=16) + amount

    if not 0 <= dec_result < 16:
        overflow = dec_result if dec_result < 0 else dec_result - 15
        msg = f'We had to neutralize the color {overflow} units.'

        raise DigitOutOfRange(msg, overflow=overflow)

    return str(hex(dec_result))[2:]


def warmer(color, amount, subtle):
    if abs(amount) > 7:
        raise ValueError('Amount must be less than 8 units.')

    r, g, b = color[:2], color[2:4], color[4:6]
    digit = 1 if subtle else 0

    try:
        r_cool = sum_hex(r[digit], amount)
        b_cool = sum_hex(b[digit], amount * -1)
    except DigitOutOfRange as exception:
        amount = amount + exception.overflow
        r_cool = sum_hex(r[digit], amount)
        b_cool = sum_hex(b[digit], amount * -1)
        print(exception)
    return f'{r[0]}{r_cool}{g}{b[0]}{b_cool}' if subtle else f'{r_cool}{r[1]}{g}{b_cool}{b[1]}'


if __name__ == '__main__':
    Page().render()
    palette = [
        #     cooler('484848', 10, False),
        #    '484848',
        warmer('484848', 7, True)
    ]

    print(palette)
    for color in palette:
        print(HexColor(color))

    # print(HexColor('321'), HexColor('222'), HexColor('333'), HexColor('444'), HexColor('505050'),
    # HexColor('606060'))
