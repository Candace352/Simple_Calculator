import tkinter as tk
from tkinter import StringVar,Menu
from ttkthemes import ThemedStyle


calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    results.delete(1.0, "end")
    results.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        solution = str(eval(calculation))
        results.delete(1.0, "end")
        results.insert(1.0, solution)
    except:
        clear_field()
        results.insert(1.0, "ERROR!")



def clear_field():
    global calculation
    calculation = ""
    results.delete(1.0, "end")

def set_dark_theme():
    style.set_theme("black")
    root.configure(bg=style.lookup('TFrame','background'))
    button_list = [btn_1, btn_2, btn_3, btn_4, btn_5, btn_6, btn_7, btn_8, btn_9, btn_0, btn_clear, btn_closebracket, btn_openbracket, btn_addition, btn_subtract, btn_stop, btn_multiply, btn_division, btn_percent, btn_equals]
    for button in button_list:
        button.configure(bg=style.lookup('TButton','background'), fg=style.lookup('TButton','foreground'))
    root.update_idletasks()


def set_light_theme():
    style.set_theme("breeze")
    root.configure(bg=style.lookup('TFrame','background'))
    button_list = [btn_1,btn_2,btn_3,btn_4,btn_5,btn_6,btn_7,btn_8,btn_9,btn_0,btn_clear,btn_closebracket,btn_openbracket,btn_addition,btn_subtract,btn_stop,btn_multiply,btn_division,btn_percent,btn_equals]
    for button in button_list:
        button.configure(bg=style.lookup('TButton','background'),fg=style.lookup('TButton','foreground'))
    root.update_idletasks()

root = tk.Tk()
root.geometry("300x275")
root.title("My Simple Calculator")

menubar = Menu(root)
theme_menu = Menu(menubar, tearoff=0)
theme_menu.add_command(label="Dark", command=set_dark_theme)
theme_menu.add_command(label="Light", command=set_light_theme)
menubar.add_cascade(label="Theme", menu=theme_menu)
root.config(menu=menubar)

style = ThemedStyle(root)
style.set_theme("breeze")



results = tk.Text(root,height=2,width=16, font=('Open Sans',24))
results.grid(columnspan=5)
results.grid(padx=1.5)


btn_openbracket = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=5, font=('Open Sans', 14))
btn_openbracket.grid(row=2, column=1)


btn_closebracket = tk.Button(root, text=")", command=lambda: add_to_calculation(")"),width=5, font=('Open Sans', 14))
btn_closebracket.grid(row=2, column=2)

btn_percent = tk.Button(root, text="%", command=lambda: add_to_calculation("%"),width=5, font=('Open Sans', 14))
btn_percent.grid(row=2, column=3)

btn_clear = tk.Button(root, text="AC", command=clear_field,width=5, font=('Open Sans', 14))
btn_clear.grid(row=2, column=4)

btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7),width=5, font=('Open Sans', 14))
btn_7.grid(row=3, column=1)

btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8),width=5, font=('Open Sans', 14))
btn_8.grid(row=3, column=2)

btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9),width=5, font=('Open Sans', 14))
btn_9.grid(row=3, column=3)

btn_division = tk.Button(root, text="/", command=lambda: add_to_calculation("/"),width=5, font=('Open Sans', 14))
btn_division.grid(row=3, column=4)

btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4),width=5, font=('Open Sans', 14))
btn_4.grid(row=4, column=1)

btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5),width=5, font=('Open Sans', 14))
btn_5.grid(row=4, column=2)

btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6),width=5, font=('Open Sans', 14))
btn_6.grid(row=4, column=3)

btn_multiply= tk.Button(root, text="*", command=lambda: add_to_calculation("*"),width=5, font=('Open Sans', 14))
btn_multiply.grid(row=4, column=4)

btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1),width=5, font=('Open Sans', 14))
btn_1.grid(row=5, column=1)

btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2),width=5, font=('Open Sans', 14))
btn_2.grid(row=5, column=2)

btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3),width=5, font=('Open Sans', 14))
btn_3.grid(row=5, column=3)

btn_subtract = tk.Button(root, text="-", command=lambda: add_to_calculation("-"),width=5, font=('Open Sans', 14))
btn_subtract.grid(row=5, column=4)

btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0),width=5, font=('Open Sans', 14))
btn_0.grid(row=6, column=1)

btn_stop = tk.Button(root, text=".", command=lambda: add_to_calculation("."),width=5, font=('Open Sans', 14))
btn_stop.grid(row=6, column=2)

btn_equals = tk.Button(root, text="=", command=lambda: evaluate_calculation(),width=5, font=('Open Sans', 14))
btn_equals.grid(row=6, column=3)

btn_addition = tk.Button(root, text="+", command=lambda: add_to_calculation("+"),width=5, font=('Open Sans', 14))
btn_addition.grid(row=6, column=4)





root.mainloop()
