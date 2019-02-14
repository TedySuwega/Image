import  modules

if __name__ == '__main__':
    a = modules.load_images("D:\Another\Image\image_\image_1.jpg")
    modules.show_image(a)
    hist = modules.calc_histogram(a)
    print(hist)
    grey = modules.rgb2gray(a)
    modules.show_image(grey)
    bw = modules.gray2bw(grey)
    modules.show_image(bw)

    import numpy as np
    from matplotlib import pyplot as plt
    plt.hist(a.ravel(), 256, [0, 256]);
    plt.show()