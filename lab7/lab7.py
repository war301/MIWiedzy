import numpy as np

def projekcja(u,v):
    u_v = np.dot(u.T,v)
    u_u = np.dot(u.T,u)
    if u_u==0:
        return u
    return (u_v/u_u)*u

a=np.array([[1,2],
            [0,1],  
            [1,0]])
        
def QR(matrix):
    v_list=[]
    for i in range(len(a[1])):
        v_list1=[]
        for x in a:
            v_list1.append(x[i])
        v_list.append(v_list1)    
    
    u_list = []
    q = []

    for v in v_list:
        v = np.array(v)
        projekcje = 0
        for u_x in u_list:
            u_x = np.array(u_x)
            projekcje+=projekcja(u_x, v)
        u = v - projekcje
        u_list.append(u)
        if np.linalg.norm(u)==0:
            e=u
        else:
            e = (1/np.linalg.norm(u))*u
        q.append(e)    
        
    q = np.array(q).T
    r = np.dot(q.T,a)
    new_a = np.dot(q,r)
            
    print(q,r,new_a)

QR(a)    
