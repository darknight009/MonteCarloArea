from skimage.morphology import skeletonize
from skimage.util import invert
import copy

strEle = [[[0,0,0] for i in range(5)] for j in range(5)]

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
   if chng == 0:
      return out1
   else:
      return zhangthinning(out1, height, width, it+1)

def skthinning(image):
   return invert(skeletonize(invert(image)))