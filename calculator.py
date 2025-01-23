import tkinter as tk

def calculator():
    cal = eval(b.get())
    label.config(text=cal)

a = tk.Tk()
a.title("Calculator")

b = tk.Entry(a, width=100)
b.pack(pady=10)

button = tk.Button(a, text="evaluate", command=calculator)
button.pack(pady=10)

label = tk.Label(a,text="")
label.pack(pady=20)

a.mainloop()