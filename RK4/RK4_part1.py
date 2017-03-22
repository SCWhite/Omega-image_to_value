import math
n = 10
h = 0.01
p0 = 0.5
w = 0.2

for i in range(0, 10):
    k1 = w*p0
    y1 = p0 + ((h/2)*k1)
    k2 = w*y1
    y2 = p0 + ((h/2)*k2)
    k3 = w*y2
    y3 = p0 + (h*k3)
    k4 = w*y3

    p1 = p0 + (h/6)*(k1 + 2*k2 + 2*k3 + k4)
    print p1
    p0= p1
print '========================================'

for i in range(1, 10):
    ep = 0.5*math.exp(i*0.01*0.2)
    print ep
    
#print p1
