from skimage.measure import compare_ssim as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2
from PIL import Image

import gnureadline


img1 = cv2.imread('similar_images/empire_basic_2.jpg')
img2 = cv2.imread('similar_images/empire_basic_3.jpg')
img1_1 = cv2.imread('similar_images/empire_purple_1.jpg')
img1_2 = cv2.imread('similar_images/empire_purple_2.jpg')

if img1.shape > img2.shape:


def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    import pdb; pdb.set_trace()
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    import pdb; pdb.set_trace()
    err /= float(imageA.shape[0] * imageA.shape[1])

    # return the MSE, the lower the error, the more "similar"
    # the two images are
    return err


def compare_images(imageA, imageB, title):
    # compute the mean squared error and structural similarity
    # index for the images
    import pdb; pdb.set_trace()

    m = mse(imageA, imageB)
    s = ssim(imageA, imageB)

    import pdb; pdb.set_trace()

    # setup the figure
    fig = plt.figure(title)
    # plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))

    # show first image
    ax = fig.add_subplot(1, 2, 1)
    plt.imshow(imageA, cmap=plt.cm.gray)
    plt.axis("off")

    # show the second image
    ax = fig.add_subplot(1, 2, 2)
    plt.imshow(imageB, cmap=plt.cm.gray)
    plt.axis("off")

    # show the images
    plt.show()



import pdb; pdb.set_trace()