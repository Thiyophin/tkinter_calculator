# Code to make simple calculator using python3(GUI)

from tkinter import *

screen_width = 380
screen_height = 410

window = Tk()
window.geometry("{}x{}".format(screen_width, screen_height))
window.title("Simple Calculator")
window.resizable(0, 0)

screen = Entry(window, width=50, borderwidth=5, justify="right")
screen.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


def button_click(number):
    present = screen.get()
    screen.delete(0, END)
    screen.insert(0, present + number)
    return


def button_clear():
    screen.delete(0, END)
    return


def button_delete():
    present = screen.get()
    length = len(present)-1
    screen.delete(length, END)


def button_equal():
    ans = screen.get()
    ans = eval(ans)
    screen.delete(0, END)
    screen.insert(0, ans)


button7 = Button(window, text="7", padx=40, pady=20, command=lambda: button_click('7'))
button8 = Button(window, text="8", padx=40, pady=20, command=lambda: button_click('8'))
button9 = Button(window, text="9", padx=40, pady=20, command=lambda: button_click('9'))
button4 = Button(window, text="4", padx=40, pady=20, command=lambda: button_click('4'))
button5 = Button(window, text="5", padx=40, pady=20, command=lambda: button_click('5'))
button6 = Button(window, text="6", padx=40, pady=20, command=lambda: button_click('6'))
button1 = Button(window, text="1", padx=40, pady=20, command=lambda: button_click('1'))
button2 = Button(window, text="2", padx=40, pady=20, command=lambda: button_click('2'))
button3 = Button(window, text="3", padx=40, pady=20, command=lambda: button_click('3'))
button0 = Button(window, text="0", padx=40, pady=20, command=lambda: button_click('0'))
button_dot = Button(window, text=".", padx=40, pady=20)
button_div = Button(window, text="/", bg="#ADAFC0", padx=40, pady=20, command=lambda: button_click("/"))
button_mul = Button(window, text="x", bg="#ADAFC0", padx=40, pady=20, command=lambda: button_click("*"))
button_min = Button(window, text="-", bg="#ADAFC0", padx=40, pady=20, command=lambda: button_click("-"))
button_add = Button(window, text="+", bg="#ADAFC0", padx=40, pady=20, command=lambda: button_click("+"))
button_equal = Button(window, text="=", padx=40, pady=20, command=button_equal)
button_delete = Button(window, text="DELETE", bg="#ADAFC0", padx=170, pady=15, command=button_delete)
button_clear = Button(window, text="CLEAR", bg="#ADAFC0", padx=170, pady=15, command=button_clear)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button0.grid(row=4, column=0)
button_dot.grid(row=4, column=1)
button_equal.grid(row=4, column=2)
button_div.grid(row=1, column=3)
button_mul.grid(row=2, column=3)
button_min.grid(row=3, column=3)
button_add.grid(row=4, column=3)
button_delete.grid(row=5, column=0, columnspan=4)
button_clear.grid(row=6, column=0, columnspan=4)
window.mainloop()
