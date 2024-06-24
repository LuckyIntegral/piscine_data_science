import time
import functools as ft

def cache():
    '''decorator that caches the result of a function'''
    cache = {}
    def wrapper(func):
        def inner(*args, **kwargs):
            if args not in cache:
                cache[args] = func(*args, **kwargs)
            return cache[args]
        return inner
    return wrapper


@cache()
def pow(x: int | float) -> int | float:
    '''function that calculates the power of a number'''
    print('time consuming operation')
    time.sleep(1)
    return x ** x


for i in range(5):
    for j in range(1, 6):
        print(pow(j))
