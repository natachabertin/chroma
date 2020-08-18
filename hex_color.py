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
        return self.hex_name

    def _get_hex_name(self):
        return f'#{self.red}{self.green}{self.blue}'

    # def _change_temp(self, amount, subtle=False, warmer=False):
    #     """
    #     Moves red and blue channels in opposed directions, keeping green one equal for consistency.
    #
    #     Params:
    #     -------
    #     amount : int
    #         Number of units to shift the digit. Mandatory.
    #         Limit: if some channel arrives to the end, the other moves until the same amount to preserve harmony.
    #     subtle : bool
    #         Shifts the ones digit if true. Otherwise shifts the sixteens. Optional; false default.
    #     warmer : bool
    #         Shifts red up and blue down if true. Optional, cooler default.
    #     """
    #     return f'#{self.red}{self.green}{self.blue}'
