#!/usr/bin/env python3
from ScrapBooker import ScrapBooker
from ImageProcessor import ImageProcessor


sb = ScrapBooker()
imp = ImageProcessor()
arr = imp.load("../resources/42AI.png")
print(arr)
arr = sb.crop(arr, (50, 150), (50, 50))
imp.display(arr)
