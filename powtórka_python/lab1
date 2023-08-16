print('ala {0} {1}'.format("ma","kota"))
#imie=input("podeaj swoje imie")
#print(imie[::2])
h='2'
r=2
g=23.23
print(type(h),type(r),type(g))
mylist=["czemu","nie","to"]
print("jak tak ".join(mylist))
print("jak tak ".join(mylist).split())
miw="Metody inżynierii wiedzy są najlepsze"
print(len(miw))
miw=miw.replace("ą","a")
miw=miw.replace("ż","z")
print(miw)
miw=miw.replace(" ","")
print(miw)
print(len(miw))
dlugosc=set(miw)
print(len(dlugosc))
zmien1="czemu on"
zmien=1
zmien2=(zmien,zmien1)
print(zmien2,type(zmien2))
lista1=[1,2,3,4,5]
lista2=["q","w","e","r","t"]
lista12=lista1+lista2
print(lista12)
print(lista12[3:4],type(lista12[3:4]))
print(lista12[-6])
print(lista1.index(5))
lista11=[1,2,3,4,5]
lista22=[6,7,8,9,0]
lista11.extend(lista22)
print(lista11)
lista11.append(lista1)
print(lista11)
dic={"polska":"warszawa","niemcy":"berlin","rosja":"moskwa","bialorus":"minsk","slowacja":"bratyslawa"}
dic1={1:"warszawa",4:"berlin",3:"moskwa",7:"minsk",5:"bratyslawa"}
print(dic)
print(dic.items())
print(dic.values())
print(sorted(dic1.items(), key=lambda x: x[0]))
print(sorted(dic.items(), key=lambda x: x[1]))
import numpy as np 
macierz=np.array([[1,2,3]
                 ,[4,5,6]
                 ,[7,8,9]])
matrix=np.linalg.det(macierz)
print(matrix) 
matrix1=np.linalg.inv(macierz)
print(matrix1)

print(bool(' '))
print(bool(''))
print(bool(0))
print(bool(1))
print(bool('0'))
print(bool('1'))
print(bool([]))
print(bool([',']))

ciag_znakow = 'no simea'

if 'a' in ciag_znakow:
    print('jest a')
else:
    print('nie ma a ')

for i in range(21):
    print(i)

napis='na co się gapisz'
dodatek=''
listek=[]

for litera in napis:
    if litera == ' ':
        listek.append(dodatek)
        dodatek=''
    else:
        dodatek += litera
if dodatek != '':
    listek.append(dodatek)

print(listek)

haslo= 'Haslomaslo123!'

def sprawdź_haslo(haslo):
    dlugo = duza = specjalne = False

    if len(haslo) >=10:
        dlugo = True

    for litera in haslo:
        if litera.isupper():
            duza=True

    if '!' in haslo:
        specjalne=True

    if dlugo and duza and specjalne :
        print("haslo git")
    else:
        print("zle haslo")

sprawdź_haslo(haslo)

def jest_duza(litera):
    if ord(litera) >= 65 and ord(litera) <=90:
        return True
    else:
        return False

jest_duza("G")

next_lista=[1,2,3,99,12,99]

for i in next_lista:
    if i == '99':
        continue
    print('{} '.format(i))

def czy_nalezy(ele,lista):
    i=0
    help=False
    while i < len(lista):
        if ele == lista[i]:
            help = True
        i +=1
    return help 

print(czy_nalezy(12, next_lista))

file = open('costam.txt',"r")
print(file.read())
print(file.read(),end='')
