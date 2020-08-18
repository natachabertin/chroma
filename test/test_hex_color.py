import unittest
from hex_color import HexColor


class TestHexColor(unittest.TestCase):

    def test__get_channels_from_paired_channels(self):
        result = HexColor('012345')
        self.assertEqual(str(result), '#012345')

    def test__get_channels_from_single_channels(self):
        result = HexColor('012')
        self.assertEqual(str(result), '#001122')

    def test__get_hex_name_returns_leading_hash(self):
        result = HexColor('012345')
        self.assertEqual(str(result)[0], '#')

    def test__get_hex_name_returns_seven_chars(self):
        result = HexColor('012345')
        self.assertEqual(len(str(result)), 7)
