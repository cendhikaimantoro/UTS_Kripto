from src.mode.CipherBlockASRCI import CipherBlockASRCI
import collections
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams.update({'font.size': 5})

class CounterTest(object):
    def testCounter(self):
        key = "Tugas Pengganti UTS Kriptografi"
        cb = CipherBlockASRCI(key)
        encrypted = cb.CounterMode(b"Pak Rinaldi Mengajar kelas kriptografi IF4020 tahun 2017 - 2018 Ade dan Cendhika mengerjakan tugas besar pengganti UTS mereka dengan sungguh - sungguh", 'e')
        print(encrypted)
        col = collections.Counter(encrypted)
        print(col)
        plt.bar(range(len(col)), list(col.values()), align='center')
        plt.xticks(range(len(col)), list(col.keys()))
        plt.show()
        decrypted = cb.CounterMode(encrypted, 'd')
        print(decrypted)

    def execute(self):
        print("=========================================")
        self.testCounter()
        print("=========================================")

test = CounterTest()
test.execute()
