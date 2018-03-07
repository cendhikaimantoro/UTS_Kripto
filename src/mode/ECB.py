from src.algorithm.Block import Block

class ECB(object):

    def __init__(self, chiperEngine):
        self.chiperEngine = chiperEngine

    def encrypt(self, blockByte):
        length = len(blockByte)

        #assertion
        if length > 16:
            print("KABOOOMM!!!! Block too big")

        #transform into bit matrix
        blockBit = Block(blockByte, Block.BYTE)

        encrypted = self.chiperEngine.encrypt(blockBit.bit)
        chiperBit = Block((encrypted[0],encrypted[1],16), Block.BIT)
        chiperByte = chiperBit.byte

        return chiperByte, length

    def decrypt(self, chiperByte, length):

        #transform into bit matrix
        chiperBit = Block(chiperByte, Block.BYTE)

        decrypted = self.chiperEngine.decrypt(chiperBit.bit)
        blockBit = Block((decrypted[0],decrypted[1], length), Block.BIT)
        blockByte = blockBit.byte[:length]

        return blockByte
