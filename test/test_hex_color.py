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
            self.color._is_valid_amount(8)
        )

    def test_rangeLimitLowOutside_returnsValid(self):
        self.assertFalse(
            self.color._is_valid_amount(-8)
        )

    def test_rangeLimitHighInside_returnsValid(self):
        self.assertTrue(
            self.color._is_valid_amount(7)
        )

    def test_rangeLimitLowInside_returnsValid(self):
        self.assertTrue(
            self.color._is_valid_amount(0)
        )


class TestChangeTemperature(unittest.TestCase):
    def setUp(self):
        self.color = HexColor('484848')

    @patch('hex_color.HexColor._is_valid_amount', return_value=False)
    def test_invalidAmount_raisesValueError(self, amount_checker):
        with self.assertRaises(ValueError):
            self.color._change_temperature(10, subtle=False)

    @patch('hex_color.HexColor._digit_to_switch')
    @patch('hex_color.HexColor._is_valid_amount', return_value=True)
    def test_validAmount_callsDigitsToSwitch(self, amount_checker, get_digit):
        self.color._change_temperature(1, subtle=False)
        get_digit.assert_called_with(False)

    @patch('hex_color.HexColor._add_hex')
    @patch('hex_color.HexColor._digit_to_switch', return_value=0)
    @patch('hex_color.HexColor._is_valid_amount', return_value=True)
    def test_validAmount_callsAddHex(self, amount_checker, get_digit, add_hex):
        self.color._change_temperature(-1, subtle=False)
        self.assertTrue(add_hex.call_count > 0)

    @patch('hex_color.HexColor._add_hex')
    def test_allInRange_addHexTwice(self, add_hex):
        self.color._change_temperature(1, subtle=False)
        self.assertEqual(add_hex.call_count, 2)

    def test_zeroAmount_doesntShift(self):
        result = self.color._change_temperature(0, subtle=False)
        self.assertEqual(result, '484848')

    def test_subtleTrue_shiftsOnesDigit(self):
        result = self.color._change_temperature(1, subtle=True)
        self.assertEqual(result, '494847')

    def test_subtleFalse_shiftsSixteensDigit(self):
        result = self.color._change_temperature(1, subtle=False)
        self.assertEqual(result, '584838')

    def test_returnsHexValue(self):
        result = self.color._change_temperature(3, subtle=True)
        self.assertEqual(result, '4b4845')

    def test_inRangeBoth_shiftFullBlueAndRed(self):
        result = self.color._change_temperature(1, subtle=False)
        self.assertEqual(result, '584838')


class TestAddHex(unittest.TestCase):
    def setUp(self):
        self.color = HexColor('484848')

    def test_inRangePositive_shiftFullAmount(self):
        self.assertEqual(self.color._add_hex('8', 3), 'b')

    def test_inRangeNegative_shiftFullAmount(self):
        self.assertEqual(self.color._add_hex('8', -1), '7')

    def test_zeroAmount_doesntShift(self):
        self.assertEqual(self.color._add_hex('b', 0), 'b')

    def test_returnsHexValue(self):
        self.assertEqual(self.color._add_hex('8', 3), 'b')

    def test_higherThanRange_raisesErrorWithNegativeValueToCut(self):
        with self.assertRaises(DigitOutOfRange) as out_of_range_error:
            self.color._add_hex('c', 5)
        self.assertEqual(
            out_of_range_error.exception.msg,
            'We had to neutralize the color -2 units.'
        )
        self.assertEqual(out_of_range_error.exception.overflow, -2)

    def test_lowerThanRange_raisesErrorWithPositiveValueToCut(self):
        with self.assertRaises(DigitOutOfRange) as out_of_range_error:
            self.color._add_hex('5', -6)
        self.assertEqual(
            out_of_range_error.exception.msg,
            'We had to neutralize the color 1 units.'
        )
        self.assertEqual(out_of_range_error.exception.overflow, 1)


class TestIntegration(unittest.TestCase):
    def test_higherThanRangeRed_shiftBothSameAmount(self):
        result = HexColor('c84848')._change_temperature(5, subtle=False)
        self.assertEqual(result, 'f84818')

    def test_lowerThanRangeRed_shiftBothSameAmount(self):
        result = HexColor('484848')._change_temperature(-5, subtle=False)
        self.assertEqual(result, '084888')

    def test_higherThanRangeBlue_shiftBothSameAmount(self):
        result = HexColor('3848c8')._change_temperature(-5, subtle=False)
        self.assertEqual(result, '0848f8')

    def test_lowerThanRangeBlue_shiftBothSameAmount(self):
        result = HexColor('c84838')._change_temperature(5, subtle=False)
        self.assertEqual(result, 'f84808')

    def test_inverselyOutOfRangeBoth_shiftBothSameAmount(self):
        result = HexColor('e81')._change_temperature(5, subtle=False)
        self.assertEqual(result, 'fe8801')

    @unittest.skip('Weird loop goes eternal')
    def test_outOfRangeBothErrorGoesDeep_endsWithoutEternalLoop(self):
        result = HexColor('ccc')._change_temperature(-5, subtle=False)
        self.assertEqual(result, 'fe8801')
