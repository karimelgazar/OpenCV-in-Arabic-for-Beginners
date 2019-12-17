import numpy as np
import cv2

image = cv2.imread('images/khwarizmy-small.jpg')
print(image.shape)
cv2.imshow("The Image", image)

#? translation #
M = np.float32([[1, 0, 50], [0, 1, 100]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

cv2.imshow('[{},{}] Shifted Image'.format(50, 100), shifted)
cv2.waitKey(0)
cv2.destroyAllWindows()


def translate(image, x, y, show=False):
    """
        Our translation matrix M is defined as a floating point array
        this is important because OpenCV expects this matrix
        to be of floating point type.

        The first row of the matrix is [1, 0, x],
        where x is the number of pixels we will shift
        the image left or right. Negative values of x will shift the
        image to the left and positive values will shift the image to
        the right.

        Then, we define the second row of the matrix as [0, 1, y],
        where y is the number of pixels we will shift the image up
        or down. Negative value of y will shift the image up and
        positive values will shift the image down


        Arguments:
            image {np.array} -- the image to translate
            x {int} -- the horizontal shift
            y {int} -- the vertical shift

        Keyword Arguments:
            show {bool} -- show the shiftted image or not (default: {False})

        Returns:
            [np.array] -- the shiftted image
    """
    M = np.float32([[1, 0, x], [0, 1, y]])
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

    if show:
        cv2.imshow('[{},{}] Shifted Image'.format(x, y), shifted)
        cv2.waitKey(0)

    return shifted


#? rotatation #
center = map(lambda x: x // 2, image.shape[1::-1])  # (h, w, channels)
M = cv2.getRotationMatrix2D(tuple(center), -45, float(2))

rotated = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

cv2.imshow('{} Degree Rotated Image'.format(45), rotated)
cv2.waitKey(0)


def rotate(image, angle, scale, show=False):
    """
        Rotate the image in anti-clockwise in a given angle

        Arguments:
            image {np.array} -- original image
            angle {[int]} -- rotation angle
            scale {[float]} -- the scale of the rotated image
        Keyword Arguments:
            show {bool} -- show the rotated image or not (default: {False})

        Returns:
            [np.array] -- the rotated image
    """

    center = map(lambda x: x // 2, image.shape[1::-1])  # (h, w, channels)
    M = cv2.getRotationMatrix2D(tuple(center), angle, float(scale))

    rotated = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

    if show:
        cv2.imshow('{} Degree Rotated Image'.format(angle), rotated)
        cv2.waitKey(0)

    return rotated


#? Resizing #
new_width = 700
r = new_width / image.shape[1]
height = int(r * image.shape[0])

resized = cv2.resize(image, (new_width, height), interpolation=cv2.INTER_AREA)
# cv2.INTER_LINEAR
# cv2.INTER_CUBIC
# cv2.INTER_NEAREST

cv2.imshow('Image Resized By {0:.2f}'.format(r), resized)
cv2.waitKey(0)
cv2.destroyAllWindows()


def resize(image, width=None, height=None, show=False):
    """
        Arguments:
            image {np.array} -- original image
            width {[int]} -- the new width of the resized image
            height {[int]} -- the new height of the resized image

        Keyword Arguments:
            show {bool} -- show the resized image or not (default: {False})

        Returns:
            [np.array] -- the resized image
    """
    if width is None and height is None:
        return image

    if width is None:
        r = height / image.shape[0]
        width = int(r * image.shape[1])
    elif height is None:
        r = width / image.shape[1]
        height = int(r * image.shape[0])

    resized = cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

    if show:
        cv2.imshow('Image Resized By {0:.2f}'.format(r), resized)
        cv2.waitKey(0)

    return resized


#? Flipping #
cv2.imshow("Original", image)
flipped = cv2.flip(image, 1)
cv2.imshow("Flipped Horizontally", flipped)

flipped = cv2.flip(image, 0)
cv2.imshow("Flipped Vertically", flipped)

flipped = cv2.flip(image, -1)
cv2.imshow("Flipped Horizontally & Vertically", flipped)
cv2.waitKey(0)


#! Cropping#
# ? See the Previous Video.
