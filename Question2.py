from functions import *

with open("blocs/bloc0.txt") as f:
    bloc = f.read()

clef = ["-000-uuqubeebuz-000-" ,"-000-ennizblvwg-000-", "-000-qtdnw-000-","-000-ciuvfdfxns-000-"] #liste des clefs à tester
for clef_ in clef:
    bloc_0 = bloc + clef_
    somme = somme_5(hash(bloc_0))
    print(somme)
    if somme < 2:
        print("La clef "+clef_+" est valide")
    else:
        print("La clef "+clef_+" n'est pas valide")
