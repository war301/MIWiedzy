import numpy as np

#samemu

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

#na podstawie intenetu

def wyznacznik(A):
    wynik=0
    indeksy=list(range(len(A)))

    if(len(indeksy)==2):
        return A[0][0]*A[1][1]-A[0][1]*A[1][0]
    else:
        for ind in indeksy:
            ac=A.copy()
            ac=ac[1:]
            height=len(ac)
            for i in range(height):
                
                ac[i]=ac[i][0:ind]+ac[i][ind+1:]

            znak=(-1)**(ind%2)
            podmacierz = wyznacznik(ac)
            wynik+=znak*podmacierz*A[0][ind]    
    return wynik

test1=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
test2=[[1,2,3,4,1],[8,5,6,7,2],[9,12,10,11,3],[13,14,16,15,4],[10,8,6,4,2]]
A=[[-2,2,-3],[-1,5,3],[2,0,-1]]
print(wyznacznik(A))  
print("to",np.linalg.det(A))
print(wyznacznik(test1)) 
print("to",np.linalg.det(test1))   
print(wyznacznik(test2))    
print("to",np.linalg.det(test2))  
