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

def toBW(image):
   for j in range(len(image)):
      for i in range(len(image[0])):
         if image[j][i][1]!=255:
            image[j][i]=[0,0,0]
   return image