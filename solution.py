import numpy as np
import numpy as np
from obpng import write_png
from obpng import read_png

import os
from skimage.morphology import erosion, dilation, opening, closing, white_tophat
from skimage.morphology import black_tophat, skeletonize, convex_hull_image
from skimage.morphology import disk
from skimage.data import data_dir
from skimage.util import img_as_ubyte
from skimage import io

# Zadanie na ocenę dostateczną
def renew_pictures():

    orig_crush1 = img_as_ubyte(io.imread(os.path.join(data_dir, '..\..\..\..\..\crushed1.png'), as_gray=True))
    orig_crush2 = img_as_ubyte(io.imread(os.path.join(data_dir, '..\..\..\..\..\crushed2.png'), as_gray=True))
    orig_crush3 = img_as_ubyte(io.imread(os.path.join(data_dir, '..\..\..\..\..\crushed3.png'), as_gray=True))
    orig_crush4 = img_as_ubyte(io.imread(os.path.join(data_dir, '..\..\..\..\..\crushed4.png'), as_gray=True))
    orig_crush = read_png('crushed1.png')
    orig_crush = np.squeeze(orig_crush)
    #print(orig_crush1)

    selem_1 = disk(1)
    selem_2 = disk(1)
    #print(selem_2)
    selem_3 = disk(2)
    selem_4 = disk(3)

    #print(selem_1)
    eroded = opening(orig_crush1, selem_1)
    io.imsave("crush1.png", eroded)


    #print(disk)
    eroded = opening(orig_crush2, selem_2)
    eroded = closing(eroded, selem_2)
    io.imsave("crush2.png", eroded)


    #print(selem_3)
    eroded = opening(orig_crush3, selem_1)
    eroded = closing(eroded, selem_1)

    eroded = opening(eroded, selem_3)

    eroded = opening(eroded, selem_4)
    io.imsave("crush3.png", eroded)


    #print(disk)
    eroded = opening(orig_crush4, selem_1)
    eroded = closing(eroded, selem_1)

    eroded = closing(eroded, selem_3)
    eroded = opening(eroded, selem_3)

    eroded = opening(eroded, selem_4)

    io.imsave("crush4.png", eroded)

    pass


# Zadanie na ocenę dobrą
def own_simple_erosion(image):
    new_image = np.zeros(image.shape, dtype=image.dtype)

    def erode(mask, img):
        w = mask.shape[0]
        h = mask.shape[1]
        sum = 0

        for i in range(w-1):
            for t in range(h-1):
                if (img[i, t] == 0) & (mask[i, t] == 1):
                    sum = sum + 1
                else:
                    sum = sum
        if sum == 0:
            return 255
        else:
            return 0



    def get_img(im, point, mask):
        w = mask.shape[0]
        h = mask.shape[1]
        d = int(w/2)

        img = im[point[0]-d:point[0]+d+1, point[1]-d:point[1]+d+1]
        return img

    image = np.squeeze(image)
    kernel = disk(1)
    w = image.shape[0]
    h = image.shape[1]

    d = int((kernel.shape[0])/2)
    new_image = image

    #print(image)

    for i in range(w-1):
        if (i >= d) & (i <= w - d):
            for t in range(h-1):
                if (t >= d) & (t <= h - d)
                    k = get_img(image, (i, t), kernel)
                    new_image[i, t] = erode(kernel, k)




    write_png(new_image, 'results/erosion.png')

    return new_image


# Zadanie na ocenę bardzo dobrą
def own_erosion(image, kernel=None):
    new_image = np.zeros(image.shape, dtype=image.dtype)
    if kernel is None:
        kernel = np.array([[0, 1, 0],
                           [1, 1, 1],
                           [0, 1, 0]])

    def erode(mask, img):
        w = mask.shape[0]
        h = mask.shape[1]
        sum = 0

        for i in range(w-1):
            for t in range(h-1):
                if (img[i, t] == 0) & (mask[i, t] == 1):
                    sum = sum + 1
                else:
                    sum = sum
        if sum == 0:
            return 255
        else:
            return 0



    def get_img(im, point, mask):
        w = mask.shape[0]
        h = mask.shape[1]
        d = int(w/2)

        img = im[point[0]-d:point[0]+d+1, point[1]-d:point[1]+d+1]
        return img


    image = np.squeeze(image)
    w = image.shape[0]
    h = image.shape[1]

    d = int((kernel.shape[0])/2)
    new_image = image

    #print(image)

    for i in range(w-1):
        if (i >= d) & (i <= w - d):
            for t in range(h-1):
                if (t >= d) & (t <= h - d):
                    image = read_png('3_checkerboard.png')
                    image = np.squeeze(image)
                    k = get_img(image, (i, t), kernel)
                    new_image[i, t] = erode(kernel, k)




    write_png(new_image, 'results/erosion.png')

    return new_image
