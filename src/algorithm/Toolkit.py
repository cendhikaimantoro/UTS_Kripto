class Toolkit(object):
    def __init__(self):
        pass

    def roundFunction(self, roundkey, halfblock):
        return self.transposition(roundkey,self.subtitution(roundkey,halfblock))

    def subtitution(self, roundkey, halfblock):
        ret = [[0 for i in range(8)] for j in range(8)]
        for i in range(8):
            for j in range(8):
                idx = roundkey[(i + 1) % 8][j]
                ret[i][j] = (ret[i][j] + halfblock[idx // 8][idx % 8])%2
                idx = roundkey[(i + 7) % 8][j]
                ret[i][j] = (ret[i][j] + halfblock[idx // 8][idx % 8])%2
                idx = roundkey[i][(j + 1) % 8]
                ret[i][j] = (ret[i][j] + halfblock[idx // 8][idx % 8])%2
                idx = roundkey[i][(j + 7) % 8]
                ret[i][j] = (ret[i][j] + halfblock[idx // 8][idx % 8])%2
        return ret

    def transposition(self, roundkey, halfblock):
        # shift x
        copy = halfblock
        shift = [0 for i in range(8)]
        for i in range(8):
            sum = 0
            for j in range(8):
                sum=(sum+roundkey[i][j])%8
            shift[i] = sum

        ret = [[0 for i in range(8)] for j in range(8)]
        for i in range(8):
            for j in range(8):
                ret[i][j] = copy[i][(j+8-shift[i])%8]

        #shift y
        copy = ret
        shift = [0 for i in range(8)]
        for i in range(8):
            sum = 0
            for j in range(8):
                sum = (sum + roundkey[j][i]) % 8
            shift[i] = sum

        ret = [[0 for i in range(8)] for j in range(8)]
        for i in range(8):
            for j in range(8):
                ret[i][j] = copy[(i +8- shift[j]) % 8][j]

        return ret

    def roundKey(self, key):

        #key to array(int)
        arr = bytearray(key, encoding='utf8')

        #count nRound
        sum = 0
        for i in range(len(arr)):
            sum = (sum + arr[i])%8
        nRound = 8 + sum

        #build round key
        ret = [[[0 for i in range(8)] for j in range (8)] for k in range(nRound)]
        sum = 0
        for i in range(nRound*8*8):
            sum = (sum + arr[i%len(arr)])%64
            ret[i//64][i%64//8][i%8] = sum

        return ret

    def xorFunction(self, l, r):
        ret = [[0 for i in range(8)] for j in range(8)]

        for i in range(8):
            for j in range(8):
                ret[i][j] = int(l[i][j] != r[i][j])
        return ret

    def counter(self, k):
        key = b'kriptografi'
        intSequence = []
        counter = 0
        for i in range(16):
            counter += int(key[i%len(key)])
            counter = counter % 256
            c = ((k+1) * counter) % 256
            intSequence.append(c)
        byteSequence = bytearray(intSequence)

        bitstream = bin(int.from_bytes(byteSequence, byteorder='big'))[2:]
        padding = '0' * ((8 - (len(bitstream) % 8)) % 8)
        bitstream = padding + bitstream

        bit = [[[0 for i in range(8)] for j in range(8)] for k in range(2)]
        for i in range(len(bitstream)):
            bit[i // 64][i % 64 // 8][i % 8] = int(bitstream[i])

        return bit