import numpy as np
import math 
import random 
#1.1
(1+5**0.5)/2
print('\n')

#2.1
lis=[1,2,3,4,5,6,7,8,9,10]
lis[0:5]
print(lis)
print('\n')

#2.2
lista=np.zeros(100)
for n in range(0,100):
    lista[n]=(-1)**n
print(lista)
print('\n')

#2.3    
lista
l=np.zeros(31)
l[15]=1
print(l)
print('\n')

#2.4
m = [21, 48, 79, 60, 77, 15, 43, 90, 5, 49, 15, 52, 20, 70, 55, 4, 86, 49, 87, 59]

b=sorted(m)
median=(b[9]+b[10])/2.0
print(median)
print('\n')

#3.1	
dc={"0":"a","1": "e","2":"i","3":"o","4":"u"}
#print(dc["0"])

#3.2
act= {
    'Monday': {'study':4, 'sleep':8, 'party':0},
    'Tuesday': {'study':8, 'sleep':4, 'party':0},
    'Wednesday': {'study':8, 'sleep':4, 'party':0},
    'Thursday': {'study':4, 'sleep':4, 'party':4},
    'Friday': {'study':1, 'sleep':4, 'party':8},}
 
nw={}
for k , v in act.items():
	s=sum(v.values())
	nw[k]=s

print(nw)
print('\n')

#4.1
for i in range(6):
    ini=5
    n=ini-i
    print(n)
print('\n')

#4.2
def rd(N):
	mvb=np.zeros(N)
	for i in range(N):
		a=random.random()
		mvb[i]=a
		s=sum(mvb)
	return s

f=rd(100)
print(f)
print('\n')

#4.3
def stddev(N):
	new=np.zeros(1000)
	xc=0.0
	for i in range(1000):
		new[i]=rd(N)
	prom=sum(new)/1000
	for i in range(1000):
		xc+=(new[i]-prom)**2
	t=(xc/(N-1.0))**0.5
	return t

re=stddev(100)
print re
print('\n')
		
#5.1
c=0
n=0
while n < 100:
    step=int(6.0*random.random())+1
    n+=step
    c+=1
print(c,n)
print('\n')

#6.1
def eucld(a,b):
    N=len(a)
    p=0
    for i in range(0,N):
        p+=(a[i]-b[i])**2
    
    t=p**0.5
    return t
a=[0,0]
b=[1,1]
u=eucld(a,b)
print(u)
print('\n')

#7.1
class Circle:
    def __init__(self,r):
        self.radius=r
    def perimetro(self):
        
        return 2.0*math.pi * self.radius 
a=Circle(0.5)
print(a.perimetro())
print('\n')

#7.2
class Vector3D:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def dot(self,v):
        return (self.x)*(v.x)+(self.y)*(v.y)+(self.z)*(v.z)
v = Vector3D(2, 0, 1)
w = Vector3D(1, -1, 3)
cv=v.dot(w)
print(cv)
print('\n')

#8.1
fk=np.zeros(10)
for i in range(10):
    fk[i]=i
print fk
random.shuffle(fk)
print(fk)
	


	
	
