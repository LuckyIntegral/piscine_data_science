''' day0, ex03 of python piscine data science '''
import math

def NULL_not_found(obj: any) -> int:
    ''' function checks if the passed parameter is NULL '''

    if obj is None:
        print(f'Nothing: None {type(obj)}')
    elif isinstance(obj, float) and math.isnan(obj):
        print(f'Cheese: {obj} {type(obj)}')
    elif isinstance(obj, int) and obj == 0:
        print(f'Zero: {obj} {type(obj)}')
    elif isinstance(obj, bool) and obj is False:
        print(f'Fake: {obj} {type(obj)}')
    elif isinstance(obj, str) and obj == '':
        print(f'Empty: {obj} {type(obj)}')
    else:
        print('Type not Found')
        return 1
    
    return 0

# Nothing: None <class 'NoneType'>$
# Cheese: nan <class 'float'>$
# Zero: 0 <class 'int'>$
# Empty: <class 'str'>$
# Fake: False <class 'bool'>$
# Type not Found$
# 1$
