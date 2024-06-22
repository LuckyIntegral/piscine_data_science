
def ft_mean(*args: any) -> float:
    '''function that calculates the mean of a list of numbers
    '''
    if not args:
        print('ERROR')
    else:
        print(f'mean: {sum(args) / len(args)}')


def ft_median(*args: any) -> float:
    '''function that calculates the median of a list of numbers
    '''
    if not args:
        print('ERROR')
    else:
        args = sorted(args)
        n = len(args)
        if n % 2 == 0:
            print(f'median: {(args[n // 2 - 1] + args[n // 2]) / 2}')
        else:
            print(f'median: {args[n // 2]}')


def ft_quartile(*args: any) -> float:
    '''function that calculates the quartile of a list of numbers
    '''
    def ft_round(n: float) -> int:
        '''function that rounds a number division
        '''
        return int(n)

    if not args:
        print('ERROR')
    else:
        args = sorted(args)
        n = len(args)
        q1 = args[ft_round(n * 0.25)]
        q2 = args[ft_round(n * 0.75)]
        print(f'quartile: {q1}, {q2}')


def ft_standard_deviation(*args: any) -> float:
    '''function that calculates the variance of a list of numbers
    '''
    if not args:
        print('ERROR')
    else:
        mean = sum(args) / len(args)
        n = len(args)
        std = sum((el - mean) ** 2 for el in args) / n
        std = std ** 0.5
        print(f'std: {std}')


def ft_variance(*args: any) -> float:
    '''function that calculates the standard deviation of a list of numbers
    '''
    if not args:
        print('ERROR')
    else:
        mean = sum(args) / len(args)
        n = len(args)
        variance = sum((el - mean) ** 2 for el in args) / n
        print(f'var: {variance}')


def ft_statistics(*args: any, **kwargs: any) -> None:
    '''function that calculates the next statistics:
    mean, median, mode, variance and standard deviation
    '''
    for value in kwargs.values():
        if not all(isinstance(el, (int, float)) for el in args):
            print('ERROR')
            continue
        if value == "mean":
            ft_mean(*args)
        elif value == "median":
            ft_median(*args)
        elif value == "quartile":
            ft_quartile(*args)
        elif value == "var":
            ft_variance(*args)
        elif value == "std":
            ft_standard_deviation(*args)
