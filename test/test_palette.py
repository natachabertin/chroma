import unittest
# from unittest.mock import patch

from hex_color import HexColor
from palette import Palette, PaletteFromColor


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

    def test_change_hue(self):
        colors = ['2288cc', '22cc88', '8822cc', '88cc22', 'cc2288', 'cc8822']
        expected = [HexColor(color) for color in colors]
        self.palette.change_hue()
        self.assertEqual(self.palette.colors, expected)

    def test_double_highest_in_range(self):
        colors = ['2288cc', '2288ff']
        expected = [HexColor(color) for color in colors]
        self.palette.double_highest()
        self.assertEqual(self.palette.colors, expected)

    def test_double_highest_out_of_range(self):
        colors = ['2288cc', '2288ff']
        expected = [HexColor(color) for color in colors]
        self.palette.double_highest()
        self.assertEqual(self.palette.colors, expected)

    def test_half_lowers_in_range(self):
        colors = ['2288cc', '2288ff']
        expected = [HexColor(color) for color in colors]
        self.palette.half_lowers()
        self.assertEqual(self.palette.colors, expected)

    def test_half_lowers_out_of_range(self):
        colors = ['2288cc', '2288ff']
        expected = [HexColor(color) for color in colors]
        self.palette.half_lowers()
        self.assertEqual(self.palette.colors, expected)
