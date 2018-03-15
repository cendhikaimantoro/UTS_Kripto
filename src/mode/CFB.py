from src.algorithm.Block import Block
from src.algorithm.Toolkit import Toolkit

class CFB(object):
    def __init__(self,chiperEngine):
        self.chiperEngine = chiperEngine
        self.firstEnc = True
        self.firstDec = True

    def initQueue(self):
        self.queue = ([[1,0,1,0,1,0,1,0],[0,1,0,1,0,1,0,1],[1,0,1,0,1,0,1,0],[0,1,0,1,0,1,0,1],[1,0,1,0,1,0,1,0],[0,1,0,1,0,1,0,1],[1,0,1,0,1,0,1,0],[0,1,0,1,0,1,0,1]],[[1,0,1,0,1,0,1,0],[0,1,0,1,0,1,0,1],[1,0,1,0,1,0,1,0],[0,1,0,1,0,1,0,1],[1,0,1,0,1,0,1,0],[0,1,0,1,0,1,0,1],[1,0,1,0,1,0,1,0],[0,1,0,1,0,1,0,1]])

    def encrypt(self, blockByte):
        self.initQueue()
        length = len(blockByte)

        #assertion
        if length > 16:
            print("KABOOOMM!!!! Block too big")
        blockBit = Block(blockByte, Block.BYTE)
        encrypted = self.chiperEngine.encrypt(self.queue)
        tk = Toolkit()
        input = (tk.xorFunction(blockBit.bit[0], encrypted[0]),tk.xorFunction(blockBit.bit[1], encrypted[1]))
        chiperBit = Block((input[0], input[1], 16), Block.BIT)
        chiperByte = chiperBit.byte

        self.queue = chiperByte
        return chiperByte,length

    def decrypt(self,blockByte,length):
        self.initQueue()
        chiperBit = Block(blockByte, Block.BYTE)
        decrypted = self.chiperEngine.decrypt(self.queue)
        tk = Toolkit()
        input = (tk.xorFunction(chiperBit.bit[0], decrypted[0]),tk.xorFunction(chiperBit.bit[1], decrypted[1]))
        blockBit = Block((input[0], input[1], 16), Block.BIT)
        blockByte = blockBit.byte
        self.queue = blockByte
        return blockByte[:length],length