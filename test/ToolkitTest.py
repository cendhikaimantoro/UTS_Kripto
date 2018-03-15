from src.algorithm.Toolkit import Toolkit


class ToolkitTest(object):
    def testTransposition(self):
        key = [[int(i == 5) for i in range(8)] for j in range(8)]
        for i in range(8):
            print(key[i])
        print()

        input = [[int(i>0 and j>0 and i<7 and j<7) for i in range(8)]for j in range(8)]
        tk = Toolkit()

        out = tk.transposition(key,input)


        for i in range(8):
            print(out[i])

    def testSubtitution(self):
        key = [[8*j+i for i in range(8)] for j in range(8)]
        for i in range(8):
            print(key[i])
        print()

        input = [[int(i>0 and j>0 and i<7 and j<7) for i in range(8)]for j in range(8)]
        tk = Toolkit()

        out = tk.subtitution(key,input)


        for i in range(8):
            print(out[i])

    def testRoundFunction(self):
        key = [[(8 * j + i + int(i > 0 and j > 0 and i < 7 and j < 7))%64 for i in range(8)] for j in range(8)]
        for i in range(8):
            print(key[i])
        print()

        input = [[int(i > 0 and j > 0 and i < 7 and j < 7) for i in range(8)] for j in range(8)]
        tk = Toolkit()

        out = tk.roundFunction(key, input)

        for i in range(8):
            print(out[i])

    def testRoundKey(self):

        tk = Toolkit()

        out = tk.roundKey("Cendhika Imantoro - Ade Surya Ramadhani")

        for i in range(len(out)):
            for j in range(8):
                print(out[i][j])
            print()

    def testCounter(self):
        tk = Toolkit()
        for i in range(5):
            hashVal = tk.counter(i)
            for j in range(8):
                print(hashVal[0][j],hashVal[1][j])
            print()

    def execute(self):
        print("=========================================")
        self.testTransposition()
        print("=========================================")
        self.testSubtitution()
        print("=========================================")
        self.testRoundFunction()
        print("=========================================")
        self.testRoundKey()
        print("=========================================")
        self.testCounter()
        print("=========================================")



test = ToolkitTest()
test.execute()
