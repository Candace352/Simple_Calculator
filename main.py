import tkinter as tk

root = tk.Tk()

root.geometry("550x500")
root.resizable(0,0)
root.title("My First Simple Calculator")

label = tk.Label(root, text="Simple Calculator",font=('Arial',25))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=2.5, font=('Arial', 16))
textbox.pack(padx=20,pady=15)

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0,weight=1)
buttonframe.columnconfigure(1,weight=1)
buttonframe.columnconfigure(2,weight=1)
buttonframe.columnconfigure(3,weight=1)

btn1 = tk.Button(buttonframe, text="(",font =('Arial', 18))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(buttonframe, text=")",font =('Arial', 18))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(buttonframe, text="%",font =('Arial', 18))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

btn3 = tk.Button(buttonframe, text="AC",font =('Arial', 18))
btn3.grid(row=0, column=3, sticky=tk.W+tk.E)

btn4 = tk.Button(buttonframe, text="7",font =('Arial', 18))
btn4.grid(row=1, column=0, sticky=tk.W+tk.E)

btn5 = tk.Button(buttonframe, text="8",font =('Arial', 18))
btn5.grid(row=1, column=1, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonframe, text="9",font =('Arial', 18))
btn6.grid(row=1, column=2, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonframe, text="/",font =('Arial', 18))
btn6.grid(row=1, column=3, sticky=tk.W+tk.E)

btn4 = tk.Button(buttonframe, text="4",font =('Arial', 18))
btn4.grid(row=2, column=0, sticky=tk.W+tk.E)

btn5 = tk.Button(buttonframe, text="5",font =('Arial', 18))
btn5.grid(row=2, column=1, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonframe, text="6",font =('Arial', 18))
btn6.grid(row=2, column=2, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonframe, text="x",font =('Arial', 18))
btn6.grid(row=2, column=3, sticky=tk.W+tk.E)

btn4 = tk.Button(buttonframe, text="1",font =('Arial', 18))
btn4.grid(row=3, column=0, sticky=tk.W+tk.E)

btn5 = tk.Button(buttonframe, text="2",font =('Arial', 18))
btn5.grid(row=3, column=1, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonframe, text="3",font =('Arial', 18))
btn6.grid(row=3, column=2, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonframe, text="-",font =('Arial', 18))
btn6.grid(row=3, column=3, sticky=tk.W+tk.E)

btn4 = tk.Button(buttonframe, text="0",font =('Arial', 18))
btn4.grid(row=4, column=0, sticky=tk.W+tk.E)

btn5 = tk.Button(buttonframe, text=".",font =('Arial', 18))
btn5.grid(row=4, column=1, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonframe, text="=",font =('Arial', 18))
btn6.grid(row=4, column=2, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonframe, text="+",font =('Arial', 18))
btn6.grid(row=4, column=3, sticky=tk.W+tk.E)

buttonframe.pack(fill='x')


root.mainloop()
