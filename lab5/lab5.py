import math as m
import numpy as np

matrix = []
with open("../Lab_03/australian.dat","r") as file:
    matrix = [list(map(lambda a: float(a),line.split())) for line in file]
    
matrix_2 = [x[:14] for x in matrix] #matrix without decission
print(srednia_aryt(matrix_2[0]))
print(wariancja(matrix_2[0]))
print(odchylenie_std(matrix_2[0]))


def srednia_aryt_matrix(lista):
    ones = np.ones((len(lista),1))
    return float(1/len(lista))*np.dot(np.array(lista),ones)[0]

def wariancja_matrix(lista):
    srednia = srednia_aryt_matrix(lista)
    ones = np.ones((1,len(lista)))*srednia
    minus = np.array(lista) - ones
    return float(1/len(lista))*np.dot(minus[0],minus[0].T)

def odchylenie_std_matrix(lista):
    return m.sqrt(wariancja_matrix(lista))

print(srednia_aryt_matrix(matrix_2[0]))
print(wariancja_matrix(matrix_2[0]))
print(odchylenie_std_matrix(matrix_2[0]))
