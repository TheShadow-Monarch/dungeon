import tkinter as tk
import numpy as np

def mean_is():

    try:
        a=entry.get()
        b=[float(c) for c in a.split()]
        d=np.mean(b)
        label.config(text=f'The mean is: {d:.2f}')
    except ValueError:
        label.config(text="Input must be numbers or decimals")
    except SyntaxError:
        label.config(text="Input must be numbers or decimals")

dis=tk.Tk()
dis.title("mean finder")

label1=tk.Label(dis,text="Give your input followed by a space!😊")
label1.pack(pady=10)

entry=tk.Entry(dis,width=100)
entry.pack(pady=10)

label2 = tk.Label(dis,text="Click on Enter to get the results and press escape to exit!!!")
label2.pack(pady=30)

dis.bind('<Return>', lambda event: mean_is())
dis.bind("<Escape>",lambda event: exit())

label=tk.Label(dis,text="")
label.pack(pady=20)

dis.mainloop()