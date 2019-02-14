import cv2

def load_images(loc):
    return cv2.imread(loc)

def rgb2gray(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def show_image(img):
    cv2.imshow('', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def calc_histogram(img):
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    return (hist)

def gray2bw(img):
    """
    Convert grayscaled image into black & white image

    :param img: Grayscaled image
    :return: Black & white image
    """
    # return cv2.threshold(img, 75, 255, cv2.THRESH_TOZERO)[1]
    return cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)[1]
