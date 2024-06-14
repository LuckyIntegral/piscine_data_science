''' day0, ex06 of python piscine data science '''


def ft_filter(function: callable, iterable: iter) -> list:
    ''' Returns filtered data from iterable:
    Return a list of items for which function(item) is true.
    If function is None, return the items that are true.'''

    if function is None or not callable(function):
        return [el for el in iterable if el]
    return [el for el in iterable if function(el)]
