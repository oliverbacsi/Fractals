#GENERATE FRACTAL IMAGES

> Generate colorful Fractal images of the **Mandelbrot** set and the **Julia** set.
> More info abouth the mathematical aspects is available on Wikipedia: [Mandelbrot Set](https://en.wikipedia.org/wiki/Mandelbrot_set) and [Julia Set](https://en.wikipedia.org/wiki/Julia_set)


##General preconditions

These softwares are written in **`Python`** programming language, but they also require the **`PIL`** Image Library, as well as they recommend to be run on a **256 color** capable **`ANSI`** terminal. (They were coded under linux.)


##Operation

Initially all 3 programs start up with a default colorful palette and such mathematical input conditions that produce a spectacular view of the desired Fractal types. _(Remember: the Julia set is a **chaotic system** that means the smallest alteration in the input parameters results in a completely different fractal)_.

The initial default view is calibrated so that the main body of the desired Fractal is completely shown on the available screen.


##Handling, User Interface

The programs produce and output a fractal image on the text screen (terminal screen) using 256 color ANSI escape sequences and checquered pattern special Unicode characters to fade ANSI Foreground and ANSI Background colors into each other to produce a smoothly fading color image even on the text screen.

The bottom line of the screen is some kind of status line presenting the parameters of the Fractal and the view:

* **`C`** : The constant Complex value to add at each iteration (Julia Fractals only) _(as for Mandelbrot this is the variable on the complex plane)_
* **`Rmax`** : The maximum Radius (length) of the resulting iterated complex vector to consider the whole series as being divergent (thus stop the iteration). This is the iteration treshold value.
* **`ITmax`** : The maximum number of iterations when to give up iterating and consider the whole series as being convergent.
* **`Re` _L_ _R_** : Real axis value of the Left and Right edge of the visible screen (to see where we zoomed in)
* **`Im` _B_ _T_** : Imaginary axis value of the Bottom and Top edge of the visible screen (to see where we zoomed in)

After these values there is a **`>>>`** propmt displayed waiting for Your command to enter. (This is handled via the Python `input` command, so after a command You have to hit [ENTER] to proceed.)

**Available Interactive Commands:**

* **`U`** : Walk Up 1/5 of the viewed screen : The picture slides down
* **`D`** : Walk Down 1/5 of the viewed screen : The picture slides up
* **`L`** : Walk Left 1/5 of the viewed screen : The picture slides right
* **`R`** : Walk Right 1/5 of the viewed screen : The picture slides left
* **`+`** : Zoom in 2.0x on the current view (focus point is the center of the screen)
* **`-`** : Zoom out 0.5x on the current view (focus point is the center of the screen)
* **`I`** : Export a super detailed 3840x2160 PNG image of the current view in the Screenshots/ folder **\*note1)**
* **`Q`** : Quit the program

> **\*note1)** : Currently there is only 1 way to influence the size of the exported pictures : Go to the Python codes of the respective programs, and within the last 3 program rows You will see a function invoked:  `exportImage(3840,2160)` -- edit this to have different image size.
>
> Although:  Having a smaller size like 1920x1080 will result an image with lower resolution that will still look OK on a FullHD screen, although not zoomable at all as it will immediately show pixel grains. While having a larger size image will result a very slow picture generation.
>
> You can follow up the status of the picture generation as the current picture row number will be shown on the standard output.


##Command line arguments interpreted by the programs

You can influence the initial parameters of the Fractals by specifying command line arguments.

* **`Mxxx`** : Change the Maximum number of Iterations to `xxx`. Default is 500. Higher number of iterations will result slower running speed at convergent areas (as You have to iterate them to the end to state that they are convergent). Lower values might result inaccurate results on very detailed areas (spirals or small details), so these areas will probably look not as beautiful and detailed.
* **`Vxxx`** : Change the maximum length of the iterated Vector to `xxx`. Should be a float number. This is the treshold value of the iteration. Default is 3.0
* **`Rxxx`** : Real part of the constant C value that is added at each iteration (Julia only). `xxx` should be float.
* **`Ixxx`** : Imaginary part of the constant C value that is added at each iteration (Julia only). `xxx` should be float.
* **`B`** : Switch to Black&White palette (on the ANSI screen only)


##Mathematical background

**Mandelbrot**

> The iterated formula is: `Zn+1 = Zn ^ 2 + C` , where C is the parameter taken from the X-Y location on the screen.

* Z0 = 0
* Z1 = 0 ^ 2 +C = C
* Z2 = C ^ 2 +C

So the iteration always starts from {0,0} and the generated picture shows how convergent/divergent is the iteration series if we add the complex value under the respective pixel to the series. So the screen shows the complex plane of C.

Simply put : "For each pixel of the screen: If we start our iteration from zero and add **this** value where we stand on the screen to each iteration step then how fast our iteration value would fly away to infinite or whether it will remain in the proximity of zero"

---

**Julia**

> The iterated formula is: `Zn+1 = Zn ^ 2 + C` , where C is a predefined constant complex number given at the start of the program, and the initial value of Z0 is taken from the X-Y position on the screen.

* Z0 = (defined by the position on the screen)
* Z1 = Z0 ^ 2 +C , where C is constant throughout the whole operation of the program
* ...

Simply put : "For each pixel of the screen: If we start our iteration from the value where we stand on the complex plane on the screen, and at each iteration adding a predefined C value, how fast our iteration value would fly away to infinite or whether it will remain in the proximity of zero"

Easy to see that Mandelbrot and Julia sets somehow "complement" each other: Keeping either one of Z or C constant while varying the other one by the position on the screen.

**Note** : The initial value of C has a great impact on the look and style of the Julia set varying from an amorph "blob", through spectacular dragon-shaped pictures, to distant groups of single dots.

It is called a "chaotic system", meaning that a minor change on the input value C will greatly influence the output. Therefore when specifying the initial C value try to make minimal changes to be able to follow-up the changes of the output.

---

**Julia3**

Sames as **Julia** but the formula is "cubic" instead of "square".

> Iterated formula is : `Zn+1 = Zn ^ 3 +C`

Try to have the Re and Im part of C as a relatively small negative number. The default C is {-0.41 , -0.006}

---

Have fun playing around with them, generating nice pictures.

Check out some [Screen Shots](https://github.com/oliverbacsi/Fractals/blob/master/Screenshots/)
