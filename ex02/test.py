#!/usr/bin/env python3
import numpy as np
from ScrapBooker import ScrapBooker
spb = ScrapBooker()
arr1 = np.arange(0, 25).reshape(5, 5)
print(repr(spb.crop(arr1, (3, 1), (1, 0))))
# Output
'''
array([[ 5],
[10],
[15]])
'''
arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1, 9)
print(repr(spb.thin(arr2, 3, 0)))
# Output
'''
array([['A', 'B', 'D', 'E', 'G', 'H'],
      ['A', 'B', 'D', 'E', 'G', 'H'],
      ['A', 'B', 'D', 'E', 'G', 'H'],
      ['A', 'B', 'D', 'E', 'G', 'H'],
      ['A', 'B', 'D', 'E', 'G', 'H'],
      ['A', 'B', 'D', 'E', 'G', 'H']], dtype='<U1')
'''
arr3 = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
print(repr(spb.juxtapose(arr3, 3, 1)))
# Output
'''
array([[1, 2, 3, 1, 2, 3, 1, 2, 3],
[1, 2, 3, 1, 2, 3, 1, 2, 3],
[1, 2, 3, 1, 2, 3, 1, 2, 3]])
'''
