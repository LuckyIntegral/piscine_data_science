''' module1/ex03 '''
from PIL import Image
import numpy as np


def ft_load(path: str) -> np.array:
    ''' the function loads the image and returns rgb array of pixels'''
    try:
        img = Image.open(path)
        arr = np.array(img)
        return arr
    except Exception as e:
        print(f"Error: {e}")
    return None
