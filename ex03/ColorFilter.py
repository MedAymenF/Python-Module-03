import numpy as np


class ColorFilter:
    @staticmethod
    def invert(array):
        """Inverts the color of the image received as a numpy array.
Args:
array: numpy.ndarray corresponding to the image.
Return:
array: numpy.ndarray corresponding to the transformed image.
None: otherwise.
Raises:
This function should not raise any Exception."""
        if not isinstance(array, np.ndarray):
            return None
        new_arr = array[:, :, :3]
        return 1 - new_arr

    @staticmethod
    def to_blue(array):
        """Applies a blue filter to the image received as a numpy array.
Args:
array: numpy.ndarray corresponding to the image.
Return:
array: numpy.ndarray corresponding to the transformed image.
None: otherwise.
Raises:
This function should not raise any Exception."""
        if not isinstance(array, np.ndarray):
            return None
        new_arr = array[:, :, :3]
        (x, y, _) = new_arr.shape
        zero = np.zeros((x, y, 2))
        zero = np.dstack((zero, new_arr[:, :, 2]))
        return zero

    @staticmethod
    def to_green(array):
        """Applies a green filter to the image received as a numpy array.
Args:
array: numpy.ndarray corresponding to the image.
Return:
array: numpy.ndarray corresponding to the transformed image.
None: otherwise.
Raises:
This function should not raise any Exception."""
        if not isinstance(array, np.ndarray):
            return None
        new_arr = array[:, :, :3]
        cpy = new_arr.copy()
        cpy[:, :, [0, 2]] = 0
        cpy[:, :, 1] = 1
        return new_arr * cpy

    @staticmethod
    def to_red(array):
        """Applies a red filter to the image received as a numpy array.
Args:
array: numpy.ndarray corresponding to the image.
Return:
array: numpy.ndarray corresponding to the transformed image.
None: otherwise.
Raises:
This function should not raise any Exception."""
        if not isinstance(array, np.ndarray):
            return None
        new_arr = array[:, :, :3]
        return new_arr - ColorFilter.to_blue(new_arr) -\
            ColorFilter.to_green(new_arr)

    @staticmethod
    def to_celluloid(array):
        """Applies a celluloid filter to the image received as a numpy array.
Celluloid filter must display at least four thresholds of shades.
Be careful! You are not asked to apply black contour on the object,
you only have to work on the shades of your images.
Remarks:
celluloid filter is also known as cel-shading or toon-shading.
Args:
array: numpy.ndarray corresponding to the image.
Return:
array: numpy.ndarray corresponding to the transformed image.
None: otherwise.
Raises:
This function should not raise any Exception."""
        if not isinstance(array, np.ndarray):
            return None
        new_arr = array[:, :, :3]
        n_shades = 4
        shades = np.linspace(0, 1, n_shades + 1)
        for i in range(n_shades):
            shade_index = (new_arr >= shades[i]) & (new_arr <= shades[i + 1])
            new_arr[shade_index] = shades[i]
        return new_arr

    @staticmethod
    def to_grayscale(array, filter, **kwargs):
        """Applies a grayscale filter to the image received as a numpy array.
For filter = ’mean’/’m’: performs the mean of RBG channels.
For filter = ’weight’/’w’: performs a weighted mean of RBG channels.
Args:
array: numpy.ndarray corresponding to the image.
filter: string with accepted values in [’m’,’mean’,’w’,’weight’]
weights: [kwargs] list of 3 floats where the sum equals to 1,
corresponding to the weights of each RBG channels.
Return:
array: numpy.ndarray corresponding to the transformed image.
None: otherwise.
Raises:
This function should not raise any Exception."""
        if not isinstance(array, np.ndarray):
            return None
        if filter not in ['m', 'mean', 'w', 'weight', 'weighted']:
            return None
        new_arr = array[:, :, :3]
        if filter in ['m', 'mean']:
            m = new_arr.sum(axis=2) / 3
            return np.dstack((m, m, m))
        else:
            if 'weights' not in kwargs\
                or not isinstance(kwargs['weights'], list)\
                    or len(kwargs['weights']) != 3:
                return None
            weights = kwargs['weights']
            return ColorFilter.to_grayscale(weights * new_arr, 'm')
