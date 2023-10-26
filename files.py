def read_file():    
    #other way to open file
    """ 
    name = "fichier.txt"
    variable = open(name)
    print(variable.read())  # no space between lines
    """    
    f_names = open("fichier.txt")
    for name in f_names:
        if "a" in name:
            name = name.strip()  #remove space
            print("Hello {}".format(name))


read_file()

#basics
"""
f = open("fichier.txt", "w") #write
f = open("fichier.txt", "r") #read
f = open("fichier.txt", "a") #append
f = open("fichier.txt", "r+") #read and write
print(f.name)   #name of file
print(f.mode)   #mode of file

"""

def read_file2():
    with open('fichier.txt', 'r') as f:
        #small file
        f_contents = f.read()

        #f_contents = f.readlines() #list of lines
        print(f_contents)

def writing_file():
    with open('fichier.txt', 'w') as f:
        f.write('Test')
        f.seek(0) #move cursor to 0
        f.write('Test')
        f.seek('R') #move cursor to R

def wrinting_starts():
    with open('test.txt', 'w') as f:
        val1 = 'test'
        val2 = 'waza'
        f.write(val1+' '+val2+'\n')
        f.seek(0)
        f.write('Surprise!')
        f.seek(6)
        f.write('z')

def copy_file():
    with open('test.txt', 'r') as rf:
        with open('test_copy.txt', 'w') as wf:
            for line in rf:
                wf.write(line)

def copy_img():
    with open('image.jpg', 'rb') as rf:
        with open('image_copy.jpg', 'wb') as wf:
            for line in rf:
                wf.write(line)
copy_img()