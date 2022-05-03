from functions import *

with open("blocs/bloc0.txt") as f:
    bloc_0 = f.read()

while somme_5(hash(bloc_0)) > 1:
    clef_hash_0 = '-000-' + clef(10) + "-000-"
    bloc_0 = bloc_0 + clef_hash_0

print("la clef valide du bloc 0 est :",clef_hash_0)
print("la hash de l'ensemble 0 est :",hash(bloc_0))
