### ------------------ IMPORT LIBRARIES ----------------- ####
from tkinter import *
from functools import reduce
master = Tk()

##### ----------------- INSERTION FUNCTIONS ----------------- ####

# if the symbol is clicked, insert operator into the entry bar. 
def add():
    e.insert(END, "+")

def subtract():
    e.insert(END, "-")
    
def multiply():
    e.insert(END, "*")

def divide():
    e.insert(END, "/")
##### ------------------ OPERATIONAL FUNCTIONS ------------- #######
##### perform calculative operation based on desired function to be performed
##### on numbers. 
def addL():
    try:
        
        #store value of entry bar into a variable
        #this is to then split the string into a list, the delimiter being the operator
        
        string = e.get()
        l = string.split('+')


        #now we have a split up list of strings which are our numbers to be operated on
        #convert each string element to either a float or int, and store in variable "nums"
        nums = [float(i) if '.' in i else int(i) for i in l]
        answer = sum(nums)


        #convert answer back to string and insert in entry bar. 
        final = str(answer)
        e.delete(0, END)
        e.insert(END, "Sum:   " + final)
    except ValueError:
        e.delete(0, END)
        e.insert(END, "Invalid Input!")
def subL():
    try:
        string = e.get()
        l1 = string.split('-')

        nums = [float(i) if '.' in i else int(i) for i in l1]

        #find maximum number in list, then remove it from list and store in variable
        #use stored maximum number to subtract by every remaining integer in list
        maximum = max(nums)
        nums.remove(maximum)
        answer = [maximum - i for i in nums]

        
        final = str(answer)
        #empty entry bar before insertion of answer
        e.delete(0, END)
        e.insert(END, "Sum:   " + final)
    except ValueError:
        e.delete(0, END)
        e.insert(END, "Invalid Input!")
    
def multL():
    try:
        string = e.get()
        data = string.split("*")

        nums = [float(i) if '.' in i else int(i) for i in data]

        # use lambda to multiply each numer within our list "nums"
        answer = reduce(lambda x, y: x*y, nums)

        final = str(answer)
        e.delete(0, END)
        e.insert(END, "Sum:   " + final)
    except ValueError:
        e.delete(0, END)
        e.insert(END, "Invalid Input!")
def divL():
    ######### Add ZeroDivisionError Exception..... ##########
    try:
        string = e.get()
        list1 = string.split("/")
        
        nums = [float(i) if '.' in i else int(i) for i in list1]

        maximum = max(nums)
        nums.remove(maximum)
        #use stored maximum number to divide by every remaining integer in list

        answer = [maximum / i for i in nums]

        final = str(answer)
        e.delete(0, END)
        e.insert(END, "Sum:   " + final)
    except ZeroDivisionError:
        e.delete(0, END)
        e.insert(END, "Can't Divide By Zero!")
    except ValueError:
        e.delete(0, END)
        e.insert(END, "Invalid Input!")
###### DETERMINE WHICH FUNCTION TO EXECUTE BASED ON WHICH OPERATION IS INPUTTED
    
def enter():
    for i in e.get():
        if i == "+":
            addL()
        elif i == "*":
             multL()
        elif i == "/": 
             divL()
        elif i == "-":
             subL()
#### ----- INSERT NUMBERS INTO ENTRY BAR BASED ON WHICH BUTTON IS CLICKED ---- #     
def zero():
    e.insert(END, "0")
def one():
    e.insert(END, "1")
def two():
    e.insert(END, "2")
def three():
    e.insert(END, "3")
def four():
    e.insert(END, "4")
def five():
    e.insert(END, "5")
def six():
    e.insert(END, "6")
def seven():
    e.insert(END, "7")
def eight():
    e.insert(END, "8")
def nine():
    e.insert(END, "9")

###### ------------------ DESIGN AND GUI FEATURES --------------- #######
e = Entry(master)
e.grid(row=0, column=1)

b = Button(master, text="0", command=zero)
b.grid(row=3, column=0)

b1 = Button(master, text="1", command=one)
b1.grid(row=3, column=1)

b2 = Button(master, text="2", command=two)
b2.grid(row=3, column=2)

b3 = Button(master, text="3", command=three)
b3.grid(row=4, column=0)

b4 = Button(master, text="4", command=four)
b4.grid(row=4, column=1)

b5 = Button(master, text="5", command=five)
b5.grid(row=4, column=2)

b6 = Button(master, text="6", command=six)
b6.grid(row=5, column=0)

b7 = Button(master, text="7", command=seven)
b7.grid(row=5, column=1)

b8 = Button(master, text="8", command=eight)
b8.grid(row=5, column=2)

b9 = Button(master, text="9", command=nine)
b9.grid(row=6, column=1)

enterN = Button(master, text="ENTER", command=enter)
enterN.grid(row=8, column=0)

addN = Button(master, text="+", command=add)
subtract=Button(master, text="-", command=subtract)
mult = Button(master, text="X", command=multiply)
divideN = Button(master, text="/", command=divide)

addN.grid(row=7, column=4)
subtract.grid(row=7, column=2)
mult.grid(row=8, column=4)
divideN.grid(row=8, column=2)

master.geometry("230x200")
master.title("Calculator")
mainloop()
