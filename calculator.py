from tkinter import *

root = Tk()
root.title("Simple Calculator")

e1 = Entry(root, width= 70)
e1.grid(row=0, column=0, columnspan=4, padx=10)

e = Entry(root, width=70, borderwidth=5)
e.grid(row=1, column=0, columnspan=4, padx=10, pady=10, ipady = 5)

def button_click(number):
    #e.delete(0, END) simple insert will insert the number in reverse
    current = e.get()
    e.delete(0, END)
    e.insert(0,str(current) + str(number))
    e1.delete(0,END)
    e1.insert(0, str(current) + str(number))
    return


def button_addition():
    global first_num
    global sign 
    global pos
    first_num = int(e.get())
    sign = str(1)
    k = str(e.get())
    size = len(k)
    e1.insert(size+1, '+')
    pos = size+1
    e.delete(0, END)


def button_subtraction():
    global first_num
    global sign 
    global pos
    first_num = int(e.get())
    sign = str(2)
    k = str(e.get())
    size = len(k)
    e1.insert(size+1, '-')
    pos = size+1
    e.delete(0, END)

def button_multiplication():
    global first_num
    global sign 
    global pos
    first_num = int(e.get())
    sign = str(3)
    k = str(e.get())
    size = len(k)
    e1.insert(size+1, '*')
    pos = size+1
    e.delete(0, END)

def button_division():
    global first_num
    global sign 
    global pos
    first_num = int(e.get())
    sign = str(4)
    k = str(e.get())
    size = len(k)
    e1.insert(size+1, '/')
    pos = size+1
    e.delete(0, END)



def button_equalsto(): 
    second_num = e.get()
    e.delete(0, END)
    e1.delete(0, END)
    if sign == "1":
         e.insert(0, int(first_num) + int(second_num))
         e1.insert(0, int(first_num) + int(second_num))
    elif sign == "2":
         e.insert(0, int(first_num) - int(second_num))
         e1.insert(0, int(first_num) - int(second_num))
    elif sign == "3":
         e.insert(0, int(first_num) * int(second_num))
         e1.insert(0, int(first_num) * int(second_num))
    elif sign == "4":
        e.insert(0, int(first_num) / int(second_num))
        e1.insert(0, int(first_num) / int(second_num))
    
    

def button_clear():
    e.delete(0, END)
    e1.delete(0, END)

button1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_mul = Button(root, text="*", padx=40, pady=20, command=button_multiplication)
button_div = Button(root, text="/", padx=40, pady=20, command=button_division)
button_add = Button(root, text="+", padx=40, pady=20, command=button_addition)
button_sub = Button(root, text="-", padx=40, pady=20, command=button_subtraction)
button_equals = Button(root, text="=", padx=40, pady=20, command=button_equalsto)
button_clear = Button(root, text="C", padx=40, pady=20, command= button_clear)


#Put the buttons on the screen

button1.grid(row=4, column=0)
button2.grid(row=4, column=1)
button3.grid(row=4, column=2)
button_mul.grid(row=4, column=3)

button4.grid(row=3, column=0)
button5.grid(row=3, column=1)
button6.grid(row=3, column=2)
button_div.grid(row=3, column = 3)

button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)
button_clear.grid(row=2, column=3)

button0.grid(row=5, column=1)
button_add.grid(row=5, column=0)
button_sub.grid(row=5, column=2)
button_equals.grid(row=5, column=3)



root.mainloop() 