from PIL import Image
import image_slicer
import os

path = 'BeforeAfter'
arr = os.listdir(path)

def crop():
    for i in arr:
        # fullpath = os.path.join(path, i)
        if os.path.isfile(i):
            img = Image.open(i)
            f, e = os.path.splitext(i)
            left = 66.6
            top = 37.4
            right = 1212.4
            bottom = 550.7
            imCrop = img.crop((left, top, right, bottom))
            imCrop.save("CroppedImages/", "PNG", quality= 100)
            # tiles = image_slicer.slice(toslice, 12, save=False)
            # image_slicer.save_tiles(tiles, directory='frames')
crop()