import numpy as np
import random
import copy
import cv2
import skvideo.io
from utils import *
from thinning import *

image = cv2.imread("inputs/circle_t.png")
original = copy.deepcopy(image)

height, width, channels = image.shape

out = toBW(skthinning(image))
cv2.imwrite("C:/Workspace/my/MonteCarloArea/results/skeleton.jpg", out)
out1 = copy.deepcopy(out)

toVideo = 0
noOfPoints = 100000
count_in = 0
count = 0

for it in range(noOfPoints//10000):
   out_video =  np.empty([10000, height, width, 3], dtype = np.uint8).astype(np.uint8)
   for r in range(10000):
      x=random.randint(0, width-1)
      y=random.randint(0, height-1)
      lw=liesWithin(y, x, out, width, height)
      if lw%2==1 and out[y][x][0]!=0:
         count_in+=1
         out1[y][x] = [255, 0, 0]
         if lw!=1:
            out[y][x] = [0, 255, 0]
      else:
         out1[y][x] = [0, 0, 255]
      # video.write(out1)
      out_video[r] = out1
      count+=1
   if toVideo:
      skvideo.io.vwrite("res/"+str(it)+"video.mp4", out_video)

ratio=count_in/count
outer_area=width*height
inner_area=ratio*outer_area
print(inner_area, outer_area, ratio)