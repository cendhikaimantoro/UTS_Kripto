class Block(object):
    BYTE = 0
    BIT = 1
    def __init__(self, value, mode):
        #mode Byte, value byteArray
        if mode == self.BYTE:
            blockBytes = value
            if (len(blockBytes) > 16):
                print("KABOOOM!!!! WRONG BLOCK SIZE")

            self.length = len(blockBytes)
            self.byte = blockBytes

            bitstream = bin(int.from_bytes(self.byte, byteorder='big'))[2:]
            padding = '0'*((8-(len(bitstream)%8))%8)
            bitstream = padding+bitstream
            if (len(bitstream)%8 != 0):
                print("KABOOOM!!!! wrong bitstream size")

            self.bit = [[[0 for i in range(8)]for j in range(8)] for k in range(2)]
            for i in range (len(bitstream)):
                self.bit[i//64][i%64//8][i%8] = int(bitstream[i])
        # mode Bit, value (left, right, length)
        elif mode == self.BIT:
            self.bit = value[:2]
            self.length = value[-1]
            bitstream = ''
            for i in range(self.length*8):
                bitstream += str(self.bit[i//64][i%64//8][i%8])

            self.byte = bytearray(int(bitstream, 2).to_bytes(len(bitstream)//8,'big'))
