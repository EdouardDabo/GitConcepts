import matplotlib.pyplot as plt
import numpy as np
#%matplotlib inline

def draw_graph(x,y):
    x = np.linspace(-2,2,101)
    y = x**2
    print(x)

    plt.plot(x,y) #vector x,y
    plt.title('Graph of x^2 vs x')
    plt.show()

#draw_graph()

def draw_graph2():
    x = np.linspace(0,3*np.pi,500)
    plt.plot(x,np.sin(x**2))
    plt.title('A simple chirp')
    plt.show()

#draw_graph2()

def draw_graph3():
    x = np.linspace(-2,2,101)
    y = x**2
    plt.xlabel('x')    #name x axe
    plt.ylabel('f(x)') #name y axe
    plt.plot(y)
    plt.title('Graph 3') #name graph
    plt.show()
#draw_graph3()

def draw_graph_v2():
    x = np.linspace(-2,2,101)
    y = x**2
    print(x)

    plt.xlabel('x')    #name x axe
    plt.ylabel('f(x)') #name y axe
    plt.xlim(-1.5, 1.5) #limit x axe
    plt.ylim(-0.5, 2.5) #limit y axe
    plt.plot(x,y,'g', label = "x**2") #vector x, y,     green line (g: green)
    plt.title('Graph')
    y2 = x**4
    plt.plot(x,y2, 'ro',label = "x**4") #Red dot (r: red, o: large dot)
    y4 = x**3
    plt.plot(x,y4, 'b.',label = "x**3") #Blue dot (b: blue, .: small dot)
    plt.legend() #show label
    plt.savefig('graph.png') #save graph on computer    (png, pdf, ps, eps, svg, jpeg, jpg,...)   
    plt.show()

#draw_graph_v2()

def trigonometric_function():
    n = int(input('enter the number of points to draw: '))
    x = np.linspace(-1,1,n)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Body function (2pix)')
    y = np.cos(2*np.pi*x)
    plt.plot(x,y)
    plt.savefig('cos2pix.png')
    plt.show()

#trigonometric_function()
    
def two_trigo_func():
    n = int(input('enter the number of points to draw: '))
    x = np.linspace(-1,1,n)    
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Functions cos(2pix) and sin(2pix)')
    y = np.cos(2*np.pi*x)
    plt.plot(x,y, label = 'cos(2pix)')

    y2 = np.sin(2*np.pi*x)
    plt.plot(x,y2, label = 'sin(2pix)')

    plt.legend()
    plt.savefig('trigonometric.png')
    plt.show()
#two_trigo_func() 

def S10_3():
    try:
        n = int(input('enter the number of points to draw: '))
    except ValueError:
        print('Error: you must enter an integer')
        S10_3()
        return
    else:
        x = np.linspace(0,4,n)
        plt.xlabel('x')
        plt.ylabel('f(x)')
        y = np.sin(np.pi*x)*np.sin(20*np.pi*x)*np.exp(-x)
        plt.plot(x,y)
        plt.show()
S10_3()

def S10_4():
    try:
        n = int(input('enter the number of points to draw: '))
        t = int(input('enter the temperature: '))
    except ValueError:
        print('Error: you must enter an integer')
        S10_4()
        return
    else:
        x= np.linspace(2,10,n)
        plt.xlabel('Pressure(atm)')
        plt.ylabel('Molar volume(L/mol)')
        plt.title('Isotherm (ideal gas)')
        y = 0.08206*t/x
        plt.plot(x,y)
        plt.show()
        plt.savefig('isotherm.jpg')

#S10_4()

def S10_exPLots():#doesn t work
    try:
        n = int(input('enter the number of points to draw: '))
        nt = int(input('how many temperatures do you want to draw: '))
        for i in range(nt):
            t = int(input('enter the temperature : '))
            t_lst = []
            t_lst.append(t)
    except ValueError:
        print('Error: you must enter an integer')
        S10_exPLots()
        return
    else:
        for e in t_lst:
            print(t_lst[e])
        x = np.linspace(2,10,n)
        for i in t_lst:
            y =  0.08206*t/x
            plt.plot(x,y)
        plt.show    

#S10_exPLots()

def S10_6():
    n = int(input('enter the number of points to draw: '))
    start = int(input('enter the start value: '))
    end = int(input('enter the end value: '))
    x0 = int(input('enter the value of x0: '))
    s = float(input('enter the value of s: '))
    x = np.linspace(start,end,n)
    y = 1/np.sqrt(2*np.pi)*np.exp((-1/2)*(x-x0)**2/s**2)
    plt.title('Gaussian function')
    plt.xlabel('x')
    plt.ylabel('f(x)')    
    plt.plot(x,y)
    plt.show()
#S10_6()

def S10_7():
    n = int(input('enter the number of points to draw: '))
    x = np.linspace(0,3,n)
    y1 = np.exp(-x)
    y2 = np.sin(3*np.pi*x)*np.exp(-x)
    plt.title('Functions')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.plot(x,y1, label = 'exp(-x)')
    plt.plot(x,y2, label = 'sin(3pix)*exp(-x)')
    plt.legend()
    plt.show()
#S10_7()

def S10_10():
    n = int(input('enter the number of points to draw: '))
    nf = int(input('enter the number of functions to draw: '))
    start = int(input('enter the start value: '))
    end = int(input('enter the end value: '))
    
    for i in range(nf):
        x0 = int(input('enter the value of x0: '))
        s = float(input('enter the value of s: '))
        x = np.linspace(start,end,n)
        y = 1/np.sqrt(2*np.pi)*np.exp((-1/2)*(x-x0)**2/s**2)
        plt.plot(x,y, label = 'x0 = '+str(x0)+', s = '+str(s))
    plt.legend()
    plt.title('Gaussian function')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.show()
    
#S10_10()

