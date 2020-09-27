from exceptions import DigitOutOfRange


class HexColor:
    """ Given a hex value, generate a color and operate with its channels. """
    # TODO: refactor to operate over 2 digits at once with step=16 if not subtle else step=1.
    def __init__(self, hex_color):
        self.red, self.green, self.blue = self._get_channels(hex_color)
        self.hex_name = self._get_hex_name()

    @staticmethod
    def _get_channels(hex_color):
        precision = len(hex_color) // 3
        channels = [
            hex_color[precision * i:precision * (i + 1)]
            for i in range(3)
        ]
        return channels if precision == 2 else [channel * 2 for channel in channels]

    def _get_hex_name(self):
        return f'#{self.red}{self.green}{self.blue}'

    def __str__(self):
        return self.hex_name

    def __repr__(self):
        return f'<HexColor {self.hex_name}>'

    def __eq__(self, other):
        return self.hex_name == other.hex_name

    def cooler(self, amount, subtle=False):
        return self._change_temperature(-amount, subtle=subtle)

    def warmer(self, amount, subtle=False):
        return self._change_temperature(amount, subtle=subtle)

    def brightener(self, amount, subtle=False):
        return self._change_shades(amount, subtle=subtle)

    def additive_saturator(self, amount=None):
        """Upper the highest channel to get a lighter more saturated color.
        If amount negative, dulls the color."""
        return self._upper_highest(amount) if amount else self._double_highest()

    def subtractive_saturator(self, amount=None):
        """Down the lower two channels to get a darker more saturated color.
        If amount negative, dulls the color."""
        return self._lower_lowests(amount) if amount else self._half_lowests()

    @staticmethod
    def _digit_to_switch(subtle):
        return 1 if subtle else 0

    @staticmethod
    def _add_hex(hex_value, amount):
        dec_result = int(hex_value, base=16) + amount

        if not 0 <= dec_result < 16:
            overflow = -dec_result if dec_result < 0 else -(dec_result - 15)
            msg = f'We had to neutralize the color {overflow} units.'
            raise DigitOutOfRange(msg, overflow=overflow)

        return str(hex(dec_result))[2:]

    @staticmethod
    def _amount_in_valid_range(amount):
        return abs(amount) < 8

    @staticmethod
    def _all_colors_can_be_switched(red, green, blue):
        return all(
                0 < int(val, base=16) < 15
                for val in [red, green, blue]
        )

    def _upper_highest(self, amount):
        # Todo: refactor rgb attrs to dict color:value to avoid self.dict ugliness.
        highest_channel = max(self.__dict__, key=self.__dict__.get)
        highest_channel_value = self.__dict__[highest_channel]
        digit_to_update = self.__dict__[highest_channel][0]
        try:
            updated_digit = self._add_hex(digit_to_update, amount)
        except DigitOutOfRange:
            updated_digit = 'f'
        self.__dict__[highest_channel] = f'{updated_digit}{highest_channel_value[1]}'
        self.hex_name = self._get_hex_name()
        return self.hex_name

    def _double_highest(self):
        highest_channel = max(self.__dict__, key=self.__dict__.get)
        highest_channel_value = self.__dict__[highest_channel]
        digit_to_update = self.__dict__[highest_channel][0]
        try:
            amount = int(digit_to_update, base=16)
            updated_digit = self._add_hex(digit_to_update, amount)
        except DigitOutOfRange:
            updated_digit = 'f'
        self.__dict__[highest_channel] = f'{updated_digit}{highest_channel_value[1]}'
        self.hex_name = self._get_hex_name()
        return self.hex_name

    def _half_lowests(self):
        lowest_channels = [ch for ch in self.__dict__ if (ch != max(self.__dict__, key=self.__dict__.get) and ch != 'hex_name')]
        for channel in lowest_channels:
            lowest_channel_value = self.__dict__[channel]
            digit_to_update = self.__dict__[channel][0]
            try:
                amount = round(int(digit_to_update, base=16)/2)
                updated_digit = self._add_hex(digit_to_update, -amount)
            except DigitOutOfRange:
                updated_digit = '0'
            self.__dict__[channel] = f'{updated_digit}{lowest_channel_value[1]}'
        self.hex_name = self._get_hex_name()
        return self.hex_name

    def _lower_lowests(self, amount):
        # Todo: refactor rgb attrs to dict color:value to avoid self.dict ugliness.
        lowest_channels = [ch for ch in self.__dict__ if (ch != max(self.__dict__, key=self.__dict__.get) and ch != 'hex_name')]
        for channel in lowest_channels:
            lowest_channel_value = self.__dict__[channel]
            digit_to_update = self.__dict__[channel][0]
            try:
                updated_digit = self._add_hex(digit_to_update, -amount)
            except DigitOutOfRange:
                updated_digit = '0'
            self.__dict__[channel] = f'{updated_digit}{lowest_channel_value[1]}'
        self.hex_name = self._get_hex_name()
        return self.hex_name

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

        Raise:
        ------
        ValueError
            If value is out of 0-16 range.
        """
        if self._amount_in_valid_range(amount):
            digit = self._digit_to_switch(subtle)
            try:
                new_r = self._add_hex(self.red[digit], amount)
                new_b = self._add_hex(self.blue[digit], -amount)
            except DigitOutOfRange as exception:
                amount = amount + exception.overflow
                new_r = self._add_hex(self.red[digit], amount)
                new_b = self._add_hex(self.blue[digit], -amount)
            # TODO: Refact calculations result so it edits the same color values (and hexname) to actually modify the color instead of returning a new one.
            return f'{self.red[0]}{new_r}{self.green}{self.blue[0]}{new_b}' if subtle else f'{new_r}{self.red[1]}{self.green}{new_b}{self.blue[1]}'
        else:
            raise ValueError('Amount must be less than 8 units.')

    def _change_shades(self, amount, subtle=False):
        """
        Moves all the channels in the same directions.
        This lower or raise the brightness, while lowering saturation.
        This way, color doesn't loss its essence.

        Params:
        -------
        amount : int
            Number of units to shift the digit. Mandatory.
            Limit: if some channel arrives to the end, the left ones moves until the same amount to preserve harmony.
        subtle : bool
            Shifts the ones digit if true. Otherwise shifts the sixteens. Optional; false default.
        """
        digit = self._digit_to_switch(subtle)
        step = 1 if amount > 0 else -1
        red, green, blue = self.red[digit], self.green[digit], self.blue[digit]

        while abs(amount) > 0 and self._all_colors_can_be_switched(red, green, blue):
            red = self._add_hex(red, step)
            green = self._add_hex(green, step)
            blue = self._add_hex(blue, step)
            amount -= step

        return f'{self.red[0]}{red}{self.green[0]}{green}{self.blue[0]}{blue}' if subtle else f'{red}{self.red[1]}{green}{self.green[1]}{blue}{self.blue[1]}'
