import numpy as np

def projekcja(u,v):
    u_v = np.dot(u.T,v)
    u_u = np.dot(u.T,u)
    if u_u==0:
        return u
    return (u_v/u_u)*u

a=np.array([[1,2],
            [2,1],  
            [1,0]])
        
def QR(matrix):
    lista=[]
    for i in range(len(a[1])):
        lista_pom=[]
        for x in a:
            lista_pom.append(x[i])
        lista1.append(lista_pom)    
    
    lista1 = []
    q = []

    for v in lista:
        v = np.array(v)
        projekcje = 0
        for u in lista1:
            u = np.array(u)
            projekcje+=projekcja(u, v)
        u = v - projekcje
        lista1.append(u)
        if np.linalg.norm(u)==0:
            e=u
        else:
            e = (1/np.linalg.norm(u))*u
        q.append(e)    
        
    q = np.array(q).T
    r = np.dot(q.T,a)
    a = np.dot(q,r)
            
    print(q,r,a)

QR(a)    
