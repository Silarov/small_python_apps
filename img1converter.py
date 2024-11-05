from ast import While
from PIL import Image

again = "y"

while again == "y":

    imgPath = input("Path of Images:  ")

    for i in range(36):
        if i == 15:
            i + 1
        img = imgPath + "\\" + str(i) + ".jpg"
        img = Image.open (img).convert('RGB')
        destPath = imgPath
        img.save(destPath + '\\' + str(i) + '.webp', 'webp')

    again = input("again? [y|n] ")