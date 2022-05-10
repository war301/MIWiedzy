import numpy as np 
import math
import random as rd 

def monte_carlo(function, a, b, ile_punktow):
    maxValue = max(map(lambda i : function(i), np.linspace(a, b, ile_punktow, True)))
    points = [(rd.uniform(a,b), rd.uniform(0, maxValue)) for x in range(ile_punktow)] #uniform zwraca losową pomiędzy 
    print(maxValue)
    print(rd.uniform(a,b))
    print(points)
    lower = upper = 0
    for x in points:
        if x[1] < function(x[0]):
            lower += 1
        else:
            upper += 1
 
    return maxValue*(b-a)*(lower/(lower+upper))

def riemann(function, a, b, precision):
    points = tuple(map(lambda i: function(i), np.linspace(a, b, precision, True)))
    diff = (b-a)/(precision-1)
 
    area = 0
    for x in points[1:]:
        area += diff*x
 
    return area
 
def trapmann(function, a, b, precision):
    points = tuple(map(lambda i: function(i), np.linspace(a, b, precision, True)))
    diff = (b-a)/(precision-1)
 
    area = 0
    for x in range(1, precision):
        area += diff*(points[x]+points[x-1])/2
 
    return area

#print(monte_carlo(math.sin, 0, math.pi, 100))
#print(riemann(math.sin, 0, math.pi, 100))
#print(trapmann(math.sin, 0, math.pi, 100))
