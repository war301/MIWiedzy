import copy

file = open("australian.dat","r")

def wczytaj(file):
  lista = []
  for line in file:
      row = line.split()
      lista.append(list(map(lambda x: float(x),row)))
  return lista      


def metryka_euklidesowa(listaA,listaB):
    suma = 0
    for i in range(len(listaA)-1):
        suma += (listaA[i] - listaB[i]) ** 2
    return suma ** 0.5


y = lista[0]
slownik = {}

for element in lista [1:]:
    if slownik.get(element[-1]) == None:
        slownik[element[-1]] = [metryka_euklidesowa(element,y)]
    else:
        slownik[element[-1]].append(metryka_euklidesowa(element,y))


for key, value in slownik.items():
    print(key,value)

x=lista[0]

def oblicz(x,lista):
    slown ={}
    for para in lista:
        c=para[0]
        if c in slown:
            slown[c].append(para[1])
        else:
            slown[c]=[]
        slown[c].append(para[1])
    return slown
