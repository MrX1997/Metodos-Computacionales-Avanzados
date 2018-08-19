
# coding: utf-8

# In[ ]:




# In[58]:

import numpy as np
import matplotlib.pyplot as plt

N=1000 #numero de personas 
am=40

a=np.linspace(0,am)
edadm=[]
for i in range(1,101):
    for j in range(500):
        ed=np.random.randint(1,i+1,N)
        p=np.random.choice(ed)
        q=np.random.choice(ed)
        if(p>q)&(p==am):
            edadm.append(p)
        else:
            edadm.append(q)

sig=(np.var(edadm))**0.5
ii=np.argmax(edadm)
mp=edadm[ii]
m=np.mean(edadm)


values = 'Max Prob = {:.2f}, Mean = {:.2f}, Sigma={:.2f}'.format(mp, m, sig)

plt.hist(edadm, bins=100,normed="True")
plt.title(values)
plt.legend()
plt.xlim(40)
plt.xlabel('$Edad$')
plt.ylabel('$PDF (p_a|40)$')
plt.savefig('ejercicio4.pdf')


# In[ ]:



