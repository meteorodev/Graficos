# -*- coding: utf-8 *-*
import csv
import pprint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def readCsv(ruta):
    with open(ruta) as f:
        reader = csv.reader(f)
        #for row in reader:
        #    print(row)

        #pprint.pprint(list(reader))


readCsv('/media/drosero/Datos/QGIS/Niña/datosTrim/VarTnSierra.csv')

file = r'/media/drosero/Datos/QGIS/Niña/porRegion/VarRRCosta.csv'

df = pd.read_csv(file, delimiter=",")
columns=df.keys().tolist()
print(len(columns), columns)
var = df[columns[6]].tolist()
colIndexp1 = np.arange(7, 20)
print(colIndexp1)

for i in range(6,19):
    var=df[columns[i]].tolist()
    plt.plot(var, label=str(columns[i]))
    print(str(columns[i]))
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.title("Anomalía de temperatura 1973-1976")
plt.show()

