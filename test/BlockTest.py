from src.algorithm.Block import Block


class BlockTest(object):
    def testConstructor(self):
        value1 = bytearray(b'CendhikaImantoro')
        block1 = Block(value1, Block.BYTE)
        print("Block 1")
        print("length : ", block1.length)
        print("byte : ", bytes(block1.byte))
        for i in range(8):
            print(block1.bit[0][i], "      ", block1.bit[1][i])

        block2 = Block((block1.bit[0],block1.bit[1], block1.length), Block.BIT)

        print("Block 2")
        print("length : ", block2.length)
        print("byte : ", bytes(block2.byte))
        for i in range(8):
            print(block2.bit[0][i], "      ", block2.bit[1][i])

        value1 = bytearray(b'Ade Surya R')
        block1 = Block(value1, Block.BYTE)
        print("Block 1")
        print("length : ", block1.length)
        print("byte : ", bytes(block1.byte))
        for i in range(8):
            print(block1.bit[0][i], "      ", block1.bit[1][i])

        block2 = Block((block1.bit[0], block1.bit[1], block1.length), Block.BIT)

        print("Block 2")
        print("length : ", block2.length)
        print("byte : ", bytes(block2.byte))
        for i in range(8):
            print(block2.bit[0][i], "      ", block2.bit[1][i])

    def execute(self):
        print("=========================================")
        self.testConstructor()
        print("=========================================")



test = BlockTest()
test.execute()
