from src.algorithm.Toolkit import Toolkit
from src.mode.CBC import CBC
from src.architecture.FeistelNetwork import FeistelNetwork
from src.mode.CipherBlockASRCI import CipherBlockASRCI
import collections
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams.update({'font.size': 5})

class CFBTest(object):
    def testCFB(self):

        key = "Tugas Pengganti UTS Kriptografi"
        cb = CipherBlockASRCI(key)
        encrypted = cb.CFBmode(b"Pak Rinaldi Mengajar kelas kriptografi IF4020 tahun 2017 - 2018 Ade dan Cendhika mengerjakan tugas besar pengganti UTS mereka dengan sungguh - sungguh",'e')
        print(encrypted)
        col = collections.Counter(encrypted)
        print(col)
        plt.bar(range(len(col)), list(col.values()), align='center')
        plt.xticks(range(len(col)), list(col.keys()))
        plt.show()
        decrypted = cb.CFBmode(encrypted,'d')
        print(decrypted)
    def execute(self):
        print("=========================================")
        self.testCFB()
        print("=========================================")

test = CFBTest()
test.execute()
