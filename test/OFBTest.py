from src.mode.CipherBlockASRCI import CipherBlockASRCI
import collections
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams.update({'font.size': 5})

class OFBTest(object):
    def testOFB(self):

        key = "Tugas Pengganti UTS Kriptografi"
        cb = CipherBlockASRCI(key)
        encrypted = cb.OFBmode(b"Pak Rinaldi Mengajar kelas kriptografi IF4020 tahun 2017 - 2018 Ade dan Cendhika mengerjakan tugas besar pengganti UTS mereka dengan sungguh - sungguh",'e')
        print(encrypted)
        col = collections.Counter(encrypted)
        print(col)
        plt.bar(range(len(col)), list(col.values()), align='center')
        plt.xticks(range(len(col)), list(col.keys()))
        plt.show()
        decrypted = cb.OFBmode(encrypted,'d')
        print(decrypted)
    def execute(self):
        print("=========================================")
        self.testOFB()
        print("=========================================")

test = OFBTest()
test.execute()
