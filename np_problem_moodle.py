# numpy problems moodle
import numpy as np

def exS09_4():  
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
        y[i,1] = round(1/(m.sqrt(2*m.pi)*s)*m.exp(-0.5*((i-x0)/s)**2))
    print(y)

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