import cv2
import numpy
import random
import copy 
from skimage.morphology import skeletonize
from skimage.util import invert
import cv2

strEle = [[[0,0,0] for i in range(5)] for j in range(5)]

def liesWithin(y, x, image, width, height):
   # print(x, width, y, height)
   inx=0
   iny=0
   prevx=0
   prevy=0
   for i in range(x, width):
      if image[y][i][0]==0 and image[y][prevx][0]!=0:
         inx+=1
      prevx=i
   for j in range(y, height):
      if image[j][x][0]==0 and image[prevy][x][0]!=0:
         iny+=1
      prevy=j
   if inx%2==1 and iny%2==1:
      return 1
   return 0

def thinning(image, height, width):
   out=[]
   for it in range(3):
      redundant=[[0 for i in range(width)] for j in range(height)]
      for j in range(1, height-1):
         for i in range(1, width-1):
            kernel=[]
            kernel.append(image[j][i-1]);
            kernel.append(image[j+1][i-1]);
            kernel.append(image[j+1][i]);
            kernel.append(image[j+1][i+1]);
            kernel.append(image[j][i+1]);
            kernel.append(image[j-1][i+1]);
            kernel.append(image[j-1][i]);
            kernel.append(image[j-1][i-1]);
            kernel.append(image[j][i-1]);
            sp=0
            np=0
            for k in range(8):
               if not numpy.array_equal(kernel[k+1], kernel[k]):
                  sp+=1
               if kernel[k].all()==0:
                  np+=1

            if np in [0, 1, 7, 8] or sp<2:
               redundant[j][i]=1

      for j in range(1, height-1):
         for i in range(1, width-1):
            if redundant[j][i]!=1:
               image[j][i]=[255, 255, 255]

      out.append(copy.deepcopy(image))
   return out

def strthinning(image, height, width):
   out = copy.deepcopy(image)
   for j in range(2, height-2):
      for i in range(2, width-2):
         f=1
         for p in range(-2, 3):
            for q in range(-2, 3):
               if image[j+p][i+q][0] != 0:
                  f=0
         if f==1:
            out[j][i] = [0, 0, 0]
         else:
            out[j][i] = [255, 255, 255]
   return out

def zhangthinning(image, height, width, it=0):
   out = copy.deepcopy(image)
   chng = 0
   for j in range(1, height-1):
      for i in range(1, width-1):
         P = [image[j-1][i][0], image[j-1][i+1][0], image[j][i+1][0], image[j+1][i+1][0], image[j+1][i][0], image[j+1][i-1][0], image[j][i-1][0], image[j-1][i-1][0], image[j-1][i][0]]
         A = 0
         B = 0
         for p in range(1, len(P)):
            if P[p] ==0 and P[p-1]==255:
               A+=1
            if P[p] == 0:
               B+=1
         if image[j][i][0]==0 and B>=2 and B<=6 and A==1:
            if not (P[0] == 0 and P[2] == 0 and P[4] == 0):
               if not (P[2] == 0 and P[4] == 0 and P[6] == 0):
                  out[j][i] = [255, 255, 255]
                  chng = 1

   out1 = copy.deepcopy(out)
   for j in range(1, height-1):
      for i in range(1, width-1):
         P = [out[j-1][i][0], out[j-1][i+1][0], out[j][i+1][0], out[j+1][i+1][0], out[j+1][i][0], out[j+1][i-1][0], out[j][i-1][0], out[j-1][i-1][0], out[j-1][i][0]]
         A = 0
         B = 0
         for p in range(1, len(P)):
            if P[p] ==0 and P[p-1]==255:
               A+=1
            if P[p] == 0:
               B+=1
         if out[j][i][0]==0 and B>=2 and B<=6 and A==1:
            if not (P[0] == 0 and P[2] == 0 and P[6] == 0):
               if not (P[0] == 0 and P[4] == 0 and P[6] == 0):
                  out1[j][i] = [255, 255, 255]
                  chng = 1
   cv2.imwrite("C:/Workspace/my/MonteCarloArea/res/"+str(it)+".jpg", out1)
   print(chng)
   if chng == 0:
      return out1
   else:
      return zhangthinning(out1, height, width, it+1)

def skthinning(image):
   # perform skeletonization
   return invert(skeletonize(invert(image)))

def toBW(image):
   for j in range(len(image)):
      for i in range(len(image[0])):
         if image[j][i][1]!=255:
            image[j][i]=[0,0,0]

   return image

image = cv2.imread("circle_t.png")
original=cv2.imread("circle_t.png")


height, width, channels = image.shape
out = skthinning(image)
out = toBW(out)
out1 = copy.deepcopy(out)
count_in=0
count=0
for r in range(100000):
   x=random.randint(0, width-1)
   y=random.randint(0, height-1)
   lw=liesWithin(y, x, out, width, height)
   if lw%2==1 and out[y][x][0]!=0:
      count_in+=1
      out1[y][x] = [255, 0, 0]
      # if lw!=1:
      #    print(y,x,lw)
      #    out[y][x] = [0, 255, 0]
   else:
      out1[y][x] = [0, 0, 255]
   count+=1


ratio=count_in/count
outer_area=width*height
inner_area=ratio*outer_area
print(inner_area, outer_area, ratio)

cv2.imshow("plot", out1)
cv2.waitKey(0)
