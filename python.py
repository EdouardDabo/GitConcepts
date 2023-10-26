import numpy as np

npoints = 21
values = np.linspace (-2.0, 2.0, npoints)
print(values)


npoints = 21
values = np.linspace (10, 30, npoints, dtype = int)
print(values)

vect = np.arange (0, 9, 3)
print(vect)

vect2 = np.arange(9)



# insert values in the vector
def methode1():
    nel = int(input("Enter the number of elements: "))
    lvec = []
    for i in range(nel):
        comp = int(input("Enter the value of the component {}: ".format(i)))
        lvec.append(float(comp))
    vec = np.array(lvec)    # create an array from a list
    print(vec)


def methode2():
    nel = int(input("Enter the number of elements: "))
    vec = np.zeros(nel)
    for i in range(nel):
        comp = int(input("Enter the value of the component {}: ".format(i)))
        vec[i] = float(comp)
    print(vec)

def list_or_vetor():
    lin = input("Enter the components of a vector in a line: ")
    smooth = lin.split()
    vec = np.float_(smooth)
    print("List: {}".format(smooth))    
    print("Vector: {}".format(vec)) # convert list to vector


def printmatrix():
    x = np.zeros((3, 4))    # 3x4 matrix of zeros 
    print(x)

def printmatrix2():
    x = np.ones((4,3))    
    for i in range(4):
        for j in range(3):
            x[i,j] = float(input("Enter the value of the component ({},{}): ".format(i,j)))

    print(x)

def operation_mat():
    mat1 = np.ones((2,2))    
    for i in range(2):
        for j in range(2):
            mat1[i,j] = float(input("Enter the value of the component ({},{}): ".format(i,j)))
    mat2 = np.ones((2,2)) 
    print("\n")   
    for i in range(2):
        for j in range(2):
            mat2[i,j] = float(input("Enter the value of the component ({},{}): ".format(i,j)))
    print("Matrix 1: \n{}".format(mat1))
    print("Matrix 2: \n{}".format(mat2))
    
    mat3 = mat1.dot(mat2)
    print("AB: \n{}".format(mat3))

    mat4 = np.linalg.inv(mat3)
    print("(AB)^-1: \n{}".format(mat4))

def operation_mat2():
    mat1 = np.ones((2,2))    
    for i in range(2):
        for j in range(2):
            mat1[i,j] = float(input("Enter the value of the component ({},{}): ".format(i,j)))
    mat2 = np.ones((2,2)) 
    print("\n")   
    for i in range(2):
        for j in range(2):
            mat2[i,j] = float(input("Enter the value of the component ({},{}): ".format(i,j)))
    mat3 = np.zeros((2,2))
    print("\n")   
    for i in range(2):
        for j in range(2):
            mat3[i,j] = float(input("Enter the value of the component ({},{}): ".format(i,j)))
    print("Matrix A: \n{}".format(mat1))
    print("Matrix B: \n{}".format(mat2))
    print("Matrix C: \n{}".format(mat3))

    # find matrix X such that AXB = C
    mat4 = np.linalg.inv(mat1)
    mat5 = np.linalg.inv(mat2)
    mat6 = mat4.dot(mat3)
    mat7 = mat6.dot(mat5)
    print("X: \n{}".format(mat7))

def exS09_4():  # numpy problems moodle
    vect = np.linspace(1.0, 5.0, 21)
    for i in range(21):     
        vect[i] = vect[i]*0.1
    # 2e methode: vect = vect*0.1
    print(vect)

def exS09_5():
    import math as m
    x0 = int(input("x0: "))
    s = float(input("s: "))
    init = float(input("initial value: "))
    final = float(input("final value: "))
    n = int(input("number of points: "))
    vect = np.linspace(init, final, n)
    y = np.zeros((n,2))
    for  i in range(n):
        y[i,0] = vect[i]
        y[i,1] = round(1/(m.sqrt(2*m.pi)*s)*m.exp(-0.5*((i-x0)/s)**2),5)
    print(y)
exS09_5()
def exS09_6():
    temp_mar = [13.8, 13.3, 13.9, 15.0, 16.4, 20.0, 21.9, 22.3, 22.0, 21.2, 18.8,16.0]
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October","November", "December"]
    temp = np.array(temp_mar)
    average = round(np.mean(temp),1)
    print("Average temperature: {}".format(average))
    
    min_temp = np.min(temp)
    index = np.where(temp == min_temp)
    print("The coldest month was {} and its temperature was {}".format(months[index[0][0]], min_temp))
    
    max_temp = np.max(temp)
    index = np.where(temp == max_temp)
    print("The hottest month was {} and its temperature was {}".format(months[index[0][0]], max_temp))    

def exS09_10(): # highest & lowest grades with coefs
    n = int(input("Enter the number of students: "))
    grades = np.zeros((n,4))
    for i in range(n):        
        grades[i,0] = i
        theory = float(input("Theory grade of student {}: ".format(i+1)))
        grades[i,1] = theory 
        problem = float(input("Problem grade of student {}: ".format(i+1)))
        grades[i,2] = problem
        grades[i,3] = grades[i,1]*0.4 + grades[i,2]*0.6
        
    print(grades)
    
    print("The highest grade is {}".format(np.max(grades[:,3])))
    print("The lowest grade is {}".format(round(np.min(grades[:,3]),2)))
    print("The average grade of the class is {}".format(round(np.mean(grades[:,3]),1)))
    index = np.where(grades[:,3] == np.max(grades[:,3]))
    print("The best student is {}".format(int(grades[index[0][0],0])+1))

def exS09_10_1(): # highest & lowest grades without coefs
    n = int(input("Enter the number of students: "))
    grades = np.zeros((n,4))
    lowest = 10
    highest = 0
    for i in range(n):        
        grades[i,0] = i
        theory = float(input("Theory grade of student {}: ".format(i+1)))
        if theory < lowest:
            lowest = theory
        grades[i,1] = theory 
        problem = float(input("Problem grade of student {}: ".format(i+1)))
        if problem > highest:
            highest = problem
        grades[i,2] = problem
        grades[i,3] = grades[i,1]*0.4 + grades[i,2]*0.6
        
    print(grades)
    
    print("The highest grade is {}".format(highest))
    print("The lowest grade is {}".format(lowest))
    print("The average grade of the class is {}".format(round(np.mean(grades[:,3]),1)))
    index = np.where(grades[:,3] == np.max(grades[:,3]))
    print("The best student is {}".format(int(grades[index[0][0],0])+1))
exS09_10_1()
