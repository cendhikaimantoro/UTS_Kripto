from src.algorithm.Block import Block
from src.algorithm.Toolkit import Toolkit
from src.architecture.FeistelNetwork import FeistelNetwork
from src.mode.CBC import CBC
from src.mode.ECB import ECB

class CipherBlockASRCI():
    def __init__(self,key):
        tk = Toolkit()
        self.fn = FeistelNetwork(tk.roundKey(key), tk.roundFunction, tk.xorFunction)

    def CBCmode(self,text,mode):
        copy = text
        cbc = CBC(self.fn)
        if mode == 'e':
            encrypted = []
            i = 0
            while (i < len(copy)):
                if i + 16 > len(copy) :
                    plain = copy[i:len(copy)]
                else:
                    plain = copy[i:i+16]

                encrypted1, length1 = cbc.encrypt(bytearray(plain))
                i = i + 16
                encrypted.append(encrypted1)
            return b''.join(encrypted)
        if mode == 'd':
            decrypted = []
            i = 0
            while (i < len(copy)):
                if i + 16 >= len(copy) :
                    plain = copy[i:len(copy)]
                    decrypted1, length1 = cbc.decrypt(bytearray(plain),len(copy)-i-1)
                else:
                    plain = copy[i:i+16]
                    decrypted1, length1 = cbc.decrypt(bytearray(plain),16)
                i = i + 16
                decrypted.append(decrypted1[:length1])
            return b''.join(decrypted)
        return b"wrong mode"
