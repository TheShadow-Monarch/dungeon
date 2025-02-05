import tkinter as tk

def calculator():
    try:
        cal = eval(b.get())
        label.config(text=(f"Result: {cal:.2f}"))
    except ValueError:
        label.config(text="Input must be numbers or decimals")
    except SyntaxError:
        label.config(text="Input must be numbers or decimals")
    except Exception:
        label.config(text="There is some error from your input")

a = tk.Tk()
a.title("Calculator")

b = tk.Entry(a, width=100)
b.pack(pady=10)

button = tk.Button(a, text="evaluate", command=calculator)
button.pack(pady=10)

label = tk.Label(a,text="")
label.pack(pady=20)

a.mainloop()
