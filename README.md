# Chroma

### A palette generator algorithm coded just for fun.
The idea came to me while reading [this article](https://www.smashingmagazine.com/2012/10/the-code-side-of-color/ "«Hex Color – The Code Side Of Color», in Smashing Magazine") about color harmony and their hexadecimal values written by [Ben Gremillion](https://twitter.com/benthinkin "@benthinkin").

Now adding functionality to auto generate a tagged palette to be used in a design system.  

### In development

#### DuetFromColor
Given a origin color, return a duet palette adding a matching one.

##### Double highest & half lowers
Return a duet with matching color

##### Choosing harmonic hue
Receives a primary or secondary color, and returns the matching duet choosing from the matching hues the reddest | purplest | greenest | etc   

#### Design System functionality
Dict with functional keys and colors as value.

* Primary, Secondary
* Dark Background, Dark Text, Dark Muted
* Light Background, Light Text, Light Muted
* Warning, Danger, Success
* etc

