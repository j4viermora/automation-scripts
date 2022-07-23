from distutils import extension
from distutils.command.build_ext import extension_name_re
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
            os.remove(dowloadsFolder + filename)
            print(name + ": " + extension)
        if extension in ["mp3"]:
            musicFolder = "/home/j4viermora/Downloads/music"
