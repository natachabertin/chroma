import unittest

from hex_color import HexColor
from palette import Palette, PaletteFromColor, DuetFromColor


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
        self.assertEqual(res, '<Palette: #111111 #222222 #333333>')


class TestPaletteFromColor(unittest.TestCase):
    def setUp(self):
        self.color = HexColor('28c')
        self.palette = PaletteFromColor(self.color)

    def test_retrieve_matching_hues(self):
        colors = ['2288cc', '22cc88', '8822cc', '88cc22', 'cc2288', 'cc8822']
        expected = [HexColor(color) for color in colors]
        self.palette.retrieve_matching_hues()
        self.assertEqual(self.palette.colors, expected)

@unittest.skip("Not developed yet.")
class TestDuetFromColorChooseHue(unittest.TestCase):
    def setUp(self):
        self.color = '0af'
        self.palette = DuetFromColor(self.color)

    def test_choose_hue_red_greenish(self):
        expectedAddition = 'fa0'
        self.palette.choose_hue('rg')
        self.assertEqual(self.palette, Palette(self.color, expectedAddition))

    def test_choose_hue_red_blueish(self):
        expectedAddition = 'f0a'
        self.palette.choose_hue('rb')
        self.assertEqual(self.palette, Palette(self.color, expectedAddition))

    def test_choose_hue_green_reddish(self):
        expectedAddition = 'af0'
        self.palette.choose_hue('gr')
        self.assertEqual(self.palette, Palette(self.color, expectedAddition))

    def test_choose_hue_green_blueish(self):
        expectedAddition = '0fa'
        self.palette.choose_hue('gb')
        self.assertEqual(self.palette, Palette(self.color, expectedAddition))

    def test_choose_hue_blue_reddish(self):
        expectedAddition = 'a0f'
        self.palette.choose_hue('br')
        self.assertEqual(self.palette, Palette(self.color, expectedAddition))

    def test_choose_hue_blue_greenish(self):
        expectedAddition = '0af'
        self.palette.choose_hue('bg')
        self.assertEqual(self.palette, Palette(self.color, expectedAddition))

    def test_choose_hue_red_pair(self):
        expectedAddition = ('fa0', 'f0a')
        self.palette.choose_hue('r')
        self.assertEqual(self.palette, Palette(self.color, *expectedAddition))

    def test_choose_hue_green_pair(self):
        expectedAddition = ('af0', '0fa')
        self.palette.choose_hue('g')
        self.assertEqual(self.palette, Palette(self.color, *expectedAddition))

    def test_choose_hue_blue_pair(self):
        expectedAddition = 'a0f'
        self.palette.choose_hue('b')
        self.assertEqual(self.palette, Palette(self.color, expectedAddition))
