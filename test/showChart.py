import collections
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams.update({'font.size': 5})
encrypted = b"Pak Rinaldi Mengajar kelas kriptografi IF4020 tahun 2017 - 2018 Ade dan Cendhika mengerjakan tugas besar pengganti UTS mereka dengan sungguh - sungguh"
col = collections.Counter(encrypted)
print(col)
plt.bar(range(len(col)), list(col.values()), align='center')
plt.xticks(range(len(col)), list(col.keys()))
plt.show()