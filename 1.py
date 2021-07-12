from tkinter import *
from PIL import ImageTk, Image

root=Tk()

root.title("Simple Calculator")
root.iconbitmap('C:/Users/Prafulmhrjn/OneDrive/Desktop/headphone.ico')

my_image=ImageTk.PhotoImage(Image.open("C:/Users/Prafulmhrjn/OneDrive/Desktop/lens.png"))
my_label=Label(image=my_image)
my_label.pack()


button_quit=Button(root,text="Exit",command=root.quit,width=20)
button_quit.pack()
root.mainloop()