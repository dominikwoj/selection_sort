import random


def selection_sort(in_l):
    '''
        >>> selection_sort([])
        []
        >>> selection_sort([71])
        [71]
        >>> selection_sort([71, 65, 39, 38, 38, 19, 42, 85, 33])
        [19, 33, 38, 38, 39, 42, 65, 71, 85]
        '''

    out_l = []
    for i in range(len(in_l)):
        value = min(in_l)
        out_l.append(value)
        in_l.remove(value)
    return out_l


if __name__ == "__main__":
    # selection_sort([random.randint(0, 100) for i in range(10)])
    import doctest

    doctest.testmod()
