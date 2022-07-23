from distutils import extension
from pickletools import optimize
from PIL import Image

import os

dowloadsFolder = "/home/j4viermora/Downloads/"
saveFolder = '/home/j4viermora/Pictures/'


if __name__ == "__main__":
    for filename in os.listdir(dowloadsFolder):
        name, extension = os.path.splitext(dowloadsFolder + filename)

        if extension in [".jpg", ".jpeg", ".png"]:
            picture = Image.open(dowloadsFolder + filename)
            picture.save(saveFolder + "compressed_" +
                         filename, optimize=True, quality=60)
