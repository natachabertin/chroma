from itertools import permutations

from hex_color import HexColor


class Palette:
    """List of harmonic colors."""
    def __init__(self, *colors):
        self.colors = list()
        self._enter_colors(colors)

    def append_new_colors(self, *other_colors):
        new_palette = self.colors[:]
        for color_value in other_colors:
            new_palette.append(self._transform_to_color(color_value))
        self._enter_colors(new_palette)

    def _enter_colors(self, colors):
        """Add colors to the palette."""
        for color_value in colors:
            onboarding_color = self._transform_to_color(color_value)
            self.colors.append(onboarding_color) if onboarding_color not in self.colors else None

    @staticmethod
    def _transform_to_color(color_value):
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

    def get_color(self, position=0):
        return self.colors[position]

    def get_color_channels(self, position=0):
        return self.get_color(position).channels.values()

    def random_generate(self, number_of_colors=None):
        """
        Mix triplets from colors in the list,
        return a new palette with the mixed ones.
        """
        return


class PaletteFromColor(Palette):
    """List of harmonic colors based on one color."""
    def __init__(self, color):
        super().__init__(color)

    def retrieve_matching_hues(self):
        """Generate a palette permuting triplets."""
        channel_values = self.get_color_channels()
        new_colors = list()
        for permutation in permutations(channel_values):
            color = ''.join(permutation)
            new_colors.append(color)

        self._enter_colors(new_colors)


class TrioFromColor(Palette):
    """Given a color, get 2 matching ones and retrieve the trio palette."""
    def __init__(self, color):
        super().__init__(color)

    def choose_hue(self, hue):
        """Given the hues matching the color, return the one tending to the chosen tints."""
        # TODO: Change channels dict keys from red to r and get rid of this dict.
        channel_keys = dict(r='red', g='green', b='blue')

        highest_channel = channel_keys.pop(hue[0])
        middle_channel, lowest_channel = channel_keys.values()

        new_color1 = {
            highest_channel: self.get_color().get_highest_channel_value(),
            middle_channel: self.get_color().get_middle_channel_value(),
            lowest_channel: self.get_color().get_lowest_channel_value()
        }
        new_color2 = {
            highest_channel: self.get_color().get_highest_channel_value(),
            middle_channel: self.get_color().get_lowest_channel_value(),
            lowest_channel: self.get_color().get_middle_channel_value()
        }
        self.append_new_colors(new_color1, new_color2)


class DuetFromColor(Palette):
    """Given a color, get a matching one and retrieve the duet palette."""
    def __init__(self, color):
        super().__init__(color)

    def choose_hue(self, hue):
        """Given the hues matching the color, return the one tending to the chosen tints."""
        # TODO: Change channels dict keys from red to r and get rid of this dict.
        channel_keys = dict(r='red', g='green', b='blue')

        highest_channel = channel_keys.pop(hue[0])
        middle_channel = channel_keys.pop(hue[1])
        lowest_channel = channel_keys[list(channel_keys.keys())[0]]

        new_color = {
            highest_channel: self.get_color().get_highest_channel_value(),
            middle_channel: self.get_color().get_middle_channel_value(),
            lowest_channel: self.get_color().get_lowest_channel_value()
        }
        self.append_new_colors(new_color)

    def double_highest(self):
        """Doubling the highest channel."""
        channels = self.get_color_channels()
        new_colors = list()
        for permutation in permutations(channels):
            color = ''.join(permutation)
            new_colors.append(color)

        self._enter_colors(new_colors)

    def half_lowers(self):
        """Dividing the lower two channels by half."""
        channels = self.get_color_channels()
        new_colors = list()
        for permutation in permutations(channels):
            color = ''.join(permutation)
            new_colors.append(color)
