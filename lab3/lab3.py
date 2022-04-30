import numpy as np
import matplotlib as plot
import random

for x in range(5):
    print(australia[x])
    
#tablica z nazwami, lambda ucina wszystkie poza pierwszymi 3 literkami
miasta=["olsztyn","gdansk","warszawa","klodzko"]
result = map(lambda x: x[:3],miasta)
print(list(result))

def euklides_vector(lista1,lista2):
    v1=np.array(lista1)
    v2=np.array(lista2)
    c=v1-v2
    return mat.sqrt(np.dot(c,c))
