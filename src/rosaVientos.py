# _*_ coding: utf-8 *_*
# Autor: Darwin Rosero Vaca
# Descripción:

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm
from math import pi
from windrose import WindroseAxes
import matplotlib.patches as mpatches


class graficar():
    """Esta clase genera graficos deversos"""

    def __init__(self, ):
        """Constructor for graficar"""

    def windRouse(self, archvo):
        # creamos datos de direcion y velocidad
        ws = np.random.random(500) * 10
        print(len(ws), " ", ws)
        wd = np.random.random(500) * 360  # [x*30 for x in range(0,12)]
        print(len(wd), " ", wd)
        # A stacked histogram with normed(displayed in percent) results:
        ax = WindroseAxes.from_ax()
        ax.bar(wd, ws, normed=True, opening=0.8, edgecolor='white')
        ax.set_legend()
        plt.show()
        # A windrose in filled representation, with a controled colormap
        # …or without filled regions
        ax = WindroseAxes.from_ax()
        ax.contour(wd, ws, bins=np.arange(0, 8, 1), cmap=cm.hot, lw=3)
        ax.set_legend()
        plt.show()
        print("###############################################################")
        print("###############################################################")
        print("###############################################################")

    def polarGraf(self):
        ax = plt.axes([0.025, 0.025, 0.95, 0.95], polar=True)
        print("Polar axes = ", ax)
        N = 12
        grados = [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330]
        # [0.0,0.52359878,1.04719755,1.57079633,2.0943951, 2.61799388,3.14159265,3.66519143,4.1887902,4.71238898,5.23598776,5.75958653]
        # largo de la barra
        theta = [-1, 2, 3, 5, -2, 6, 4, -2, 6, -5, -2, 3]  # np.arange(0.0, 2 * np.pi, 2 * np.pi / N)
        print("theta", theta)
        ##largo de la barra
        radii = [2, 3, 5] * 4  # [x * pi/180 for x in grados] #10 * np.random.rand(N)
        print("radii", radii, len(radii))
        # ancho de la barra
        # width =[0.1]*12# np.pi / 4 * np.random.rand(N)
        # print("width",width)
        bars = plt.bar(theta, radii, width=0.3, bottom=3)

        for r, bar in zip(radii, bars):
            print(r)
            bar.set_facecolor(plt.cm.jet(r / 10.))
            # print(plt.cm.jet(r / 10.))
            bar.set_alpha(0.5)
        plt.show()
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        plt.show()

    def variTem(self):
        """grafica circular de las anomalìas de temperatura"""

        #plt.subplot(111,projection="aitoff")

        # carga los datos en un Dataframe
        datos = pd.read_csv(archivo, delimiter=";")
        dire = [90, 60, 30, 0, 330, 300, 270, 240, 210, 180, 150, 120]

        pos = [x * pi / 180 for x in dire]

        ##recorre los años
        for a in datos.columns[1:]:
            fig = plt.figure(figsize=(6.5, 7))
            ax = plt.axes([0.12, 0.07, 0.75, 0.75], polar=True)
            print("graficando el año" ,a)
            serie = datos[a]

            lab=['ENE', 'FEB', 'MAR', 'ABR', 'MAY', 'JUN', 'JUL', 'AGO','SEP','OCT','NOV','DIC']
            plt.xticks(pos, lab, rotation=30)
            ax.set_title("Variación de temperatura para el año :\n"+a+'\n', fontsize="15", color="black")
            ax.set_rlabel_position(90)  # Move radial labels away from plotted line
            #ax.grid(True)
            #ax.text(2.45 , 1.35, "Año "+str(a), fontsize=9,bbox={'facecolor':'white', 'alpha':1, 'pad':2})
            plt.margins(0.5)
            plt.subplots_adjust(top=0.5)
            # graficando las variaciones
            bars = plt.bar(pos, serie, width=0.4, bottom=1)
            #ax.set_rorigin(-2.5)
            for r, bar in zip(serie, bars):
                # print(r, bar)
                if r < 0:
                    bar.set_facecolor('blue')
                else:
                    bar.set_facecolor('red')
                # bar.set_alpha(1)
            #Agregando leyendas
            #print("Xlim value ", ax.get_xlim())
            #positivo = mpatches.Patch(color='red', label='positiva')
            #negativo = mpatches.Patch(color='blue', label='negativa')
            #plt.legend(handles=[positivo,negativo], loc=0,title="Variación ")
            #plt.title(a,fontsize=15)
            plt.savefig("../"+a+".png",y=50)
            plt.close()
        #plt.show()

    def polarEje(self):
        theta = np.linspace(0, 2 * np.pi)
        r = 5 + 50 * theta

        fig = plt.figure()
        ax = fig.add_subplot(111, projection="polar")
        ax.plot(theta, r)

        plt.show()
        theta = np.linspace(0, 2 * np.pi, 1000)
        print(theta)
        r = 5 * np.cos(5 * theta)

        fig = plt.figure()
        ax = fig.add_subplot(111, projection="polar")
        ax.plot(theta, r, color="#ffb6c1", linewidth=3)
        plt.show()

    def bubblePolar(self):
        # otra gráfica polar

        # Fixing random state for reproducibility
        np.random.seed(19680801)

        # Compute areas and colors
        N = 150
        r = 2 * np.random.rand(N)
        theta = 2 * np.pi * np.random.rand(N)
        area = 50 * r ** 2
        colors = theta

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='polar')
        c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)
        plt.show()

        ####otra mas
        fig = plt.figure()
        ax = fig.add_subplot(111, polar=True)
        c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)


        ax.set_rorigin(3)
        ax.set_theta_zero_location('W', offset=10)
        plt.show()


g = graficar()
archivo = "/media/drosero/Datos/Desarrollo/Python/infRW.csv"
#g.polarGraf()
#g.bubblePolar()
# g.windRouse(archivo)
g.variTem()
#g.polarEje()
