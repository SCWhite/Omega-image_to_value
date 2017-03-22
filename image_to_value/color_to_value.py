# -*- coding: cp950 -*-
from PIL import Image
import cv2
import numpy

xbase = 0
ybase = 0
count = 0
aver = 0

def check(i,j):
        global count
        r,g,b=a.getpixel((i,j))#注意r g b 為0到255之間的整數
        if (r==0)and(g==255)and(b==255): #5 
            new.putpixel((i,j),(r,g,b))
            count = count + 5
        elif (r==0)and(g==150)and(b==255): #10
            new.putpixel((i,j),(r,g,b))
            count = count + 10
        elif (r==0)and(g==0)and(b==255): #15
            new.putpixel((i,j),(r,g,b))
            count = count + 15
        elif (r==0)and(g==255)and(b==0): #20
            new.putpixel((i,j),(r,g,b))
            count = count + 20
        elif (r==0)and(g==200)and(b==0): #25
            new.putpixel((i,j),(r,g,b))
            count = count + 25
        elif (r==0)and(g==150)and(b==0): #30
            new.putpixel((i,j),(r,g,b))
            count = count + 30
        elif (r==255)and(g==255)and(b==0): #35
            new.putpixel((i,j),(r,g,b))
            count = count + 35
        elif (r==255)and(g==200)and(b==0): #40
            new.putpixel((i,j),(r,g,b))
            count = count + 40
        elif (r==255)and(g==120)and(b==0): #45
            new.putpixel((i,j),(r,g,b))
            count = count + 45
        elif (r==255)and(g==0)and(b==0): #50
            new.putpixel((i,j),(r,g,b))
            count = count + 50
        elif (r==200)and(g==0)and(b==0): #55
            new.putpixel((i,j),(r,g,b))
            count = count + 55
        elif (r==150)and(g==0)and(b==0): #60
            new.putpixel((i,j),(r,g,b))
            count = count + 60
        elif (r==255)and(g==0)and(b==255): #65
            new.putpixel((i,j),(r,g,b))
            count = count + 65
        elif (r==150)and(g==0)and(b==144): #70
            new.putpixel((i,j),(r,g,b))
            count = count + 70

def cell(xbase,ybase):
    global count
    count = 0
    for i in range(0+59*xbase,59+59*xbase):
        for j in range(0+59*ybase,59+59*ybase):
            check(i,j)
            #print i,j
            aver = count/(59*59)
            total_list[xbase][ybase] = aver

img = cv2.imread('test.png')
img = img[490:1965,1125:2600]
cv2.imwrite('res2.png', img)
print 'ok'


#開一個二維陣列
total_list = []
for i in range (0, 25):
    new = []
    for j in range (0, 25):
        new.append(i)
    total_list.append(new)

a=Image.open('res2.png')#找張jpg照片放在此程式檔之檔案夾內
m=a.size[0]
n=a.size[1]
new=Image.new('RGB', (m,n), (255, 255, 255))#建立一張同大小全黑的暫時圖檔 m:x / n:y


for i in range (0, 25):
    for j in range (0, 25):
        cell(i,j)
        ybase = ybase + 1
    xbase = xbase + 1
    
f = open('R_list2.txt','w')
for i in range (0, 25):
    for j in range (0, 25):
        if (total_list[j][i] < 10):
            f.write(' ' + str(total_list[j][i]) + ' ')
        else:
            f.write(str(total_list[j][i]) + ' ')
    f.write('\n')
        
f.close()
print total_list


