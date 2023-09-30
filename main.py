import tkinter as tk
from tkinter import ttk

#setup
w = tk.Tk()
w.title('Buttons')
w.geometry('600x400')

#button
def button_func():
    print('A basic button.')
button_string = tk.StringVar(value = 'A button with string var')
button = ttk.Button(w,text='A Simple Button', command=button_func,textvariable=button_string)
button.pack()

#check button
check_var = tk.BooleanVar()
check = ttk.Checkbutton(w, text='Check 1',command=lambda: print(check_var.get()),variable=check_var)
check.pack()

#radio buttons

radio1 = ttk.Radiobutton(w,text='Radio 1',value=1)
radio2 = ttk.Radiobutton(w,text='Radio 2',value='h')
radio1.pack()
radio2.pack()


#run
w.mainloop()

