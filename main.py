import cv2
import numpy
import random
import copy 

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
   print(image[0][0])
   out=[]
   f=1
   for j in range(2, height-2):
      for i in range(2, width-2):
         for p in range(-2, 3):
            for q in range(-2, 3):
               if strEle[p+2][q+2][0] != image[j+p][i+q][0]:
                  f=0
                  break
               else:
                  image[j+p][i+q] = [255,255,255]
            if f==0:
               break
         if f==1:
            image[j][i] = [0,0,0]
   out.append(copy.deepcopy(image))
   return out


image = cv2.imread("circle_t.png")
original=cv2.imread("circle_t.png")


height, width, channels = image.shape
out=strthinning(image, height, width)

for o in range(len(out)):
   cv2.imshow(str(o), out[o])
cv2.waitKey(0)

count_in=0
count=0
for r in range(10000):
   x=random.randint(0, width-1)
   y=random.randint(0, height-1)
   lw=liesWithin(y, x, image, width, height)
   if lw%2==1 and image[y][x][0]!=0:
      count_in+=1
      original[y][x] = [0, 0, 255]
      if lw!=1:
         print(y,x,lw)
         original[y][x] = [0, 255, 0]
   count+=1


ratio=count_in/count
outer_area=width*height
inner_area=ratio*outer_area
print(inner_area, outer_area, ratio)

cv2.imshow("plot", original)
cv2.waitKey(0)
