
def square(x: int | float) -> int | float:
    '''function that calculates the square of a number'''
    return x ** 2


def pow(x: int | float) -> int | float:
    '''function that calculates the power of a number'''
    return x ** x


def outer(x: int | float, function) -> object:
    '''function that applies a function to a number'''
    count = 0

    def inner() -> float:
        '''the function applies to the number'''
        nonlocal count
        count += 1
        res = x
        for _ in range(count):
            res = function(res)
        return res
    return inner
