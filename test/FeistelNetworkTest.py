from src.algorithm.Toolkit import Toolkit
from src.algorithm.Block import Block
from src.architecture.FeistelNetwork import FeistelNetwork


class FeistelTest(object):
    def testFeistel(self):

        key = "Tugas Pengganti UTS Kriptografi"

        tk = Toolkit()

        fn = FeistelNetwork(tk.roundKey(key),tk.roundFunction, tk.xorFunction)

        value1 = bytearray(b'CendhikaImantoro')
        block1 = Block(value1, Block.BYTE)
        print("Block 1")
        print("length : ", block1.length)
        print("byte : ", bytes(block1.byte))
        for i in range(8):
            print(block1.bit[0][i], "      ", block1.bit[1][i])

        encrypted = fn.encrypt(block1.bit)
        print("Encrypted")
        for i in range(8):
            print(encrypted[0][i], "      ", encrypted[1][i])

        decrypted = fn.decrypt(encrypted)
        print("Decrypted")
        for i in range(8):
            print(decrypted[0][i], "      ", decrypted[1][i])

        block2 = Block((decrypted[0],decrypted[1], 16), Block.BIT)

        print("Block 2")
        print("length : ", block2.length)
        print("byte : ", bytes(block2.byte))
        for i in range(8):
            print(block2.bit[0][i], "      ", block2.bit[1][i])

    #untuk kustomisasi pesan di level bit dan key di level karakter
    def testFeistel2(self):
        key1 = "<INSERT YOUR KEY HERE>"
        key2 = "<INSERT yOUR KEY HERE>"

        plain1 = [[[0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0]],

                 [[0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0]]]

        plain2 = [[[1, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0]],

                  [[0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0]]]

        tk = Toolkit()
        fn1 = FeistelNetwork(tk.roundKey(key1), tk.roundFunction, tk.xorFunction)
        fn2 = FeistelNetwork(tk.roundKey(key2), tk.roundFunction, tk.xorFunction)

        print("==============================================================")

        print("PLAIN1")
        for i in range(8):
            print(plain1[0][i], " ", plain1[1][i])
        print()

        print("PLAIN2")
        for i in range(8):
            print(plain2[0][i], " ", plain2[1][i])
        print()

        print("KEY1")
        print(key1)
        print()

        print("KEY2")
        print(key2)
        print()

        print("==============================================================")

        print("PLAIN1 KEY1")
        encrypted1 = fn1.encrypt(plain1)
        for i in range(8):
            print(encrypted1[0][i], " ", encrypted1[1][i])
        print()

        print("PLAIN2 KEY1")
        encrypted2 = fn1.encrypt(plain2)
        for i in range(8):
            print(encrypted2[0][i], " ", encrypted2[1][i])
        print()

        print("PLAIN2 KEY2")
        encrypted3 = fn2.encrypt(plain2)
        for i in range(8):
            print(encrypted3[0][i], " ", encrypted3[1][i])
        print()

        print("PLAIN1 KEY2")
        encrypted4 = fn2.encrypt(plain1)
        for i in range(8):
            print(encrypted4[0][i], " ", encrypted4[1][i])
        print()


    def execute(self):
        print("=========================================")
        self.testFeistel()
        print("=========================================")
        self.testFeistel2()



test = FeistelTest()
test.execute()
