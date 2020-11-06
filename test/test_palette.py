import unittest

from hex_color import HexColor
from palette import Palette, PaletteFromColor, DuetFromColor, TrioFromColor


class TestPalette(unittest.TestCase):
    def test_palette_from_hex_colors(self):
        color1 = HexColor('111')
        color2 = HexColor('222')
        res = str(Palette(color1, color2))
        self.assertEqual(res, 'Palette: #111111 #222222')

    def test_palette_from_hex_values(self):
        color1 = '111'
        color2 = '222'
        res = str(Palette(color1, color2))
        self.assertEqual(res, 'Palette: #111111 #222222')

    def test_palette_from_hex_colors_and_values_mixed(self):
        color1 = '111'
        color2 = HexColor('222')
        res = str(Palette(color1, color2))
        self.assertEqual(res, 'Palette: #111111 #222222')

    def test_palette_print(self):
        color1 = HexColor('111')
        color2 = HexColor('222')
        color3 = HexColor('333')
        res = str(Palette(color1, color2, color3))
        self.assertEqual(res, 'Palette: #111111 #222222 #333333')

    def test_palette_repr(self):
        color1 = HexColor('111')
        color2 = HexColor('222')
        color3 = HexColor('333')
        res = repr(Palette(color1, color2, color3))
        self.assertEqual(res, '<Palette HexColors: #111111 #222222 #333333>')


class TestPaletteRandomGenerate(unittest.TestCase):
    def setUp(self):
        self.palette = Palette('6081e8', '344283', '251c1e', '775a30')

    def test_retrieve_another_palette(self):
        result = self.palette.random_generate()
        self.assertFalse(all([color in self.palette.colors for color in result.colors]))  # can repeat some but not all

    def test_retrieve_same_amount_of_colors_as_default(self):
        result = self.palette.random_generate()
        self.assertEqual(len(result.colors), len(self.palette.colors))

    def test_retrieve_amount_of_colors_asked(self):
        number_of_colors = 2
        result = self.palette.random_generate(number_of_colors)
        self.assertEqual(len(result.colors), number_of_colors)


class TestPaletteFromColor(unittest.TestCase):
    def setUp(self):
        self.color = HexColor('28c')
        self.palette = PaletteFromColor(self.color)

    def test_retrieve_matching_hues(self):
        colors = ['2288cc', '22cc88', '8822cc', '88cc22', 'cc2288', 'cc8822']
        expected = [HexColor(color) for color in colors]
        self.palette.retrieve_matching_hues()
        self.assertEqual(self.palette.colors, expected)


class TestDuetFromColorChooseHue(unittest.TestCase):
    def setUp(self):
        self.color = '0af'
        self.palette = DuetFromColor(self.color)

    def test_choose_hue_if_selected_hue_is_starting_color_return_one_starting_color(self):
        self.palette.choose_hue('bg')
        self.assertEqual(self.palette, Palette(self.color))

    def test_choose_hue_red_greenish(self):
        expected_addition = 'fa0'
        self.palette.choose_hue('rg')
        self.assertEqual(self.palette, Palette(self.color, expected_addition))

    def test_choose_hue_red_blueish(self):
        expected_addition = 'f0a'
        self.palette.choose_hue('rb')
        self.assertEqual(self.palette, Palette(self.color, expected_addition))

    def test_choose_hue_green_reddish(self):
        expected_addition = 'af0'
        self.palette.choose_hue('gr')
        self.assertEqual(self.palette, Palette(self.color, expected_addition))

    def test_choose_hue_green_blueish(self):
        expected_addition = '0fa'
        self.palette.choose_hue('gb')
        self.assertEqual(self.palette, Palette(self.color, expected_addition))

    def test_choose_hue_blue_reddish(self):
        expected_addition = 'a0f'
        self.palette.choose_hue('br')
        self.assertEqual(self.palette, Palette(self.color, expected_addition))

    def test_choose_hue_blue_greenish(self):
        expected_addition = '0af'
        self.palette.choose_hue('bg')
        self.assertEqual(self.palette, Palette(self.color, expected_addition))


class TestTrioFromColorChooseHue(unittest.TestCase):
    def setUp(self):
        self.color = '0af'
        self.palette = TrioFromColor(self.color)

    def test_choose_hue_red_pair(self):
        expected_addition = ('fa0', 'f0a')
        self.palette.choose_hue('r')
        self.assertEqual(self.palette, Palette(self.color, *expected_addition))

    def test_choose_hue_green_pair(self):
        expected_addition = ('af0', '0fa')
        self.palette.choose_hue('g')
        self.assertEqual(self.palette, Palette(self.color, *expected_addition))

    def test_choose_hue_blue_pair(self):
        expected_addition = 'a0f'
        self.palette.choose_hue('b')
        self.assertEqual(self.palette, Palette(self.color, expected_addition))
