#!/usr/bin/env python3
from matplotlib import pyplot as plt

from ColorFilter import ColorFilter
cf = ColorFilter()

array = plt.imread("../resources/musk.png")
for f in [cf.to_red, cf.to_green, cf.to_blue, cf.invert]:
    plt.imshow(f(array))
    plt.show()

im = cf.to_grayscale(array, "m")
plt.imshow(im, cmap="gray")
plt.show()

im = cf.to_grayscale(array, "w", weights=[0.2126, 0.7152, 0.0722])
plt.imshow(im, cmap="gray")
plt.show()

im = cf.to_celluloid(array)
plt.imshow(im)
plt.show()
