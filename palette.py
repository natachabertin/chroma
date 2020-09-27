from itertools import permutations

from hex_color import HexColor


class Palette:
    """List of harmonic colors."""
    def __init__(self, *colors):
        self.colors = list()
        self._onboard_colors(colors)

    def _onboard_colors(self, colors):
        """Add colors to the palette."""
        for color_value in colors:
            onboarding_color = self._onboard_color(color_value)
            self.colors.append(onboarding_color) if onboarding_color not in self.colors else None

    def _onboard_color(self, color_value):
        """Add color to the palette, whether are
        entered as hex colors or hex values."""
        return color_value if isinstance(color_value, HexColor) else HexColor(color_value)

    def __str__(self):
        colors = [color.hex_name for color in self.colors]
        return f"Palette: {' '.join(colors)}"

    def __repr__(self):
        colors = [color.hex_name for color in self.colors]
        return f"<Palette: {' '.join(colors)}>"

    def __eq__(self, other):
        return self.colors == other.colors


class PaletteFromColor(Palette):
    """List of harmonic colors based on one color."""
    def __init__(self, color):
        super().__init__(color)

    def retrieve_matching_hues(self):
        """Generate a palette permutating triplets."""
        channels = self._get_main_color_channels()
        new_colors = list()
        for permutation in permutations(channels):
            color = ''.join(permutation)
            new_colors.append(color)

        self._onboard_colors(new_colors)

    def _get_main_color_channels(self):
        #TODO: move this to parent class and add the param main_color defaulting to 0, so you deal with self.colors[main] and can change it in multiple colors palettes
        return self.colors[0].red, self.colors[0].green, self.colors[0].blue


class DuetFromColor(Palette):
    """Given a color, get a matching one and retrieve the duet palette."""
    def __init__(self, color):
        super().__init__(color)

    def _get_main_color_channels(self):
        return self.colors[0].red, self.colors[0].green, self.colors[0].blue

    def double_highest(self):
        """Doubling the highest channel."""
        channels = self._get_main_color_channels()
        new_colors = list()
        for permutation in permutations(channels):
            color = ''.join(permutation)
            new_colors.append(color)

        self._onboard_colors(new_colors)

    def half_lowers(self):
        """Dividing the lower two channels by half."""
        channels = self._get_main_color_channels()
        new_colors = list()
        for permutation in permutations(channels):
            color = ''.join(permutation)
            new_colors.append(color)

    def choose_hue(self, hue):
        """Given the hues matching the color, return the one tending to the choosen tint."""
        channels = self._get_main_color_channels()
        new_colors = list()
        for permutation in permutations(channels):
            color = ''.join(permutation)
            new_colors.append(color)

        self._onboard_colors(new_colors)


class PaletteFromColorsList(Palette):
    """ Operations to generate palette after a list of colors. """

    def harmonic_with_others(self, color_list):
        # Mix triplets from colors in the list
        pass
