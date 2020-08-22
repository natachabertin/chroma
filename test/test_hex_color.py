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


class TestCooler(unittest.TestCase):
    def setUp(self):
        self.color = HexColor('484848')

    @patch('hex_color.HexColor._change_temperature')
    def test_positiveAmount_callsChangeTempWithNegativeSign(self, temp_changer):
        self.color.cooler(1, False)
        temp_changer.assert_called_with(-1, subtle=False)

    @patch('hex_color.HexColor._change_temperature')
    def test_negativeAmount_callsChangeTempWithPositiveSign(self, temp_changer):
        self.color.cooler(-1, False)
        temp_changer.assert_called_with(1, subtle=False)


class TestWarmer(unittest.TestCase):
    def setUp(self):
        self.color = HexColor('484848')

    @patch('hex_color.HexColor._change_temperature')
    def test_positiveAmount_callsChangeTempWithPositiveSign(self, temp_changer):
        self.color.warmer(1, False)
        temp_changer.assert_called_with(1, subtle=False)

    @patch('hex_color.HexColor._change_temperature')
    def test_negativeAmount_callsChangeTempWithNegativeSign(self, temp_changer):
        self.color.warmer(-1, False)
        temp_changer.assert_called_with(-1, subtle=False)


class TestDigitToSwitch(unittest.TestCase):
    def setUp(self):
        self.color = HexColor('484848')

    def test_subtleFalse_returnsZero(self):
        self.assertEqual(
            self.color._digit_to_switch(False), 0
        )

    def test_subtleTrue_returnsOne(self):
        self.assertEqual(
            self.color._digit_to_switch(True), 1
        )


class TestAmountChecker(unittest.TestCase):
    def setUp(self):
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
        self.assertFalse(
            self.color._is_valid_amount(10)
        )

    def test_negativeOutOfRange_returnsInvalid(self):
        self.assertFalse(
            self.color._is_valid_amount(-10)
        )

    def test_rangeLimitHighOutside_returnsValid(self):
        self.assertFalse(
            self.color._is_valid_amount(7)
        )

    def test_rangeLimitLowOutside_returnsValid(self):
        self.assertFalse(
            self.color._is_valid_amount(-1)
        )

    def test_rangeLimitHighInside_returnsValid(self):
        self.assertTrue(
            self.color._is_valid_amount(6)
        )

    def test_rangeLimitLowInside_returnsValid(self):
        self.assertTrue(
            self.color._is_valid_amount(0)
        )


class TestChangeTemperature(unittest.TestCase):
    def setUp(self):
        self.color = HexColor('484848')

    @patch('hex_color.HexColor._is_valid_amount')
    def test_validAmount_callsAmountChecker(self, amount_checker):
        self.color._change_temperature(1, False)
        amount_checker.assert_called_with(1)

    def test_invalidAmount_raisesValueError(self):
        with self.assertRaises(ValueError):
            self.color._change_temperature(10, False)

    @patch('hex_color.HexColor._digit_to_switch')
    def test_validAmount_callsDigitToSwitch(self, getDigit):
        self.color._change_temperature(1, False)
        amount_checker.assert_called_with(1)

    @patch('hex_color.HexColor._digit_to_switch')
    @patch('hex_color.HexColor._add_hex')
    def test_invalidAmount_doesntCallDigitToSwitchNorAddHex(self, add_hex, getDigit):
        self.color._change_temperature(10, False)
        getDigit.assert_not_called()
        add_hex.assert_not_called()

    @patch('hex_color.HexColor._add_hex')
    def test_validAmount_callsAddHex(self, add_hex):
        self.color._change_temperature(-1, False)
        self.assertEqual(add_hex.call_count, 1)

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


class TestAddHex(unittest.TestCase):
    def setUp(self):
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
