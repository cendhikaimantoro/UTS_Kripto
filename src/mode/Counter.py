from src.algorithm.Block import Block
from src.algorithm.Toolkit import Toolkit

class Counter(object):
    def __init__(self,chiperEngine):
        self.chiperEngine = chiperEngine
        self.initCounter()

    def initCounter(self):
        self.counter = 0

    def encrypt(self, blockByte):
        self.initCounter()
        length = len(blockByte)

        # assertion
        if length > 16:
            print("KABOOOMM!!!! Block too big")
        blockBit = Block(blockByte, Block.BYTE)
        tk = Toolkit()
        encrypted = self.chiperEngine.encrypt(tk.counter(self.counter))
        self.counter += 1
        input = (tk.xorFunction(blockBit.bit[0], encrypted[0]), tk.xorFunction(blockBit.bit[1], encrypted[1]))
        chiperBit = Block((input[0], input[1], 16), Block.BIT)
        chiperByte = chiperBit.byte

        return chiperByte, length

    def decrypt(self,blockByte,length):
        self.initCounter()
        blockBit = Block(blockByte, Block.BYTE)
        tk = Toolkit()
        encrypted = self.chiperEngine.encrypt(tk.counter(self.counter))
        self.counter += 1
        input = (tk.xorFunction(blockBit.bit[0], encrypted[0]), tk.xorFunction(blockBit.bit[1], encrypted[1]))
        chiperBit = Block((input[0], input[1], 16), Block.BIT)
        chiperByte = chiperBit.byte

        return chiperByte, length