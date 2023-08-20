import numpy as np

def wczytanie(file):
    dane = []
    with open(file, 'r') as data:
        for line in data:
            row = line.split()
            dane.append(list(map(lambda x: float(x),row)))
    return dane 

matrix=wczytanie("australian.dat")
matrix1 = [x[:14] for x in matrix] 

def average(lista):
    ones = np.ones((len(lista),1))
    return float(1/len(lista))*np.dot(np.array(lista),ones)[0]

def covariance(lista):
    srednia = srednia_aryt_matrix(lista)
    ones = np.ones((1,len(lista)))*srednia
    minus = np.array(lista) - ones
    return float(1/len(lista))*np.dot(minus[0],minus[0].T)

def stan_dev(lista):
    return (wariancja_matrix(lista))**(1/2)

print(average(matrix1[0]))
print(covariance(matrix1[0]))
print(stan_dev(matrix1[0]))
