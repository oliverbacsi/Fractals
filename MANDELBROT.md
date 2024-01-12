###MANDELBROT GENERATION

> In pseudocode, this algorithm would look as follows.
> The algorithm does not use complex numbers and manually simulates complex-number operations using two real numbers, for those who do not have a complex data type.
> The program may be simplified if the programming language includes complex-data-type operations.

```python
# for each pixel (Px, Py) on the screen do
    x0 = "scaled x coordinate of pixel (scaled to lie in the Mandelbrot X scale (-2.00, 0.47))"
    y0 = "scaled y coordinate of pixel (scaled to lie in the Mandelbrot Y scale (-1.12, 1.12))"
    x = 0.0
    y = 0.0
    iteration = 0
    max_iteration = 1000
    while x*x + y*y <= 2*2 and iteration < max_iteration :
        xtemp = x*x - y*y + x0
        y = 2*x*y + y0
        x = xtemp
        iteration += 1
    color = palette[iteration]
    plot(Px, Py, color)
```

Here, relating the pseudocode to **c**, **z** and **f~c~** :

* **z** = **x** + **i** \* **y**
* **z^2^** = **x^2^** + **i** \* 2 \* **xy** − **y^2^**
* **c** = **x~0~** + **i** \* **y~0~**

and so, as can be seen in the pseudocode in the computation of x and y:

* **x** = _Re_(**z^2^** + **c**) = **x^2^** − **y^2^** + **x~0~**
* **y** = _Im_(**z^2^** + **c**) = 2 \* **xy** + **y~0~**

To get colorful images of the set, the assignment of a color to each value of the number of executed iterations can be made using one of a variety of functions (linear, exponential, etc.).
