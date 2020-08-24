from exceptions import DigitOutOfRange

class HexColor:
    """ Given a hex value, generate a color and operate with its channels. """
    def __init__(self, hex_color):
        self.red, self.green, self.blue = self._get_channels(hex_color)
        self.hex_name = self._get_hex_name()

    def _get_channels(self, hex_color):
        precision = len(hex_color) // 3
        channels = [
            hex_color[precision * i:precision * (i + 1)]
            for i in range(3)
        ]
        return channels if precision == 2 else [channel * 2 for channel in channels]

    def __str__(self):
        return self.hex_name

    def __repr__(self):
        return f'<HexColor {self.hex_name}>'

    def _get_hex_name(self):
        return f'#{self.red}{self.green}{self.blue}'

    def cooler(self, amount, subtle=False):
        return self._change_temperature(-amount, subtle=subtle)

    def warmer(self, amount, subtle=False):
        return self._change_temperature(amount, subtle=subtle)

    def _digit_to_switch(self, subtle):
        return 1 if subtle else 0

    def _is_valid_amount(self, amount):
        return abs(amount) < 8

    def _add_hex(self, hex_value, amount):
        dec_result = int(hex_value, base=16) + amount

        if not 0 <= dec_result < 16:
            overflow = -dec_result if dec_result < 0 else -(dec_result - 15)
            msg = f'We had to neutralize the color {overflow} units.'
            raise DigitOutOfRange(msg, overflow=overflow)

        return str(hex(dec_result))[2:]

    def _change_temperature(self, amount, subtle=False):
        """
        Moves red and blue channels in opposed directions, keeping green one equal for consistency.

        Params:
        -------
        amount : int
            Number of units to shift the digit. Mandatory.
            Limit: if some channel arrives to the end, the other moves until the same amount to preserve harmony.
        subtle : bool
            Shifts the ones digit if true. Otherwise shifts the sixteens. Optional; false default.
        """
        if self._is_valid_amount(amount):
            digit = self._digit_to_switch(subtle)
            new_red_digit = self._add_hex(self.red[digit], amount)
            new_blue_digit = self._add_hex(self.blue[digit], -amount)
        else:
            raise ValueError('Amount must be less than 8 units.')
