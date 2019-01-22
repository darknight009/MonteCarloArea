# import tkinter as tk
# root = tk.Tk()
# canvas_1 = tk.Canvas(root, width=250, height=200)
# canvas_1.grid(row=0, column=1)

# point_dicx={}
# point_dicy={}

# def mmove(event):
#    python_green = "#476042"
#    x1, y1 = (event.x - 1), (event.y - 1)
#    x2, y2 = (event.x + 1), (event.y + 1)
#    canvas_1.create_oval(x1, y1, x2, y2, fill=python_green)
#    point_dicx[event.x]=event.y
#    point_dicy[event.y]=event.x

# root.bind('<Motion>', mmove)
# root.mainloop()
# print(point_dicx)
# print(point_dicy)

import random

min_x = 0
max_x = 80
min_y = 0
max_y = 60

up=[]
for x in range(60):
      up.append([x, 0])

down=[]
for x in range(60):
      down.append([x, 40])

right=[]
for y in range(40):
      right.append([60, y])

left=[]
for y in range(40):
      left.append([0, y])

count=0
count_in=0

for i in range(1000000):
   x=random.randint(1, max_x)
   y=random.randint(1, max_y)
   if x<60:
      if y<40:
         count_in+=1
   count+=1

print(count, count_in)
print(80*60*count_in/count)

# from Tkinter import *
# #from tkinter import * # For Python 3.2.3 and higher.
# root = Tk()
# root.title(‘Smoothed line’)
# cw = 250 # canvas width
# ch = 200 # canvas height
# canvas_1 = Canvas(root, width=cw, height=ch, background=”pink”)
# canvas_1.grid(row=0, column=1)

# x1 = 50
# y1 = 10
# x2 = 50
# y2 = 180
# x3 = 180
# y3 = 180

# canvas_1.create_line(x1,y1, x2,y2, x3,y3, smooth=”true”)
# root.mainloop()