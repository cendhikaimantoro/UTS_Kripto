from src.mode.CipherBlockASRCI import CipherBlockASRCI

class CounterTest(object):
    def testCounter(self):
        key = "Tugas Pengganti UTS Kriptografi"
        cb = CipherBlockASRCI(key)
        encrypted = cb.CounterMode(b"Pak Rinaldi Mengajar kelas kriptografi IF4020 tahun 2017 - 2018", 'e')
        print(encrypted)

        decrypted = cb.CounterMode(encrypted, 'd')
        print(decrypted)

    def execute(self):
        print("=========================================")
        self.testCounter()
        print("=========================================")

test = CounterTest()
test.execute()
