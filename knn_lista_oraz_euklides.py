file = open("australian.dat","r")

def wczytaj(file):
  lista = []
  for line in file:
      row = line.split()
      lista.append(list(map(lambda x: float(x),row)))
  return lista      


def euklides(lista,lista1):
    suma = 0
    for i in range(len(lista)-1):
        suma += (lista[i] - lista1[i]) ** 2
    return suma ** 0.5

def grupowanie(decyzja,lista):
    slown ={}
    for x in range(1,len(lista)):
        c=lista[x][decyzja]
        if c in slown:
            slown[c].append(euklides(lista[0], lista[x]))
        else:
            slown[c]=[euklides(lista[0], lista[x])]
    return slown  

def sortowanie(lista,k):
    slow = dict()
    for ele in lista:
        decyzja = ele[0]
        if decyzja in slow.keys():
            slow[decyzja].append(ele[1])
        else:
            slow[decyzja]=[ele[1]] 
    for key in slow.keys():
        slow[key].sort()
    for key in slow.keys():
        suma = 0
        for ele in slow[key][:k]:
            suma+= ele
        slow[key]=suma
    return slow

def knn_lista(lista,decyzja,nowy):
    slow = []
    for x in range(len(lista)):
        decyzja1 = lista[x][decyzja]
        slow.append((decyzja1,euklides(nowy, lista[x])))    
    return slow

def min_odleglosc(slow):
    pom = 1
    min = slow[list(slow.keys())[0]]
    for key,value in slow.items():
        if min > value:
            min = value
            pom1 = key
            pom=1
        elif min == slow[key]:
            pom+=1
    if pom == 1:        
        return pom1
