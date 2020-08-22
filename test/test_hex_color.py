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

    def test_changeTemp_subtleTrue_shiftsOnesDigit(self):
        color = HexColor('484848')
        result = color.warmer(1, True)
        self.assertEqual(result, '494847')

    def test_changeTemp_subtleFalse_shiftsSixteensDigit(self):
        color = HexColor('484848')
        result = color.warmer(1, False)
        self.assertEqual(result, '584838')

    def test_changeTemp_returnsHexValue(self):
        color = HexColor('484848')
        result = color.warmer(3, True)
        self.assertEqual(result, '4b4845')

    def test_changeTemp_inRangeBoth_shiftFullBR(self):
        color = HexColor('484848')
        result = color.warmer(1, False)
        self.assertEqual(result, '584838')

    def test_changeTemp_higherThanRangeRed_shiftBothSameAmount(self):
        color = HexColor('484848')
        result = color.warmer(10, False)
        self.assertEqual(result, '584838')

    def test_changeTemp_lowerThanRangeRed_shiftBothSameAmount(self):
        color = HexColor('484848')
        result = color.cooler(10, False)
        self.assertEqual(result, '584838')

    def test_changeTemp_higherThanRangeBlue_shiftBothSameAmount(self):
        color = HexColor('484848')
        result = color.cooler(10, False)
        self.assertEqual(result, '584838')

    def test_changeTemp_lowerThanRangeBlue_shiftBothSameAmount(self):
        color = HexColor('484848')
        result = color.warmer(10, False)
        self.assertEqual(result, '584838')

    def test_changeTemp_zeroAmount_doesntShift(self):
        color = HexColor('484848')
        result = color.warmer(0, False)
        self.assertEqual(result, '484848')

    def test_cooler_positiveAmount_callsChangeTempWithInvertedSign(self):
        color = HexColor('484848')
        result = color.cooler(10, False)
        self.assertEqual(result, '584838')

    def test_cooler_negativeAmount_callsChangeTempWithInvertedSign(self):
        color = HexColor('484848')
        result = color.cooler(10, False)
        self.assertEqual(result, '584838')

    def test_warmer_positiveAmount_callsChangeTempWithSameSign(self):
        color = HexColor('484848')
        result = color.warmer(10, False)
        self.assertEqual(result, '584838')

    def test_warmer_negativeAmount_callsChangeTempWithSameSign(self):
        color = HexColor('484848')
        result = color.warmer(10, False)
        self.assertEqual(result, '584838')
