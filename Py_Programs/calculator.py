import tkinter as tk

def calculator():
        try:
            cal = eval(b.get())
            label.config(text=(f"Result: {cal:.2f}"))
        except ValueError:
            label.config(text="Input must be numbers or decimals followed by operation")
        except SyntaxError:
            label.config(text="Input must be numbers or decimals followed by operation")
        except Exception as e:
             label.config(text=f"Error Found {e}")

a = tk.Tk()
a.title("Calculator")
a.geometry("600x300")

b = tk.Entry(a, width=100)
b.pack(pady=10)

label = tk.Label(a,text="")
label.pack(pady=20)

a.bind('<Return>', lambda event: calculator())
a.bind("<Escape>",lambda event: exit())

a.mainloop()