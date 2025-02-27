import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from math import *

def runge_kutta_4th_order():
    try:
       
        func = func_entry.get()
        x0 = float(x0_entry.get())
        y0 = float(y0_entry.get())
        h = float(h_entry.get())
        xf = float(xf_entry.get())

        
        for row in table.get_children():
            table.delete(row)

        
        xn = x0
        yn = y0
        n = 0

       
        while xn < xf + h / 2:  
            
            k1 = h * eval(func, {"x": xn, "y": yn})
            k2 = h * eval(func, {"x": xn + h/2, "y": yn + k1/2})
            k3 = h * eval(func, {"x": xn + h/2, "y": yn + k2/2})
            k4 = h * eval(func, {"x": xn + h, "y": yn + k3})

            yn1 = yn + (k1 + 2*k2 + 2*k3 + k4) / 6  # Actualizar y

            
            table.insert('', 'end', values=(n, round(xn, 5), round(yn, 5), 
                                            round(k1, 5), round(k2, 5), 
                                            round(k3, 5), round(k4, 5), 
                                            round(yn1, 5)))

            
            yn = yn1
            xn += h
            n += 1

    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")


root = tk.Tk()
root.title("Runge-Kutta 4° Orden")


tk.Label(root, text="Función (use 'x' y 'y' como variables):").grid(row=0, column=0, padx=10, pady=10)
func_entry = tk.Entry(root, width=30)
func_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="x0:").grid(row=1, column=0, padx=10, pady=10)
x0_entry = tk.Entry(root, width=10)
x0_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="y0:").grid(row=2, column=0, padx=10, pady=10)
y0_entry = tk.Entry(root, width=10)
y0_entry.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="h:").grid(row=3, column=0, padx=10, pady=10)
h_entry = tk.Entry(root, width=10)
h_entry.grid(row=3, column=1, padx=10, pady=10)

tk.Label(root, text="xf:").grid(row=4, column=0, padx=10, pady=10)
xf_entry = tk.Entry(root, width=10)
xf_entry.grid(row=4, column=1, padx=10, pady=10)

tk.Button(root, text="Calcular", command=runge_kutta_4th_order).grid(row=5, column=0, columnspan=2, pady=10)

#Crear la tabla
columns = ("n", "xn", "yn", "k1", "k2", "k3", "k4", "yn+1")
table = ttk.Treeview(root, columns=columns, show="headings")
table.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

for col in columns:
    table.heading(col, text=col)


root.mainloop()
