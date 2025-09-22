from tkinter import *
from tkcalendar import Calendar, DateEntry
from tkinter import ttk
from datetime import datetime

def mostrar_hora():
    # Obtener los valores seleccionados
    hora = int(hora_spinbox.get())
    minuto = minuto_spinbox.get()
    segundo = segundo_spinbox.get()
    print(f"La hora seleccionada es: {hora}:{minuto}:{segundo}")

    # Determinar la actividad según la hora
    if 0 <= hora < 8:
        print("Durmiendo.")
    elif 9 <= hora < 18:
        print("Trabajando.")
    elif 19 <= hora < 21 or 22 <= hora < 24:
        print("Descanso")
    else:
        print("Hora no válida.")

# Crear la ventana principal
ventana = Tk()
ventana.title("Selector de Hora")

# Crear los spinbox para hora, minuto y segundo
hora_spinbox = ttk.Spinbox(ventana, from_=0, to=23, width=5, format="%02.0f")
minuto_spinbox = ttk.Spinbox(ventana, from_=0, to=59, width=5, format="%02.0f")
segundo_spinbox = ttk.Spinbox(ventana, from_=0, to=59, width=5, format="%02.0f")

# Colocar los elementos en la ventana
Label(ventana, text="Hora:").grid(row=0, column=0)
hora_spinbox.grid(row=0, column=1)
Label(ventana, text="Minuto:").grid(row=0, column=2)
minuto_spinbox.grid(row=0, column=3)
Label(ventana, text="Segundo:").grid(row=0, column=4)
segundo_spinbox.grid(row=0, column=5)

# Botón para mostrar la hora seleccionada
Button(ventana, text="Mostrar hora", command=mostrar_hora).grid(row=1, column=0, columnspan=6)

ventana.mainloop()
