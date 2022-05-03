from Objects import *
from functions import *


block = Block(2,"-002-zityslwbhb-002-")
for i in range(1,5):
    block.setFilePath("Bloc3/bloc3n°"+str(i)+".txt")
    result = block.hash("-003-nosfbpbxmv-003-")
    if somme_5(result) < 2:
        print("Le bloc correct est le "+str(i)+" ième bloc n°3")
