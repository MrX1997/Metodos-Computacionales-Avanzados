from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

#5
a = np.linspace(0,2*np.pi,200)
x = np.cos(a)
y = np.sin(a)

def RPHD(N):

    nx=np.zeros(N)
    ny=np.zeros(N)
    nx1=np.zeros(N)
    ny1=np.zeros(N)
    for i in range(N):
        
        nx[i]=np.random.uniform(-1.0,1.0)
        ny[i]=np.random.uniform(-1.0,1.0)
        if( (nx[i]**2 + ny[i]**2)**0.5 < 1.0 ):
            nx1[i]=nx[i]
            ny1[i]=ny[i]
        
    return nx1,ny1

x1,y1=RPHD(1000)

plt.plot(x,y)
plt.scatter(x1,y1,color='R')
plt.axis("equal")
plt.show()



#6

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def RPHD(N):

	nx=np.zeros(N)
	ny=np.zeros(N)
	nz=np.zeros(N)
	nx1=np.zeros(N)
	ny1=np.zeros(N)
	nz1=np.zeros(N)

	for i in range(N):
		nx[i]=np.random.uniform(-1.0,1.0)
    		ny[i]=np.random.uniform(-1.0,1.0)
		nz[i]=np.random.uniform(-1.0,1.0)
		if(nx[i]<0.0):
			nx1[i]=-1*(np.sin(np.arccos(nz[i])))*(np.cos(np.arctan(ny[i]/nx[i])))
			ny1[i]=(np.sin(np.arccos(nz[i])))*(np.sin(np.arctan(ny[i]/nx[i])))	
			nz1[i]=np.cos(np.arccos(nz[i]))
		else:			
			nx1[i]=(np.sin(np.arccos(nz[i])))*(np.cos(np.arctan(ny[i]/nx[i])))
			ny1[i]=(np.sin(np.arccos(nz[i])))*(np.sin(np.arctan(ny[i]/nx[i])))	
			nz1[i]=np.cos(np.arccos(nz[i]))
		

	return nx1,ny1,nz1

x1,y1,z1=RPHD(10000)
print(x1,y1,z1)
ax.scatter(x1, y1, z1, c='r', marker='o')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')


plt.show()

 
#1
k=np.zeros((4,8))
k[:,7]=-1
k[1,:]=2
k

#2
a=np.random.normal(size=1000,scale=1.0)
a.mean()
i=(a>2.0)
print(a[i])

#3
a=np.random.normal(size=1000,scale=1.0)
b=np.linspace(-1,1)


#4
import numpy as np 
import matplotlib.pyplot as plt
a=5
b=4
A=5.0
B=5.0
f=np.pi/2
t=np.linspace(0,100,10000)
x=A*np.sin(a*t + f )
y=B*np.sin(b*t)
plt.scatter(x,y)
plt.show()




