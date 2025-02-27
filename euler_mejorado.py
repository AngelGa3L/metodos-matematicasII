import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from math import *

def euler_mejorado(f, x0, y0, h, xf):
    resultados = []
    x = x0
    y = y0
    n = 0  
    while x < xf + h / 2:  
        y_pred = y + h * eval(f, {'x': x, 'y': y})  
        y_corr = y + h/2 * (eval(f, {'x': x, 'y': y}) + eval(f, {'x': x + h, 'y': y_pred}))  
        resultados.append((n, x, y, y_pred))  
        y = y_corr
        x = x + h
        n += 1  
    return resultados

def resolver():
    try:
        f = entrada_funcion.get()
        x0 = float(entrada_x0.get())
        y0 = float(entrada_y0.get())
        h = float(entrada_h.get())
        xf = float(entrada_xf.get())
        
        resultados = euler_mejorado(f, x0, y0, h, xf)
        
        
        tabla.delete(*tabla.get_children())
        for n, x, y, y_pred in resultados:
            tabla.insert("", "end", values=(n, x, y, y_pred)) 
        
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")


ventana = tk.Tk()
ventana.title("Método de Euler Mejorado")


tk.Label(ventana, text="Función (** para potencia y *para multiplicar):").grid(row=0, column=0, padx=10, pady=10)
entrada_funcion = tk.Entry(ventana)
entrada_funcion.grid(row=0, column=1, padx=10, pady=10)

tk.Label(ventana, text="x0:").grid(row=1, column=0, padx=10, pady=10)
entrada_x0 = tk.Entry(ventana)
entrada_x0.grid(row=1, column=1, padx=10, pady=10)

tk.Label(ventana, text="y0:").grid(row=2, column=0, padx=10, pady=10)
entrada_y0 = tk.Entry(ventana)
entrada_y0.grid(row=2, column=1, padx=10, pady=10)

tk.Label(ventana, text="h:").grid(row=3, column=0, padx=10, pady=10)
entrada_h = tk.Entry(ventana)
entrada_h.grid(row=3, column=1, padx=10, pady=10)

tk.Label(ventana, text="xf:").grid(row=4, column=0, padx=10, pady=10)
entrada_xf = tk.Entry(ventana)
entrada_xf.grid(row=4, column=1, padx=10, pady=10)

boton_resolver = tk.Button(ventana, text="Resolver", command=resolver)
boton_resolver.grid(row=5, column=0, columnspan=2, pady=10)

#Crear la tabla 
columnas = ("n", "x", "y", "(Yn+1)*")  
tabla = ttk.Treeview(ventana, columns=columnas, show="headings")  
tabla.heading("n", text="n")  
tabla.heading("x", text="x")
tabla.heading("y", text="y")
tabla.heading("(Yn+1)*", text="(Yn+1)*")  
tabla.grid(row=6, column=0, columnspan=2, padx=10, pady=10)


ventana.mainloop()