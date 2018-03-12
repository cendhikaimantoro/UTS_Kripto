from src.algorithm.Block import Block
from src.algorithm.Toolkit import Toolkit

class CBC(object):

    def __init__(self, chiperEngine):
        self.firstEncrypt = True
        self.firstDecrypt = True
        self.chiperEngine = chiperEngine

    def encrypt(self, blockByte):
        length = len(blockByte)

        #assertion
        if length > 16:
            print("KABOOOMM!!!! Block too big")

        #transform into bit matrix
        blockBit = Block(blockByte, Block.BYTE)

        if (self.firstEncrypt):
            encrypted = self.chiperEngine.encrypt(blockBit.bit)
            chiperBit = Block((encrypted[0],encrypted[1],16), Block.BIT)
            chiperByte = chiperBit.byte
            self.firstEncrypt = False
        else:
            tk = Toolkit()
            input = (tk.xorFunction(blockBit.bit[0], self.prevChiper[0]), tk.xorFunction(blockBit.bit[1], self.prevChiper[1]))
            encrypted = self.chiperEngine.encrypt(input)
            chiperBit = Block((encrypted[0], encrypted[1], 16), Block.BIT)
            chiperByte = chiperBit.byte

        self.prevChiper = encrypted

        return chiperByte, length

    def decrypt(self, chiperByte, length):

        #transform into bit matrix
        chiperBit = Block(chiperByte, Block.BYTE)

        if (self.firstDecrypt):
            decrypted = self.chiperEngine.decrypt(chiperBit.bit)
            blockBit = Block((decrypted[0],decrypted[1], length), Block.BIT)
            blockByte = blockBit.byte[:length]
            self.firstDecrypt = False
        else:
            decrypted = self.chiperEngine.decrypt(chiperBit.bit)
            tk = Toolkit()
            decrypted = (tk.xorFunction(decrypted[0], self.prevChiper[0]), tk.xorFunction(decrypted[1], self.prevChiper[1]))
            blockBit = Block((decrypted[0], decrypted[1], length), Block.BIT)
            blockByte = blockBit.byte[:length]

        self.prevChiper = chiperBit.bit

        return blockByte, length
