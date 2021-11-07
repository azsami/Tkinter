from tkinter import *

root = Tk()
root.title("Simple Calculator for adding")

e = Entry(root,width=35,borderwidth = 5)
e.grid(row=0,column=0, columnspan=3, padx=5, pady=5)

#e.insert(0,"Enter Your Email: ")
def button_click(number):

    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current)+str(number))

def buttonclear():
    e.delete(0,END)



def buttonequal():

    second_number = e.get()
    e.delete(0,END)
    if math == "addition":
        e.insert(0, f_num + float(second_number))
    if math == "substract":
        e.insert(0, f_num - float(second_number))
    if math == "divide":
        e.insert(0, f_num / float(second_number))
    if math == "multiply":
        e.insert(0, f_num * float(second_number))


def buttonadd():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    e.delete(0, END)

def buttonmultiply():

    first_number = e.get()
    global f_num
    global math
    math = "multiply"
    f_num = float(first_number)
    e.delete(0, END)

def buttonsubstract():
    first_number = e.get()
    global f_num
    global math
    math = "substract"
    f_num = float(first_number)
    e.delete(0, END)

def buttondivide():
    first_number = e.get()
    global f_num
    global math
    math = "divide"
    f_num = float(first_number)
    e.delete(0, END)

#defining button

button1= Button(root, text="1", padx= 40, pady=25, command=lambda:button_click(1))
button2= Button(root, text="2", padx= 40, pady=25, command=lambda:button_click(2))
button3= Button(root, text="3", padx= 40, pady=25, command=lambda:button_click(3))
button4= Button(root, text="4", padx= 40, pady=25, command=lambda:button_click(4))
button5= Button(root, text="5", padx= 40, pady=25, command=lambda:button_click(5))
button6= Button(root, text="6", padx= 40, pady=25, command=lambda:button_click(6))
button7= Button(root, text="7", padx= 40, pady=25, command=lambda:button_click(7))
button8= Button(root, text="8", padx= 40, pady=25, command=lambda:button_click(8))
button9= Button(root, text="9", padx= 40, pady=25, command=lambda:button_click(9))
button0= Button(root, text="0", padx= 40, pady=25, command=lambda:button_click(0))
button_add= Button(root, text="+", padx= 40, pady= 25, command=lambda:buttonadd())
button_equal= Button(root, text="=", padx= 40, pady= 25, command=lambda:buttonequal())
button_clear= Button(root, text="CLEAR", padx= 120, pady= 25, command=lambda:buttonclear())
button_substract= Button(root, text="-", padx= 40, pady= 25, command=lambda:buttonsubstract())
button_multiply= Button(root, text="*", padx= 40, pady= 25, command=lambda:buttonmultiply())
button_divide= Button(root, text="/", padx= 40, pady= 25, command=lambda:buttondivide())
#put the button on the screen:


button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0)
button_add.grid(row=4,column=1)
button_clear.grid(row=6,column=0,columnspan=3)
button_equal.grid(row=4, column=2)
button_multiply.grid(row=5,column=0)
button_divide.grid(row=5,column=1)
button_substract.grid(row=5,column=2)



root.mainloop()
