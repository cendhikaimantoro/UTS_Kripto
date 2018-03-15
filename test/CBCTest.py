from src.algorithm.Toolkit import Toolkit
from src.mode.CBC import CBC
from src.architecture.FeistelNetwork import FeistelNetwork
from src.mode.CipherBlockASRCI import CipherBlockASRCI

class CBCTest(object):
    def testCBC(self):

        key = "Tugas Pengganti UTS Kriptografi"
        cb = CipherBlockASRCI(key)
        encrypted = cb.CBCmode(b"Pak Rinaldi Mengajar kelas kriptografi IF4020 tahun 2017 - 2018",'e')
        print(encrypted)

        decrypted = cb.CBCmode(encrypted,'d')
        print(decrypted)
    def execute(self):
        print("=========================================")
        self.testCBC()
        print("=========================================")

test = CBCTest()
test.execute()
