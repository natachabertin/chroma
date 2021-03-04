from exceptions import DigitOutOfRange
from hex_color import HexColor
from palette import PaletteFromColor, DuetFromColor, TrioFromColor, Palette
from render import ComboTest

def main():


    # Command line script to make a working example in the main.
    # If you're a recruiter looking for good code practices, avoid this example main and please check the tests and the palette/hex_color modules.
    # Validations in progress. This main is not tested either. Only the modules.

    print("JUST A WARN: This script is gonna open in your browser the EXTERNAL web page colorcombos.com in order to show you the colors. You can close the program to avoid it or follow the rules to continue.")
    colorValue = input('Insert a hex color value...')
    color = HexColor(colorValue)
    print(f"{color} is nice!")

    ComboTest(Palette(color)).show()
    print(f"Let's create a Palette from {color}.")
    input('Press enter to continue...')
    palette = PaletteFromColor(color)
    palette.retrieve_matching_hues()

    ComboTest(palette).show()

    print("- "* 10)
    print(f"""Now let's get from your color, three matching ones.
    You'll get your color and two matching more, towards the selected hue.
    
    (If you repeat a channel value, you're going to get less than three, because of the permutation algorithm.)
    
    Choose towards which tone you want to go:
    For example, if you want two blue-ish colors matching yours, write 'b'.
    
    The validation is in progress, so keep in mind that the accepted values are:
    r, g and b (no caps).
    """)

    toneValue = input('Insert r, g or b...')

    trio = TrioFromColor(color)
    trio.choose_hue(toneValue)

    ComboTest(trio).show()


    print("- "* 10)
    print(f"""What about being more precise? Let's create a duo from your color.
    You'll get your color and a matching one towards the selected hues.
    
    (If you repeat a channel value, you may get only one, because of the permutation algorithm.)
    
    For example, if you want two red-greenish colors matching yours, write 'rg'.
    The validation is in progress, so keep in mind that the accepted values are:
    rb, gr, gb, br, bg, rg (no caps nor spaces, but they can be in any order).  
    """)

    toneValues = input('Insert two color initials... E.g.: rb')

    duet = DuetFromColor(color)
    duet.choose_hue(toneValues)
    ComboTest(duet).show()

    print("= "* 10)
    print(f"""Now let's play modifying your selected color:
    If we upper the highest channel we get a lighter more saturated color.
    If amount negative, dulls the color.  
    
    Raises an error if the value is > 8. ANd if one of the values reach the max/min, the other one stops in order to get a matching color and not a random one.
    """)

    amountSatChange = input('Insert the amount to change the saturation... E.g.: -4')

    new_color = HexColor(colorValue)
    new_color.additive_saturator(int(amountSatChange))
    satPalette = Palette(color, new_color)
    ComboTest(satPalette).show()

if __name__ == '__main__':
    main()
