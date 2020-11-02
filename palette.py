from itertools import permutations

from hex_color import HexColor


class Palette:
    """List of harmonic colors."""
    def __init__(self, *colors):
        self.colors = list()
        self._enter_colors(colors)

    def append_new_color(self, other_color):
        new_palette = self.colors[:]
        new_palette.append(self._transform_to_color(other_color))
        self._enter_colors(new_palette)

    def _enter_colors(self, colors):
        """Add colors to the palette."""
        for color_value in colors:
            onboarding_color = self._transform_to_color(color_value)
            self.colors.append(onboarding_color) if onboarding_color not in self.colors else None

    def _transform_to_color(self, color_value):
        """Add color to the palette, whether are
        entered as hex colors or hex values."""
        return color_value if isinstance(color_value, HexColor) else HexColor(color_value)

    def __str__(self):
        colors = [str(color) for color in self.colors]
        return f"Palette: {' '.join(colors)}"

    def __repr__(self):
        colors = [str(color) for color in self.colors]
        return f"<Palette HexColors: {' '.join(colors)}>"

    def __eq__(self, other):
        return self.colors == other.colors

    def get_main_color(self):
        return self.colors[0]

    def get_main_color_channels(self):
        return self.get_main_color().channels.values()


class PaletteFromColor(Palette):
    """List of harmonic colors based on one color."""
    def __init__(self, color):
        super().__init__(color)

    def retrieve_matching_hues(self):
        """Generate a palette permuting triplets."""
        channel_values = self.get_main_color_channels()
        new_colors = list()
        for permutation in permutations(channel_values):
            color = ''.join(permutation)
            new_colors.append(color)

        self._enter_colors(new_colors)


class DuetFromColor(Palette):
    """Given a color, get a matching one and retrieve the duet palette."""
    def __init__(self, color):
        super().__init__(color)

    def choose_hue(self, hue):
        """Given the hues matching the color, return the one tending to the chosen tints."""
        # TODO: Change channels dict keys from red to r and get rid of this dict.
        CHANNEL_KEYS = dict(r='red', g='green', b='blue')

        highest_channel = CHANNEL_KEYS.pop(hue[0])
        middle_channel = CHANNEL_KEYS.pop(hue[1])
        lowest_channel = CHANNEL_KEYS[list(CHANNEL_KEYS.keys())[0]]

        new_color = {
            highest_channel: self.get_main_color().get_highest_channel_value(),
            middle_channel: self.get_main_color().get_middle_channel_value(),
            lowest_channel: self.get_main_color().get_lowest_channel_value()
        }
        self.append_new_color(new_color)

    def double_highest(self):
        """Doubling the highest channel."""
        channels = self.get_main_color_channels()
        new_colors = list()
        for permutation in permutations(channels):
            color = ''.join(permutation)
            new_colors.append(color)

        self._enter_colors(new_colors)

    def half_lowers(self):
        """Dividing the lower two channels by half."""
        channels = self.get_main_color_channels()
        new_colors = list()
        for permutation in permutations(channels):
            color = ''.join(permutation)
            new_colors.append(color)


class PaletteFromColorsList(Palette):
    """ Operations to generate palette after a list of colors. """

    def harmonic_with_others(self, color_list):
        # Mix triplets from colors in the list
        pass
