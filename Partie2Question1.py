from functions import *
import time
import matplotlib.pyplot as plt
with open("blocs/bloc0.txt") as f:
    bloc_0 = f.read()
T = []
I = []

for i in range (4,10):
    t1 = time.time()
    bloc_0 = '000-' + clef(i) + '-000'
    while somme_5(hash(bloc_0)) > 1: #si somme des 5 premiers termes du hash > 1 on continue de chercher une clef
        bloc_0 = '000-' + clef(i) + '-000'
    t2 = time.time()



    T = T + [t2 - t1]
    I = I + [i]

print(T)
print(I)

plt.plot(I,T)
plt.show()
