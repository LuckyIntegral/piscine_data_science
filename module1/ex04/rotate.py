''' module1/ex04 '''
import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def ft_transpose(image: np.array) -> np.array:
    ''' transpose '''
    new = np.zeros((400, 400, 1))
    for i in range(400):
        for j in range(400):
            new[i][j] = image[j][i]
    return new


def zoom(image: np.array) -> None:
    ''' zoom '''
    print(f'The shape of image is: {image.shape}')
    print(image)
    image = image[100:500, 450:850, 0:1]
    print(f'New shape after slicing: {image.shape} or {image.shape[0:2]}')
    print(image)

    image = ft_transpose(image)

    plt.imshow(image, cmap='gray')
    plt.title('Image')
    plt.show()


def main():
    ''' entrypoint '''
    image = ft_load('animal.jpeg')
    if image is not None:
        zoom(image)


if __name__ == '__main__':
    main()
