# Chroma

### A palette generator algorithm coded just for fun.
The idea came to me while reading [this article](https://www.smashingmagazine.com/2012/10/the-code-side-of-color/ "«Hex Color – The Code Side Of Color», in Smashing Magazine") about color harmony and their hexadecimal values written by [Ben Gremillion](https://twitter.com/benthinkin "@benthinkin").

## How to review the code?
In order to guide yourself through the code, **use the next guide or the tests** and _not the main.py file_.
The project is in development, so maybe the forgotten main is a little (?) untidy.

#### Not the main. Most of the file is deprecated.
It started as a render to test the prototype of the algorithm (you can see the repeated functions that I need to clean some day), **now is just a render in order to manually generate the colors (front end is next, when I step into React!)**.

### So, where to start?
You can **import the modules** or **use the tests** to analyze it (this was done with TDD, so all the paths should be covered!).

To fully understand the algorithm, you can open **[this article](https://www.smashingmagazine.com/2012/10/the-code-side-of-color/ "«Hex Color – The Code Side Of Color», in Smashing Magazine")** on which the project is based.


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

