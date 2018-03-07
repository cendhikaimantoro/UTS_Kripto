from src.algorithm.Toolkit import Toolkit
from src.mode.ECB import ECB
from src.architecture.FeistelNetwork import FeistelNetwork


class ECBTest(object):
    def testECB(self):

        key = "Tugas Pengganti UTS Kriptografi"

        tk = Toolkit()

        fn = FeistelNetwork(tk.roundKey(key),tk.roundFunction, tk.xorFunction)

        ecb = ECB(fn)

        encrypted, length = ecb.encrypt(bytearray(b'Ade Surya R'))

        print("Encrypted")
        print("Length : ", length)
        print(encrypted)

        decrypted = ecb.decrypt(encrypted, length)
        print("Decrypted")
        print(decrypted)

    def execute(self):
        print("=========================================")
        self.testECB()
        print("=========================================")



test = ECBTest()
test.execute()
