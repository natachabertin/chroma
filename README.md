# Chroma

### A palette generator algorithm coded just for fun.
The idea came to me while reading [this article](https://www.smashingmagazine.com/2012/10/the-code-side-of-color/ "«Hex Color – The Code Side Of Color», in Smashing Magazine") about color harmony and their hexadecimal values written by [Ben Gremillion](https://twitter.com/benthinkin "@benthinkin").

Now we have a working main...only in the happy path.

Unlike the rest of the modules, the main and the web opener weren't tested nor their input's validated.
Keep in mind that we're going to open your browser on [this EXTERNAL web](http://colorcombos.com) to show the colors.


To fully understand the algorithm, you can open **[this article](https://www.smashingmagazine.com/2012/10/the-code-side-of-color/ "«Hex Color – The Code Side Of Color», in Smashing Magazine")** on which the project is based.

All the color mixes described the were covered in this repo.

* **Start with HexColor** class (in hex_color.py)
* Once you know how the colors work, **continue with Palettes** (palette.py)


### Some functionalities

#### PaletteFromColor
Given a origin color, return a palette adding matching ones.

##### Double highest & half lowers
Match a color those two ways.

#### DuetFromColor and TrioFromColor
##### Choosing harmonic hue
Receives a primary or secondary color, and returns the matching duet choosing from the matching hues the reddest | purplest | greenest | etc   

### Coming soon...
Now adding functionality to auto generate a tagged palette to be used in a design system.

#### Design System functionality
Dict with functional keys and colors as value.

* Primary, Secondary
* Dark Background, Dark Text, Dark Muted
* Light Background, Light Text, Light Muted
* Warning, Danger, Success
* etc.

