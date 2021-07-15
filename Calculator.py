from tkinter import *

root = Tk()
root.geometry("354x460")
root.title("CALCULATOR")
mylabel = Label(root, text="CALCULATOR", bg='light green', font=("Arial", 20, 'bold'))
mylabel.pack(side=TOP)
root.config(background='light green')

textin = StringVar()
operator = ""


def clickbut(number):
    global operator
    operator = operator + str(number)
    textin.set(operator)


def equalbut():
    global operator
    add = str(eval(operator))
    textin.set(add)
    operator = ''


def equalbut():
    global operator
    sub = str(eval(operator))
    textin.set(sub)
    operator = ''


def equalbut():
    global operator
    mul = str(eval(operator))
    textin.set(mul)
    operator = ''


def equalbut():
    global operator
    div = str(eval(operator))
    textin.set(div)
    operator = ''


def clearbut():
    textin.set('')


mytext = Entry(root, font=("Courier New", 12, 'bold'), textvar=textin, width=25, bd=5, bg='powder blue')
mytext.pack()

but1 = Button(root, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(1), text="1",
              font=("Courier New", 16, 'bold'))
but1.place(x=10, y=100)

but2 = Button(root, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(2), text="2",
              font=("Courier New", 16, 'bold'))
but2.place(x=10, y=170)

but3 = Button(root, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(3), text="3",
              font=("Courier New", 16, 'bold'))
but3.place(x=10, y=240)

but4 = Button(root, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(4), text="4",
              font=("Courier New", 16, 'bold'))
but4.place(x=75, y=100)

but5 = Button(root, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(5), text="5",
              font=("Courier New", 16, 'bold'))
but5.place(x=75, y=170)

but6 = Button(root, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(6), text="6",
              font=("Courier New", 16, 'bold'))
but6.place(x=75, y=240)

but7 = Button(root, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(7), text="7",
              font=("Courier New", 16, 'bold'))
but7.place(x=140, y=100)

but8 = Button(root, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(8), text="8",
              font=("Courier New", 16, 'bold'))
but8.place(x=140, y=170)

but9 = Button(root, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(9), text="9",
              font=("Courier New", 16, 'bold'))
but9.place(x=140, y=240)

but0 = Button(root, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(0), text="0",
              font=("Courier New", 16, 'bold'))
but0.place(x=10, y=310)

butdot = Button(root, padx=47, pady=14, bd=4, bg='white', command=lambda: clickbut("."), text=".",
                font=("Courier New", 16, 'bold'))
butdot.place(x=75, y=310)

butpl = Button(root, padx=14, pady=14, bd=4, bg='white', text="+", command=lambda: clickbut("+"),
               font=("Courier New", 16, 'bold'))
butpl.place(x=205, y=100)

butsub = Button(root, padx=14, pady=14, bd=4, bg='white', text="-", command=lambda: clickbut("-"),
                font=("Courier New", 16, 'bold'))
butsub.place(x=205, y=170)

butml = Button(root, padx=14, pady=14, bd=4, bg='white', text="*", command=lambda: clickbut("*"),
               font=("Courier New", 16, 'bold'))
butml.place(x=205, y=240)

butdiv = Button(root, padx=14, pady=14, bd=4, bg='white', text="/", command=lambda: clickbut("/"),
                font=("Courier New", 16, 'bold'))
butdiv.place(x=205, y=310)

butclear = Button(root, padx=14, pady=119, bd=4, bg='white', text="AC", command=clearbut, font=("Courier New", 16, 'bold'))
butclear.place(x=270, y=100)

butequal = Button(root, padx=151, pady=14, bd=4, bg='white', command=equalbut, text="=", font=("Courier New", 16, 'bold'))
butequal.place(x=10, y=380)
root.mainloop()