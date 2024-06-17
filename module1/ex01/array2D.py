''' module1/ex01 '''
import numpy as np


def is_list(obj: any) -> bool:
    ''' checks if the object is list '''
    return obj is not None and isinstance(obj, list)


def slice_me(family: list, start: int, end: int) -> list:
    ''' slicer '''

    if not is_list(family):
        print('Assertion error : invalid argument')
        return None

    if not all(is_list(e) for e in family):
        print('Assertion error : invalid argument')
        return None

    list_size = len(family[0])
    if not all(len(e) == list_size for e in family):
        print('Assertion error : invalid argument')
        return None

    if np.abs(start) > len(family) or np.abs(end) > len(family):
        print('Assertion error : invalid argument')
        return None

    arr = np.array(family)
    print(f'My shape is : {arr.shape}')
    arr = arr[start:end]
    print(f'My new shape is : {arr.shape}')
    return np.ndarray.tolist(arr)
