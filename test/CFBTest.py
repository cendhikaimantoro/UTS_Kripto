from src.algorithm.Toolkit import Toolkit
from src.mode.CBC import CBC
from src.architecture.FeistelNetwork import FeistelNetwork
from src.mode.CipherBlockASRCI import CipherBlockASRCI

class CFBTest(object):
    def testCFB(self):

        key = "Tugas Pengganti UTS Kriptografi"
        cb = CipherBlockASRCI(key)
        encrypted = cb.CFBmode(b"Pak Rinaldi Mengajar kelas kriptografi IF4020 tahun 2017 - 2018",'e')
        print(encrypted)

        decrypted = cb.CFBmode(encrypted,'d')
        print(decrypted)
    def execute(self):
        print("=========================================")
        self.testCFB()
        print("=========================================")

test = CFBTest()
test.execute()
