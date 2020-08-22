import unittest
from unittest.mock import patch

from exceptions import DigitOutOfRange
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


@unittest.skip('Not implemented yet.')
class TestCooler(unittest.TestCase):
    def set_up(self):
        self.color = HexColor('484848')

    @patch('hex_color.HexColor._change_temperature')
    def test_positiveAmount_callsChangeTempWithNegativeSign(self, temp_changer):
        self.color.cooler(1, False)
        temp_changer.assert_called_with('484848', -1, False)

    @patch('hex_color.HexColor._change_temperature')
    def test_negativeAmount_callsChangeTempWithPositiveSign(self, temp_changer):
        self.color.cooler(-1, False)
        temp_changer.assert_called_with('484848', 1, False)

    @patch('hex_color.HexColor._is_valid_amount')
    def test_callsAmountChecker(self, amount_checker):
        self.color.cooler(-1, False)
        amount_checker.assert_called_with(-1)

    @patch('hex_color.HexColor._change_temperature')
    def test_validAmount_callsTempChanger(self, temp_changer):
        self.color.cooler(-1, False)
        self.assertEqual(temp_changer.call_count, 1)

    @patch('hex_color.HexColor._change_temperature')
    def test_invalidAmount_doesntCallTempChanger(self, temp_changer):
        self.color.cooler(10, False)
        temp_changer.assert_not_called()

    def test_invalidAmount_raisesValueError(self):
        with self.assertRaises(ValueError):
            self.color.cooler(10, False)


@unittest.skip('Not implemented yet.')
class TestWarmer(unittest.TestCase):
    def set_up(self):
        self.color = HexColor('484848')

    @patch('hex_color.HexColor._change_temperature')
    def test_positiveAmount_callsChangeTempWithPositiveSign(self, temp_changer):
        self.color.warmer(1, False)
        temp_changer.assert_called_with('484848', 1, False)

    @patch('hex_color.HexColor._change_temperature')
    def test_negativeAmount_callsChangeTempWithNegativeSign(self, temp_changer):
        self.color.warmer(-1, False)
        temp_changer.assert_called_with('484848', -1, False)

    @patch('hex_color.HexColor._is_valid_amount')
    def test_callsAmountChecker(self, amount_checker):
        self.color.warmer(-1, False)
        amount_checker.assert_called_with('484848', 1, False)

    @patch('hex_color.HexColor._change_temperature')
    def test_validAmount_callsTempChanger(self, temp_changer):
        self.color.warmer(-1, False)
        self.assertEqual(temp_changer.call_count, 1)

    @patch('hex_color.HexColor._change_temperature')
    def test_invalidAmount_doesntCallTempChanger(self, temp_changer):
        self.color.warmer(10, False)
        temp_changer.assert_not_called()

    def test_invalidAmount_raisesValueError(self):
        with self.assertRaises(ValueError):
            self.color.warmer(10, False)


@unittest.skip('Not implemented yet.')
class TestAmountChecker(unittest.TestCase):
    def set_up(self):
        self.color = HexColor('484848')

    def test_positiveInRange_returnsValid(self):
        self.assertTrue(
            self.color._is_valid_amount(3)
        )

    def test_negativeInRange_returnsValid(self):
        self.assertTrue(
            self.color._is_valid_amount(-3)
        )

    def test_positiveOutOfRange_returnsInvalid(self):
        self.assertTrue(
            self.color._is_valid_amount(10)
        )

    def test_negativeOutOfRange_returnsInvalid(self):
        self.assertTrue(
            self.color._is_valid_amount(-10)
        )

    def test_rangeLimitHighInside_returnsValid(self):
        self.assertTrue(
            self.color._is_valid_amount(7)
        )

    def test_rangeLimitLowInside_returnsValid(self):
        self.assertTrue(
            self.color._is_valid_amount(0)
        )


@unittest.skip('Not implemented yet.')
class TestChangeTemperature(unittest.TestCase):
    def set_up(self):
        self.color = HexColor('484848')

    @patch('hex_color.HexColor._add_hex')
    def test_allInRange_addHexTwice(self, add_hex):
        self.color._change_temperature(1, False)
        self.assertEqual(add_hex.call_count, 2)

    @patch('hex_color.HexColor._add_hex')
    def test_colorOutOfRange_addHexThreeToFourTimes(self, add_hex):
        self.color._change_temperature(1, False)
        self.assertTrue(2 < add_hex.call_count < 5)

    def test_subtleTrue_shiftsOnesDigit(self):
        color = HexColor('484848')
        result = color._change_temperature(1, True)
        self.assertEqual(result, '494847')

    def test_subtleFalse_shiftsSixteensDigit(self):
        color = HexColor('484848')
        result = color._change_temperature(1, False)
        self.assertEqual(result, '584838')

    def test_returnsHexValue(self):
        color = HexColor('484848')
        result = color._change_temperature(3, True)
        self.assertEqual(result, '4b4845')

    def test_inRangeBoth_shiftFullBlueAndRed(self):
        color = HexColor('484848')
        result = color._change_temperature(1, False)
        self.assertEqual(result, '584838')

    def test_higherThanRangeRed_shiftBothSameAmount(self):
        color = HexColor('484848')
        result = color._change_temperature(10, False)
        self.assertEqual(result, '584838')

    def test_lowerThanRangeRed_shiftBothSameAmount(self):
        color = HexColor('484848')
        result = color._change_temperature(10, False)
        self.assertEqual(result, '584838')

    def test_higherThanRangeBlue_shiftBothSameAmount(self):
        color = HexColor('484848')
        result = color._change_temperature(10, False)
        self.assertEqual(result, '584838')

    def test_lowerThanRangeBlue_shiftBothSameAmount(self):
        color = HexColor('484848')
        result = color._change_temperature(10, False)
        self.assertEqual(result, '584838')

    def test_zeroAmount_doesntShift(self):
        color = HexColor('484848')
        result = color._change_temperature(0, False)
        self.assertEqual(result, '484848')


@unittest.skip('Not implemented yet.')
class TestAddHex(unittest.TestCase):
    def set_up(self):
        self.color = HexColor('484848')

    def test_returnsHexValue(self):
        self.assertEqual(self.color._add_hex('8', 3), 'b')

    def test_higherThanRange_raisesErrorWithNegativeValueToCut(self):
        with self.assertRaises(DigitOutOfRange) as out_of_range_error:
            self.color._add_hex('c', 5)
        self.assertEqual(
            out_of_range_error.exception.msg,
            'We had to neutralize the color 2 units.'
        )
        self.assertEqual(out_of_range_error.exception.overflow, -2)

    def test_lowerThanRange_raisesErrorWithPositiveValueToCut(self):
        with self.assertRaises(DigitOutOfRange) as out_of_range_error:
            self.color._add_hex('5', -6)
        self.assertEqual(
            out_of_range_error.exception.msg,
            'We had to neutralize the color 1 units.'
        )
        self.assertEqual(out_of_range_error.exception.overflow, -1)

    def test_inRangePositive_shiftFullAmount(self):
        self.assertEqual(self.color._add_hex('8', 1), 'b')

    def test_inRangeNegative_shiftFullAmount(self):
        self.assertEqual(self.color._add_hex('8', -1), 'b')

    def test_zeroAmount_doesntShift(self):
        self.assertEqual(self.color._add_hex('b', 0), 'b')
