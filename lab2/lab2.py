import copy

def wyznacznik2x2(macierz):
    return (macierz[0][0]*macierz[1][1])-(macierz[0][1]*macierz[1][0])

def wyznacznik3x3(macierz):
    return (macierz[0][0]*macierz[1][1]*macierz[2][2])+(macierz[0][1]*macierz[1][2]*macierz[2][0])+(macierz[0][2]*macierz[1][0]*macierz[2][1])-((macierz[0][2]*macierz[1][1]*macierz[2][0])+(macierz[0][0]*macierz[1][2]*macierz[2][1])+(macierz[0][1]*macierz[1][0]*macierz[2][2]))  

def wyznacznik(macierz):
    lista=[]
    if len(macierz[0]) == 2:
        return wyznacznik2x2(macierz)
    if len(macierz[0]) == 3:
        return wyznacznik3x3(macierz)
    if len(macierz[0]) > 3:
        wyznacznik4x4=0
        pom=[]
        for z in range(0,4):
            for x in range(0,len(macierz[0])):
                wiersz=[]
                for y in range(0,len(macierz[0])):
                    if x != 0:
                        if y!= z:
                            wiersz.append(macierz[x][y])
                if len(wiersz) > 0:                       
                    pom.append(wiersz)
                wiersz=[]
            wynik=wyznacznik3x3(pom)
            wyznacznik4x4+=wynik*macierz[0][z]*((-1)**(0+z))
            print(pom)
            pom=[]
        return wyznacznik4x4                

matrix=[[4,2,-5,8],[1,1,-2,0],[4,0,0,0],[3,-1,-2,4]]                
print(wyznacznik(matrix))  

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

