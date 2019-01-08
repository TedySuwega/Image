import cv2

def loadImage(image):
    result = cv2.imread(image)
    return result

def load_images(loc):
    return cv2.imread(loc)

def rgb2gray(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def show_image(img):
    cv2.imshow(img,0)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# a = loadImage()
a = cv2.imread('D:\Another\Image\image\image_1.jpg')
show_image(a)
# print(a)