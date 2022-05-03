from functions import *
class Block:

    def __init__(self,rank,previous_key):
        self.rank = rank
        self.start_key = previous_key
        self.file_path = "blocs/bloc"+str(rank)+".txt"


    # Methode qui valide la clé d'un bloc
    def Validate(self,difficulty):
        while 1:
            end_key = gen_key(self.rank)
            result = self.hash(end_key)
            if somme(result,difficulty) < 2:
                break
        self.end_key = end_key

    def hash(self,end_key):
        bloc_to_hash = self.start_key+"\n"+open(self.file_path,"r").read()+end_key
        hasher = hashlib.md5(bloc_to_hash.encode("utf-8"))
        hex = hasher.hexdigest()
        return int(hex,16)

    def setFilePath(self,file_path):
        self.file_path = file_path

    def getContent(self):
        with open(self.file_path, 'r') as afile:
            buf = afile.read()
            return buf
