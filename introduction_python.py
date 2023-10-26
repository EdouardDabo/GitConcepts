
def print_name():
    fn = "edouard"
    ln = "dabo"
    print("prenom {} et nom {}".format(fn, ln))
    
def convert_float():
    a=3
    b= float(a)
    print (b)   # b = 3 // b = 3.0

def input_name():
    name = input("enter ur name ")
    print("hello ", name)    

def input_number():
    n = input("enter a number ")
    n = float(n)
    n = float(input("enter a number "))

def use_pi():
    import math
    n = math.pi

def operations():    
    num1 = float(input("enter a number "))
    num2 = float(input("enter a number "))
    sum = num1 + num2
    product = num1 * num2
    print("The sum of {} and {} is {}".format(num1, num2, sum))
    print("The product of {} and {} is {}".format(num1, num2, product))

def convert_temp():    
    temp = float(input("enter a temperature in celsius "))
    new_temp = float(temp + 273.15)
    print("The temperature in kelvin is {}".format(new_temp))

def calculate_area():
    length = float(input("enter a length"))
    edges = float(input("enter a number of edges"))
    area = float((edges * length**2)/(4 * math.tan(math.pi/edges)))
    volume = float() 

def replace_message():
    message = "good morning"
    message = message.replace("morning", "evening")
    print(message)     
     
# Conversion Celsus -> Fahrenheit  
def convert_celsus_fahrenheit(): 
    temp = input()
    degree = int(temp[:-1])
    i_convertion = temp[-1]

    if i_convertion.upper() == "C":
        result = int(round((9 * degree) / 5 + 32))
        o_convertion = "Fahrenheit"
    elif i_convertion.upper() == "F":
        result = int(round((degree - 32) * 5 / 9))
        o_convertion = "Celsius"
    else:
        print("Input proper convention.")
        quit()
    print("The temperature in", o_convertion, "is", result, "degrees.")

def divisble():
    num1 = int(input("enter a number "))
    num2 = int(input("enter a number "))

    res = num1%num2
    if res == 0:
        print("divisible : quotient = ", num1/num2)
    else:
        print("not divisible ", num1/num2, "reste = ", res) # not sure

def compare():
    num1 = int(input("enter a number "))
    num2 = int(input("enter a number "))

    if num1 > num2:
        print("{num1} is greater than {num2}").format(num1, num2)
    elif num1 < num2:
        print("{num2} is greater than {num1}").format(num2, num1)
    else:
        print("{num1} is equal to {num2}").format(num1, num2)

"""     DOESN T WORK
num = int(input("enter your unit number "))

if num < 100:
    print("no charge")
elif num>100 and num< 200: 
    supp = num - 100
    print("charge = ", supp*0.05)
elif num>200: 
    supp = num - 200
    print("charge = ", supp*0.10)

"""

def int_division_by_3():
    num = int(input("enter an integer value: "))

    while num>0:
        res = num//3
        print("the integer division of {} by 3 is {}".format(num, res))
        num = int(input("enter an integer value: "))
    
    print("we're done") 

def sum_numbers_divided_by_3():
    num = 0
    tot=0
    while num!= 211:
        res = num%3
        if res ==0:
            tot +=1
        num+=1

    print ("numbers / by 3 between 0 to 211 is equal to : ", tot)   

def factorial():
    num = int(input("enter a number"))
    fact = 1
    while num >1:
        fact = fact*num
        num-=1
    
    print("factorial = ", fact)

def use_break_continue():
    name = "Jesaa29roy"

    size = len(name)
    i=-1
    while i < size-1:
        i+=1
        if not name[i].isalpha():
            continue
#         utilisation du break 
#       if name[i].isdecimal():
#           break
   
        print(name[i], end="")
    

def is_prime():
    num = int(input("enter a number"))
    i=2
    while i<num:
        if num%i == 0:
            print("not prime")
            break
        i+=1
    else:
        print("prime")


def fibonacci():
    num = int(input("enter a number"))
    i=1
    j=1
    while i<num:
        print(i)
        i, j = j, i+j 

 
def reverse_list():
    liste = [1,2,3,4,5,6,7,8,9,10]
    liste = liste[::-1] 
    liste.reverse()
    print(liste)
    
def liste():
    lst = [1,2,3,4,5,6,7]
    print(lst[2])
    lst.append(8)
    print(lst)
    lst.remove(lst[0])
    print(lst)
    

def sum_liste():
    n = int(input("enter a number"))
    lst = []
    for i in range(1,n+1):
        lst.append(1/i)
    sn = sum(lst)
    print("For n = {}, the sum is {:.2f}".format(n, sn)) # :.2f -> affiche 2 chiffres apres la virgule



def zumba():
    a = [1,3,5,7,11]
    b = [13,17]
    c = a + b
    print(c)
    b[0] = -1
    d = []
    for e in a:
        d.append(e+1)
    print(d)
    d.append(b[0]+1)
    d.append(b[-1]+1)
    print(d)
    print(d[-2:])
    print(d[:-1])
    print(d[1:4])
    
def generate_list():
    n = int(input("enter a number"))
    lst = []
    for i in range(1,n+1):
        lst.append(i*i)
    print(lst)
    

# saisie du nom et de la note des eleves et afficher le nom avec la note associée
def students():
    n = int(input("enter a number of students"))
    dico = {}
    for i in range(n):
        name = input("enter a name: ")
        note = float(input("enter a note: "))
        dico[name] = note
    
    for key, value in dico.items():
        print(" {}\t {}".format(key, value))
        

def mean_list():
    n = input("enter a number")
    lst = []
    while n!= "":
        lst.append(n)
        n = input("enter a number")
    sum = 0
    for i in lst:
        sum += int(i)        
    print("The mean is ", sum/len(lst))
     

def writenames():
    n = input("enter names ")
    lst = []
    x = n.split(" ")
    for i in x:                             
        lst.append(i)
    
    for e in lst:
        print("Hello {}".format(e))


def calculate_molecular_mass():
    element = ["H", "C", "N", "O", "S", "CL"]
    mass = [1.008, 12.011, 14.007, 15.999, 32.065, 35.453]
    sum=0
    for i in element:
        n = int(input("enter the number of {} atoms: ".format(i)))
        sum += n*mass[element.index(i)]
        
    print("\nThe molecular mass is ", sum)


def sum_polynomial():
    n = int(input("enter the degree max "))
    
    x = float(input("enter the value of x "))
    sum = 0
    lst = ""
    for i in range(n+1):
        a = int(input("enter the coeficient no{}: ".format(i)))
        sum += a*(x**i)        
        lst = lst + str(a) + "x^" + str(i) + " + "
        a+=1
    print(lst)
    print("the sum is ", sum)

def dico():
    contry_capitals = {"United States":"Washington DC", "Italy":"Rome", "England":"London"}
    print(contry_capitals)

def dico_in_dico():
    dict = {1:"geek", 2:"for",
            3:{'A':"Welcome", 'B':"To", 'C':"Geeks"}}
    print(dict[3]['A'])

def dico2():
    cities = ("Paris", "Athens", "Madrid")
    continent = "europe"
    my_dico = dict.fromkeys(cities, continent)
    print(my_dico)
    
    key = ['ten', 'twenty', 'thirty']
    value = [10, 20, 30]
    
    my_dico = dict(zip(key, value))
    print(my_dico)


def projet1():
    
    dicoH = {"element" : "Hydrogene", "atomic number": 1, "melting pt":14, "boiling pt":20}
    dicoHe = {"element" : "Helium", "atomic number": 2, "melting pt":1, "boiling pt":4}
    dicoLi = {"element" : "Lithium", "atomic number": 3, "melting pt":453, "boiling pt":1603}
    dicoBe = {"element" : "Beryllium", "atomic number": 4, "melting pt":1560, "boiling pt":2742}
    dicoB = {"element" : "Boron", "atomic number": 5, "melting pt":2349, "boiling pt":4200}
    dicoC = {"element" : "Carbone", "atomic number": 6, "melting pt":3915, "boiling pt":3915}
    dicoN = {"element" : "Nitrogen", "atomic number": 7, "melting pt":63, "boiling pt":77}
    dicoO = {"element" : "Oxygen", "atomic number": 8, "melting pt":54, "boiling pt":90}
    dicoF = {"element" : "Fluorine", "atomic number": 9, "melting pt":53, "boiling pt":85}
    dicoNe = {"element" : "Neon", "atomic number": 10, "melting pt":25, "boiling pt":27}

    dico = {"H":dicoH, "He":dicoHe, "Li":dicoLi, "Be":dicoBe, "B":dicoB, "C":dicoC, "N":dicoN, "O":dicoO, "F":dicoF, "Ne":dicoNe}
    
    elem = input("enter an element: ").upper()
    temp = int(input("enter a temperature: "))
    
    
    if temp < dico[elem]["melting pt"]:
        print("At {}K the element {} is solid".format(temp,elem))
    elif temp > dico[elem]["boiling pt"]:
        print("At {}K the element {} is gas".format(temp,elem))
    else:
        print("At {}K the element {} is liquid".format(temp,elem))                



def projet2():
    
    dicoANZ = {"y1_2" : 2.3, "y3" : 4.1}
    dicoBoA = {"y1_2" : 0.1, "y3" : 5}
    dicoCB = {"y1_2" : 3.5, "y3" : 3.8}
    dicoW = {"y1_2" : 3.7, "y3" : 3.7}
    
    dicoBank = {"ANZ":dicoANZ, "Bank of Australia":dicoBoA, "Commonwealth Bank":dicoCB, "Westpac":dicoW}
    
    bank = input("enter a bank: ").lower()
    time_of_mortgage = int(input("enter the time of mortgage: "))


def biggest_nbr():
    def aha(num1, num2):
        if num1 > num2:
            return num1
        else:
            return num2
    
    print("the biggest number is ",aha(int(input("enter a number: ")), int(input("enter a number: "))))


def biggest_smallest(): 
    lst = []
    x=0
    while x<5:
        n = input("enter a number: ")
    
        lst.append(n)
        x+=1

    lst.sort()
    print("the biggest number is {} and the smallest is {}".format(lst[-1], lst[0]))

    

"""     HOW TO USE try except else finally
try:
    #some code
except:
    #some code 
    #handle the exeption
    #possibilité d avoir plusieurs 'except'
else:
    #some code (if try is executed)
finally:
    #some code (always executed)
    
"""  

def try_except():
    try:
        x = int(input("enter a number: "))
    except:
        print("the number is negative")
        x = int(input("enter a number: "))
    else:
        print("the number is positive")
    finally:
        if(x%2==0):
            print("the number is even")
        else:
            print("the number is odd")

try_except()
          
    


 
   
        


    

