import numpy as np


class ScrapBooker:
    def __init__(self):
        pass

    def crop(self, array, dim, position=(0, 0)):
        """Crops the image as a rectangle via dim arguments \
(being the new height and width oof the image) \
from the coordinates given by position arguments.
Args:
array: numpy.ndarray
dim: tuple of 2 integers.
position: tuple of 2 integers.
Returns:
new_arr: the cropped numpy.ndarray.
None otherwise (combinaison of parameters not incompatible).
Raises:
This function should not raise any Exception."""
        if not isinstance(array, np.ndarray):
            return None
        if not isinstance(dim, tuple)\
                or len(dim) != 2\
                or not isinstance(dim[0], int)\
                or not isinstance(dim[1], int)\
                or dim[0] < 0 or dim[1] < 0:
            return None
        if not isinstance(position, tuple)\
                or len(position) != 2\
                or not isinstance(position[0], int)\
                or not isinstance(position[1], int)\
                or position[0] < 0 or position[1] < 0:
            return None
        (x, y) = position
        (n, m) = dim
        return array[x:x + n, y:y + m]

    def thin(self, array, n, axis):
        """Deletes every n-th line pixels along the specified axis \
(0: vertical, 1: horizontal)
Args:
array: numpy.ndarray.
n: non null positive integer lower than the number of row/column of the array \
(depending of axis value).
axis: positive non null integer.
Returns:
new_arr: thined numpy.ndarray.
None otherwise (combinaison of parameters not incompatible).
Raises:
This function should not raise any Exception."""
        if not isinstance(array, np.ndarray):
            return None
        if not isinstance(n, int) or n <= 0:
            return None
        if not isinstance(axis, int) or axis not in [0, 1]:
            return None
        if axis:
            ind = [i for i in range(array.shape[0]) if (i + 1) % n]
            return array[ind]
        else:
            ind = [i for i in range(array.shape[1]) if (i + 1) % n]
            return array[:, ind]

    def juxtapose(self, array, n, axis):
        """Juxtaposes n copies of the image along the specified axis.
Args:
array: numpy.ndarray.
n: positive non null integer.
axis: integer of value 0 or 1.
Returns:
new_arr: juxtaposed numpy.ndarray.
None otherwise (combinaison of parameters not incompatible).
Raises:
This function should not raise any Exception."""
        if not isinstance(array, np.ndarray):
            return None
        if not isinstance(n, int) or n <= 0:
            return None
        if not isinstance(axis, int) or axis not in [0, 1]:
            return None
        if axis:
            return np.hstack([array] * n)
        else:
            return np.vstack([array] * n)

    def mosaic(self, array, dim):
        """Makes a grid with multiple copies of the array. \
The dim argument specifies the number of repetition along each dimensions.
Args:
array: numpy.ndarray.
dim: tuple of 2 integers.
Returns:
new_arr: mosaic numpy.ndarray.
None otherwise (combinaison of parameters not incompatible).
Raises:
This function should not raise any Exception."""
        if not isinstance(array, np.ndarray):
            return None
        if not isinstance(dim, tuple)\
                or len(dim) != 2\
                or not isinstance(dim[0], int)\
                or not isinstance(dim[1], int)\
                or dim[0] < 1 or dim[1] < 1:
            return None
        new_arr = self.juxtapose(array, dim[0], 0)
        new_arr = self.juxtapose(new_arr, dim[1], 1)
        return new_arr
