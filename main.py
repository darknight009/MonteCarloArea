import cv2
import numpy
import random

def liesWithin(y, x, image, width):
   inx=0
   prev=0
   for i in range(x, width):
      if image[y][i][0]==0 and image[y][prev][0]!=0:
         inx+=1
      prev=i
   return inx

image = cv2.imread("rect.png")
original=cv2.imread("rect.png")
# kernel = numpy.ones((3,3),numpy.uint8)
# eroded = cv2.erode(image,kernel,iterations = 1)
# eroded = cv2.erode(eroded,kernel,iterations = 1)

# cv2.imshow('Main', image)
# cv2.imshow('Numpy Vertical', eroded)
# cv2.waitKey(0)

height, width, channels = image.shape
redundant=[[0 for i in range(width)] for j in range(height)]
# for it in range(1):
#    for j in range(1, height-1):
#       for i in range(1, width-1):
#          kernel=[]
#          kernel.append(image[j][i-1]);
#          kernel.append(image[j+1][i-1]);
#          kernel.append(image[j+1][i]);
#          kernel.append(image[j+1][i+1]);
#          kernel.append(image[j][i+1]);
#          kernel.append(image[j-1][i+1]);
#          kernel.append(image[j-1][i]);
#          kernel.append(image[j-1][i-1]);
#          kernel.append(image[j][i-1]);
#          sp=0
#          np=0
#          for k in range(8):
#             if not numpy.array_equal(kernel[k+1], kernel[k]):
#                sp+=1
#             if kernel[k].all()==0:
#                np+=1

#          if np in [0, 1, 7, 8] or sp<2:
#             redundant[j][i]=1

#    for j in range(1, height-1):
#       for i in range(1, width-1):
#          if redundant[j][i]!=1:
#             image[j][i]=[255, 255, 255]

count_in=0
count=0
for r in range(10000):
   x=random.randint(0, width-1)
   y=random.randint(0, height-1)
   lw=liesWithin(y, x, image, width)
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

cv2.imshow('original', original)
cv2.imshow('thinned', image)
cv2.waitKey(0)


# print(boundary)
# boundary = smooth(boundary)
# print(boundary)

# img = numpy.zeros((height,width,3), numpy.uint8)

# for x in boundary:
#    if len(boundary[x])>1:
#       cv2.rect(img,(x,boundary[x][0]), 1, (0,0,255), -1)
#       cv2.rect(img,(x,boundary[x][1]), 1, (0,0,255), -1)
#    else:
#       print(x, boundary[x])
#       cv2.rect(img,(x,boundary[x][0]), 1, (0,0,255), -1)

# # cv2.imshow('Draw01',img)
# # cv2.waitKey(0)

# count=0

# for i in range(10000):
#    y = random.random() * height
#    x = random.random() * width
#    count+=liesWithin(boundary, x, y)

# print(count)