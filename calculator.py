from tkinter import *

root = Tk()
root.title("Calculator")

# .... Input Field .....
e = Entry(root, width=42, borderwidth=5)
e.grid(
    row=0,column=0, columnspan=3, 
    padx=10, pady=10
)

# .... Functions .....
def button_click(num):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(num))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num 
    global math 
    math = 'add'
    f_num = int(first_number)
    e.delete(0, END)

def button_substract():
    first_number = e.get()
    global f_num 
    global math 
    math = 'substract'
    f_num = int(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num 
    global math 
    math = 'multiply'
    f_num = int(first_number)
    e.delete(0, END)

def button_division():
    first_number = e.get()
    global f_num 
    global math 
    math = 'division'
    f_num = int(first_number)
    e.delete(0, END)


def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == 'add':
        e.insert(0, f_num + int(second_number))
    elif math == 'substract':
        e.insert(0, f_num - int(second_number))
    elif math == 'multiply':
        e.insert(0, f_num * int(second_number))
    else:
        if int(second_number) == 0:
            e.insert(0, "Error: Divison by zero")
        else :
            e.insert(0, f_num / int(second_number))


# .... Buttons Config.....
btn_color = '#f7f6f3'
padding_x = 40
padding_y = 18

btn1 = Button(root, text='1', padx=padding_x, pady=padding_y, command= lambda : button_click(1), bg=btn_color)
btn2 = Button(root, text='2', padx=padding_x, pady=padding_y, command= lambda : button_click(2), bg=btn_color)
btn3 = Button(root, text='3', padx=padding_x, pady=padding_y, command= lambda : button_click(3), bg=btn_color)
btn4 = Button(root, text='4', padx=padding_x, pady=padding_y, command= lambda : button_click(4), bg=btn_color)
btn5 = Button(root, text='5', padx=padding_x, pady=padding_y, command= lambda : button_click(5), bg=btn_color)
btn6 = Button(root, text='6', padx=padding_x, pady=padding_y, command= lambda : button_click(6), bg=btn_color)
btn7 = Button(root, text='7', padx=padding_x, pady=padding_y, command= lambda : button_click(7), bg=btn_color)
btn8 = Button(root, text='8', padx=padding_x, pady=padding_y, command= lambda : button_click(8), bg=btn_color)
btn9 = Button(root, text='9', padx=padding_x, pady=padding_y, command= lambda : button_click(9), bg=btn_color)
btn0 = Button(root, text='0', padx=padding_x, pady=padding_y, command= lambda : button_click(0), bg=btn_color)

btn_add = Button(root, text='+', padx=38, pady=padding_y,command= button_add, bg=btn_color)
btn_substract = Button(root, text='-', padx=41,  pady=padding_y,command= button_substract, bg=btn_color)
btn_multiply = Button(root, text='*', padx=40, pady=padding_y,command= button_multiply, bg=btn_color)
btn_division = Button(root, text='/', padx=41,  pady=padding_y,command= button_division, bg=btn_color)
btn_equal = Button(root, text='=', padx=135, pady=padding_y,command= button_equal, border=4, bg=btn_color)
btn_clear = Button(root, text="Clear", padx=29 , pady=padding_y,command= button_clear, bg=btn_color)

# .... Buttons displaying on screen  .....

btn1.grid(row= 3, column= 0)
btn2.grid(row= 3, column= 1)
btn3.grid(row= 3, column= 2)

btn4.grid(row= 2, column= 0)
btn5.grid(row= 2, column= 1)
btn6.grid(row= 2, column= 2)

btn7.grid(row= 1, column= 0)
btn8.grid(row= 1, column= 1)
btn9.grid(row= 1, column= 2)

btn0.grid(row= 4, column= 0)

btn_add.grid(row=5, column=2)
btn_substract.grid(row=5, column=1)
btn_multiply.grid(row=5, column=0)
btn_division.grid(row=4, column=1)


btn_equal.grid(row=6, column=0, columnspan=3)
btn_clear.grid(row=4, column=2)

root.mainloop()