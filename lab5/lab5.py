import numpy as np

def wczytanie(filename):
    dane = []
 
    with open(filename, 'r') as data:
        for wiersz in data:
            dane.append(list(map(lambda e : float(e), wiersz.replace('\n', '').split(' '))))
            
    return dane

matrix=wczytanie("australian.dat")

matrix_2 = [x[:14] for x in matrix] #matrix without decission

def srednia_aryt_matrix(lista):
    ones = np.ones((len(lista),1))
    return float(1/len(lista))*np.dot(np.array(lista),ones)[0]

def wariancja_matrix(lista):
    srednia = srednia_aryt_matrix(lista)
    ones = np.ones((1,len(lista)))*srednia
    minus = np.array(lista) - ones
    return float(1/len(lista))*np.dot(minus[0],minus[0].T)

def odchylenie_std_matrix(lista):
    return (wariancja_matrix(lista))**(1/2)

print(srednia_aryt_matrix(matrix_2[0]))
print(wariancja_matrix(matrix_2[0]))
print(odchylenie_std_matrix(matrix_2[0]))
