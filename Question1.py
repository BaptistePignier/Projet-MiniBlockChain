from functions import *

liste_hash = [
"0x4b3c4feeab8708750b12bd7a1ba03077",
"0x5a49213ff01230c46eeaad541676f10e",
"0x4b3b682cb51beda819af2acebca9ceb4",
"0x9e094121e956fc26999c47bb35aa308c"
]

for hash_ in liste_hash:

    a = int(hash_,16)
    s = somme_5(a)
    if s == 1:
        print("Le hash "+hash_+" est valide")
    else:
        print("Le hash "+hash_+" n'est pas valide")
