''' i bet you dont read this '''

def all_thing_is_obj(object: any) -> int:
    ''' function that prints type of the object passed as argument '''
    if isinstance(object, str):
        print(f"{object} is in the kitchen : {type(object)}")
    elif isinstance(object, list):
        print(f"List : {type(object)}")
    elif isinstance(object, set):
        print(f"Set : {type(object)}")
    elif isinstance(object, dict):
        print(f"Dict : {type(object)}")
    elif isinstance(object, tuple):
        print(f"Tuple : {type(object)}")
    elif isinstance(object, list):
        print(f"List : {type(object)}")
    else:
        print("Type not found")
    return 42
