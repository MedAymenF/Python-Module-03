#!/usr/bin/env python3
from ScrapBooker import ScrapBooker
from ImageProcessor import ImageProcessor


sb = ScrapBooker()
imp = ImageProcessor()
arr = imp.load("../resources/42AI.png")
print(arr)
arr = sb.thin(arr, 3, 1)
imp.display(arr)
