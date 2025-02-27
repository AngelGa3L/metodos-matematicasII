import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from math import *

def newton_raphson():
    try:
        func = entrada_funcion.get()
        decimales = int(entrada_decimales.get())
        x0 = float(entrada_x0.get())
        
        def f(x):
            return eval(func)
        
        def df(x):
            h = 1e-5
            return (f(x + h) - f(x - h)) / (2 * h)
        
        #Crear la tabla
        tabla.delete(*tabla.get_children())
        
        #Iterar
        tolerancia = 10 ** (-decimales)
        iteracion = 0
        while True:
            fx = f(x0)
            dfx = df(x0)
            if dfx == 0:
                messagebox.showerror("Error", "La derivada es cero. No se puede continuar.")
                return
            x1 = x0 - fx / dfx
            
            tabla.insert("", "end", values=(iteracion, round(x0, decimales), round(fx, decimales), round(dfx, decimales), round(x1, decimales)))
            
            if abs(x1 - x0) < tolerancia:
                break
            x0 = x1
            iteracion += 1
        
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")

ventana = tk.Tk()
ventana.title("Método de Newton-Raphson")

tk.Label(ventana, text="Función (f(x) ** para potencia y *para multiplicar):").grid(row=0, column=0, padx=10, pady=10)
entrada_funcion = tk.Entry(ventana)
entrada_funcion.grid(row=0, column=1, padx=10, pady=10)

tk.Label(ventana, text="Número de decimales:").grid(row=1, column=0, padx=10, pady=10)
entrada_decimales = tk.Entry(ventana)
entrada_decimales.grid(row=1, column=1, padx=10, pady=10)

tk.Label(ventana, text="Valor inicial (x0):").grid(row=2, column=0, padx=10, pady=10)
entrada_x0 = tk.Entry(ventana)
entrada_x0.grid(row=2, column=1, padx=10, pady=10)

boton_calcular = tk.Button(ventana, text="Calcular", command=newton_raphson)
boton_calcular.grid(row=3, column=0, columnspan=2, pady=10)

columnas = ("Iteración", "x0", "f(x0)", "f'(x0)", "x1")
tabla = ttk.Treeview(ventana, columns=columnas, show="headings")
for col in columnas:
    tabla.heading(col, text=col)
tabla.grid(row=4, column=0, columnspan=2, padx=10, pady=10)


ventana.mainloop()