# -*- coding: cp950 -*-
from PIL import Image

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
def gen(i,j):
    global xbase
    global ybase
    if (xbase < 5) and (ybase < 5):
        new.putpixel((i,j),(255,255,0)) #35
    elif (xbase < 10) and (ybase < 5):
            new.putpixel((i,j),(0,0,255)) #15
    elif (xbase <15) and (ybase < 5):
            new.putpixel((i,j),(255,0,255)) #65
    elif (xbase <20) and (ybase < 5):
            new.putpixel((i,j),(0,150,255)) #10
    elif (xbase <25) and (ybase < 5):
            new.putpixel((i,j),(255,200,0)) #40
    elif (xbase < 5) and (ybase < 10):
            new.putpixel((i,j),(255,0,0)) #50
    elif (xbase < 5) and (ybase < 15):
            new.putpixel((i,j),(0,150,255)) #10
    elif (xbase < 5) and (ybase < 20):
            new.putpixel((i,j),(255,200,0)) #40
    elif (xbase < 5) and (ybase < 25):
        new.putpixel((i,j),(255,255,0)) #35
    elif (xbase < 10) and (ybase < 25):
        new.putpixel((i,j),(0,200,0)) #25
    elif (xbase < 15) and (ybase < 25):
        new.putpixel((i,j),(255,120,0)) #45
    elif (xbase < 20) and (ybase < 25):
        new.putpixel((i,j),(0,255,0)) #20
    elif (xbase < 25) and (ybase < 25):
        new.putpixel((i,j),(200,0,0)) #55
    else:  
        new.putpixel((i,j),(255,255,255))

def cell(xbase,ybase):
    global count
    count = 0
    for i in range(0+59*xbase,59+59*xbase):
        for j in range(0+59*ybase,59+59*ybase):
            gen(i,j)
            #print ('cell: i:' + str(i) +' j:'+ str(j))
            


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
        #print ('5X5: i:' + str(i) +' j:'+ str(j))
        print ('5X5: xb:' + str(xbase) +' yb:'+ str(ybase))
        ybase = ybase + 1
    xbase = xbase + 1
    ybase = 0

        
#print total_list
new.save('gen1.png')#此檔案會存在此程式檔之檔案夾內
print 'ok'


