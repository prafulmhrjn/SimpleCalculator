from tkinter import *

root = Tk()

#Giving the title of the project
root.title("Simple Calculator")

e=Entry(root, width=50, borderwidth=10)
e.grid(row=0,column=0,columnspan=6,padx=10,pady=10)

#click function
def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0,END)

def button_equals():
    second_number=e.get()
    e.delete(0,END)

    if math == "addition":
        e.insert(0,f_number+int(second_number))

    if math == "subtraction":
        e.insert(0,f_number-int(second_number))

    if math == "multiplication":
        e.insert(0,f_number*int(second_number))

    if math == "division":
        e.insert(0,f_number/int(second_number))

    if math == "percent":
        e.insert(0,f_number/100)





def button_add():
    first_number=e.get()
    global f_number
    global math
    math="addition"
    f_number=int(first_number)
    e.delete(0,END)




def button_subtract():
    first_number = e.get()
    global f_number
    global math
    math = "subtraction"
    f_number = int(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_number
    global math
    math = "multiplication"
    f_number = int(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_number
    global math
    math = "division"
    f_number = int(first_number)
    e.delete(0, END)

def button_percentage():
    first_number = e.get()
    global f_number
    global math
    math = "percent"
    f_number = int(first_number)
    e.delete(0,END)




button_1=Button(root, text="1",padx=40,pady=20,command=lambda:button_click(1))
button_2=Button(root, text="2",padx=40,pady=20,command=lambda:button_click(2))
button_3=Button(root, text="3",padx=40,pady=20,command=lambda:button_click(3))
button_4=Button(root, text="4",padx=40,pady=20,command=lambda:button_click(4))
button_5=Button(root, text="5",padx=40,pady=20,command=lambda:button_click(5))
button_6=Button(root, text="6",padx=40,pady=20,command=lambda:button_click(6))
button_7=Button(root, text="7",padx=40,pady=20,command=lambda:button_click(7))
button_8=Button(root, text="8",padx=40,pady=20,command=lambda:button_click(8))
button_9=Button(root, text="9",padx=40,pady=20,command=lambda:button_click(9))
button_0=Button(root, text="0",padx=40,pady=20,command=lambda:button_click(0))
button_percentage=Button(root, text="%",padx=40,pady=20,command=button_percentage)
button_equals=Button(root, text="=",padx=90,pady=20,command=button_equals)
button_clear=Button(root, text="AC",padx=85,pady=20,command=button_clear)
button_add=Button(root, text="+",padx=40,pady=20,command=button_add)
button_subtract=Button(root, text="-",padx=40,pady=20,command=button_subtract)
button_multiply=Button(root, text="x",padx=40,pady=20,command=button_multiply)
button_divide=Button(root, text="/",padx=40,pady=20,command=button_divide)



#Button placement on screen
button_1.grid(row=4,column=1)
button_2.grid(row=4,column=2)
button_3.grid(row=4,column=3)
button_4.grid(row=3,column=1)
button_5.grid(row=3,column=2)
button_6.grid(row=3,column=3)
button_7.grid(row=2,column=1)
button_8.grid(row=2,column=2)
button_9.grid(row=2,column=3)
button_0.grid(row=5,column=1)
button_percentage.grid(row=6,column=1)
button_equals.grid(row=6,column=2,columnspan=2)
button_clear.grid(row=5,column=2,columnspan=2)
button_add.grid(row=2,column=4)
button_subtract.grid(row=3,column=4)
button_multiply.grid(row=4,column=4)
button_divide.grid(row=5,column=4)








root.mainloop()