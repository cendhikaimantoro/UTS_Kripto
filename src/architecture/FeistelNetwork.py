class FeistelNetwork(object):

    NORMAL = 0
    REVERSE = 1

    def __init__(self, roundKey, roundFunction, xorFunction):
        self.roundKey = roundKey
        self.roundFunction = roundFunction
        self.xorFunction = xorFunction

    def process(self, block, order):
        left = [[block[0][i][j] for j in range(8)] for i in range(8)]
        right = [[block[1][i][j] for j in range(8)] for i in range(8)]

        nextLeft = right
        nextRight = left


        for i in range(len(self.roundKey)):

            if (order == self.NORMAL):
                key = self.roundKey[i]
            elif order == self.REVERSE:
                key = self.roundKey[len(self.roundKey)-1-i]

            currentRight = nextLeft
            currentLeft = nextRight

            nextRight = currentRight
            nextLeft = self.xorFunction(currentLeft, self.roundFunction(key, currentRight))

        return (nextLeft, nextRight)

    def encrypt(self,block):
        return self.process(block, self.NORMAL)

    def decrypt(self,block):
        return self.process(block, self.REVERSE)