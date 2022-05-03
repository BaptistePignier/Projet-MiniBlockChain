from Objects import *
import time
import matplotlib.pyplot as plt


block = Block(1,"-000-vemvkcrwvyev-000-")
y,x = [],[]
for i in range(1,6):
    start = time.time()
    block.Validate(i)
    end = time.time()
    lapse = end - start
    x.append(i)
    y.append(lapse)
plt.plot(x,y,'k')
plt.show()
