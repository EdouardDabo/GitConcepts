import numpy as np
import matplotlib.pyplot as plt

def ex1():    
    x = np.arange(21)
    x[(x>=9) & (x<=15)] *= -1
    print(x)

def ex2():
    x = np.linspace(15, 55)
    print(x[1:-1])

def ex3():
    x = np.zeros((3,4))
    x[0,:] = 1
    x[-1,:] = 1
    x[:,0] = 1
    x[:,-1] = 1
    print(x)

def ex4():
    x = np.linspace(5,50,10)
    print(x)

def ex5():
    x = np.random.randint(0,10,5)
    print(x)

def ex6():    
    x = np.array([1,2,3,4])
    y = np.array([5,6,7,8])
    print(x*y)

def ex7():
    x = np.arange(10,22).reshape(3,4)
    print(x)

def ex8():
    x = np.arange(10,22).reshape(3,4)
    print(x.shape)
    
def ex9():
    x = np.zeros((4,4))
    x[::2,1::2] = 1
    x[1::2,::2] = 1
    print(x)

def ex10():
    list1 = [1, 3, 5, 7, 9]
    list2 = [2, 3, 4, 6, 8, 9]
    list3 = []
    for i in list1:
        for j in list2:
            if i==j:
                list3.append(i)

    print(list3)

def ex11():
    x = np.array([1,1,2,2,3,3,4,4,5,5])
    print(np.unique(x))

def ex12():
    x = np.array([1,2,3])
    y = np.array([4,5,6])
    print(np.cross(x,y))

def ex13():
    x = [ 0.89225122, 0.68774813, 0.20392039, 1.22093243, 1.24435921, 1.00358852, 0.37378547, 0.8534585, 0.31999648, 0.567451 ]
    # convert cartesian coodinates to polar coordinates
    r = np.sqrt(x[0]**2 + x[1]**2 + x[2]**2)
    theta = np.arccos(x[2]/r)
    phi = np.arctan(x[1]/x[0])
    print(r, theta, phi)
    



ex13()