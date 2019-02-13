import cv2

def load_images(loc):
    return cv2.imread(loc)

def rgb2gray(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def show_image(img):
    cv2.imshow('', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


loc = "D:\Another\Image\image_\image_1.jpg"
img = cv2.imread(loc)
print(img)
cv2.imshow('',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# img = load_images(loc)
