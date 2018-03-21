# _*_ coding: utf-8 *_*
#Autor: Darwin Rosero Vaca
#Descripción:

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm
from math import pi
from windrose import WindroseAxes

class graficar():
    """Esta clase genera graficos deversos"""

    def __init__(self,):
        """Constructor for graficar"""

    def windRouse(self,archvo):
        print("archivo")
        datos=pd.read_csv(archivo,delimiter=";")
        datos['direc']=range(0,12)
        datos['direc'] = datos['direc'] * 30
        datos['eje_x'] = datos['1901'] * np.sin(datos['direc']* pi / 180)
        datos['eje_y'] = datos['1901'] * np.cos(datos['direc'] * pi / 180)
        fig, ax = plt.subplots(figsize=(8, 8), dpi=80)
        x0, x1 = ax.get_xlim()
        y0, y1 = ax.get_ylim()
        ax.set_aspect('equal')
        _ = datos.plot(kind='scatter', x='eje_x', y='eje_y', alpha=0.35, ax=ax)
        plt.show()
        ax = WindroseAxes.from_ax()
        ax.bar(datos['direc'],datos['2010'], normed=True, opening=0.8, edgecolor='white')
        ax.set_legend()
        plt.show()
        ax = WindroseAxes.from_ax()
        ax.box(datos['direc'],datos['2010'], bins=np.arange(0, 8, 1))
        ax.set_legend()
        plt.show()
        ax = WindroseAxes.from_ax()
        ax.contourf(datos['direc'],datos['2010'], bins=np.arange(0, 8, 1), cmap=cm.hot)
        ax.set_legend()
        plt.show()
        ax = WindroseAxes.from_ax()
        ax.contourf(datos['direc'],datos['2010'], bins=np.arange(0, 8, 1), cmap=cm.hot)
        ax.set_legend()
        plt.show()


        print(datos)

    def polarGraf(self):
        ax = plt.axes([0.025, 0.025, 0.95, 0.95], polar=True)
        print("Polar axes = ",ax)
        N = 20
        theta = np.arange(0.0, 2 * np.pi, 2 * np.pi / N)
        print("theta",theta)
        radii = 10 * np.random.rand(N)
        print("radii",radii)
        width = np.pi / 4 * np.random.rand(N)
        print("width",width)
        bars = plt.bar(theta, radii, width=width, bottom=0.0)

        for r, bar in zip(radii, bars):
            bar.set_facecolor(plt.cm.jet(r / 10.))
            bar.set_alpha(0.5)

        ax.set_xticklabels([])
        ax.set_yticklabels([])
        plt.show()
        #otra gráfica polar

        # Fixing random state for reproducibility
        np.random.seed(19680801)

        # Compute areas and colors
        N = 150
        r = 2 * np.random.rand(N)
        theta = 2 * np.pi * np.random.rand(N)
        area = 200 * r ** 2
        colors = theta

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='polar')
        c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)
        #plt.show()

        ####otra mas
        fig = plt.figure()
        ax = fig.add_subplot(111, polar=True)
        c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)

        ax.set_rorigin(-2.5)
        ax.set_theta_zero_location('W', offset=10)
        #plt.show()


g=graficar()
archivo="/media/drosero/Datos/Desarrollo/Python/infRW.csv"
g.polarGraf()
#g.windRouse(archivo)