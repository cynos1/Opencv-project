import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
from PIL import Image
import image_slicer


    # crop the image
im = cv2.imread('pic1.png')
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
_,thresh = cv2.threshold(gray,50,255,cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[1]
x,y,w,h = cv2.boundingRect(cnt)
print(x,y,w,h)
crop_image = im[y:y+h, x:x+w]

plt.imshow(im)
plt.show()
# cv2.imshow("cropped", thresh)
# cv2.waitKey()
# cv2.destroyAllWindows()
# cv2.imwrite("cropped3.png", crop_image)



# arr = os.listdir('BeforeAfter')

# for itr in arr:
#     img = cv2.imread(itr)
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     _,thresh = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)
#     _, contours, _ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#     cnt = contours[0]
#     x,y,w,h = cv2.boundingRect(cnt)
#     crop = img[y:y+h,x:x+w]
#     cv2.imwrite('CroppedImages'+itr,crop)











# im = cv2.imread('pic1.png')
# y = 5
# x = 5
# w = 514
# h = 1150

# crop_image = im[x:w, y:h]
# cv2.imshow("cropped", crop_image)
# cv2.imwrite("cropped1.png", crop_image)
# cv2.waitKey(0)  



# separate image into frames
# def image_slicers(img):
#     tiles = image_slicer.slice(img,12, save=False)
#     image_slicer.save_tiles(tiles, prefix='slice', directory='frames1')
# image_slicers('cropped.png')

    # output = image_slicers(image_manipulation('pic1.png'))
    # return output
  
      







# print(os.getcwd())
# os.chdir('Downloads\frame1')
# path = 'Downloads\frame1'
# os.listdir()
# mean_height = 0
# mean_width = 0

# num_of_images = len(os.listdir('.'))

# for file in os.listdir('.'):
#     im = Image.open(os.path.join(path, file))
#     width, height = im.size
#     mean_width += width
#     mean_height += height
    
# mean_width = int(mean_width/ num_of_images)
# mean_height = int(mean_height/ num_of_images)

# for file in os.listdir('.'):
#     if file.endswith("png"):
#         im = Image.open(os.path.join(path, file))
        
#         width, height = im.size
#         print(width, height)
        
#         imResize = imResize((mean_width, mean_height), Image.ANTIALIAS)
#         imResize.save(file, 'png', quality = 95)
#         print(im.filename.split('\\')[-1], "is resized")
# def generate_video():
#     image_folder = 'Downloads/frame1'
#     video_name = 'video1.mp4'
#     os.chdir("Downloads/frame1")
    
#     images = [img for img in os.listdir(image_folder)
#              if img.endswith("png")]
#     print(images)
#     fram = cv2.VideoWriter(video_name, 0,1, (width, height))
    
#     for image in images:
#         video.write(cv2.imread(os.path.join(image_folder, image)))
#     cv2.destroyAllWindows()
#     video.release()
# generate_video()


