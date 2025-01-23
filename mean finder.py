import tkinter as tk
import numpy as np

def mean_is():
    a=entry.get()
    b=[int(c) for c in a.split()]
    d=np.mean(b)
    label.config(text=f'The mean is: {d:.2f}')

dis=tk.Tk()
dis.title("mean finder")

entry=tk.Entry(dis,width=100)
entry.pack(pady=10)

button=tk.Button(dis,text="Calculate Mean",command=mean_is)
button.pack(pady=10)

label=tk.Label(dis,text="")
label.pack(pady=20)

dis.mainloop()