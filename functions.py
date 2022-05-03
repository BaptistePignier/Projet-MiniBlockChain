import random
import string
import hashlib


def gen_key(rank):
    rand_key = clef(10)
    delimiter = "".join(["0" for i in range(3-len(str(rank)))]+[str(rank)])  # convert 0 to 001 and 24 to 024
    end_key = "-"+str(delimiter) +"-"+ rand_key +"-"+str(delimiter)+"-"
    return end_key

def listAlphabet():
  return list(string.ascii_lowercase)

lettres = listAlphabet()

def somme_5(hash_bloc):
    return somme(hash_bloc,5)

def somme(hash_bloc,difficulty):
    somme = 0
    list_hash = [int(c) for c in str(hash_bloc)]  # Je décompose mon hash en lisye de chiffres pour pouvoir les additionner
    for i in range(difficulty):
        somme = somme + list_hash[i]
    return(somme)

def hash(bloc_0):
    MdP = bloc_0
    MdP = MdP.encode('utf-8')
    m = hashlib.md5(MdP)
    a = m.hexdigest()
    a = int(a,16)     # convertir en base 10
    return(a)

def clef(x):
    c = []
    for i in range (x):
        j = random.randint(1,25)
        c.append(lettres[j])
        f = ''.join(c)
    return(f) # j'obtiens une clef de x lettres
