import numpy as np


class NumPyCreator:
    @staticmethod
    def type_is_consistent(iterable, tp):
        types = list(set(map(type, iterable)))
        if len(types) == 1:
            return types[0]
        else:
            if tp in types:
                return None
            else:
                return types[0]

    @staticmethod
    def is_valid(arg, tp):
        queue = []
        queue.extend(arg)
        while queue:
            consistent = NumPyCreator.type_is_consistent(queue, tp)
            if consistent is None:
                return False
            n = len(queue)
            if consistent is tp:
                if len(set(map(len, queue))) > 1:
                    return False
                for _ in range(n):
                    elem = queue.pop(0)
                    queue.extend(elem)
            else:
                break
        return True

    @staticmethod
    def from_list(lst):
        if not isinstance(lst, list):
            return None
        if not NumPyCreator.is_valid(lst, list):
            return None
        return np.array(lst)

    @staticmethod
    def from_tuple(tpl):
        if not isinstance(tpl, tuple):
            return None
        if not NumPyCreator.is_valid(tpl, tuple):
            return None
        return np.array(tpl)

    @staticmethod
    def from_iterable(itr):
        if itr:
            return np.fromiter(itr, type(itr[0]))
        return None

    @staticmethod
    def from_shape(shape, value=0):
        if not isinstance(shape, tuple) or len(shape) != 2\
                or not isinstance(shape[0], int)\
                or not isinstance(shape[1], int)\
                or shape[0] < 0 or shape[1] < 0:
            return None
        return np.full(shape, value)

    @staticmethod
    def random(shape):
        if not isinstance(shape, tuple) or len(shape) != 2\
                or not isinstance(shape[0], int)\
                or not isinstance(shape[1], int)\
                or shape[0] < 0 or shape[1] < 0:
            return None
        return np.random.random(shape)

    @staticmethod
    def identity(n):
        if n < 0:
            return None
        return np.identity(n)
