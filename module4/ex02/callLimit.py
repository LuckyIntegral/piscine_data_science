
def callLimit(limit: int):
    '''decorator that limits the number of calls to a function
    Args:
        limit: the maximum number of calls to the function
    Returns:
        function: the function that has limited calls
    '''
    count = 0

    def callLimiter(function):
        '''wrapped function with limited calls
        Args:
            function: the function to be limited
        Returns:
            function: the wrapped function with limited calls
        '''

        def limit_function(*args: any, **kwds: any):
            '''function that limits the number of calls to a function'''
            nonlocal count
            count += 1
            if count <= limit:
                return function(*args, **kwds)
            print(f'Error {function} call too many times')
            return None
        return limit_function
    return callLimiter
