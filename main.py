#IMPORTAMOS LAS LIBRERIAS DE INTERÉS
from openpyxl import load_workbook
from tkinter import *
import random

'''IMPORTAMOS LOS DATOS DE NUESTRAS HOJAS DE EXCEL'''
#Cargamos el archivo de datos
data_file = load_workbook("datos.xlsx")
#Obtenemos los nombres de las hojas
hojas=data_file.sheetnames
#Abrimos cada hoja en una variable diferente
key=data_file[hojas[0]]
data=data_file[hojas[1]]
#Crear la matriz de preguntas y respuestas en base al archivo de excel
pre_res=[]
for i, row in enumerate(key):
    if i==0:
        continue
    pre_res.append([row[0].value,row[1].value])

'''FUNCIÓN PARA QUE SELECCIONEMOS LAS PREGUNTAS QUE QUEREMOS QUE NUESTRO USUARIO RESPONDA'''
def seleccion_preguntas():
    global seleccion
    #Determinamos la cantidad de preguntas que hay
    cant_preguntas=len(pre_res)

    #Creamos una lista con los numeros del 0 hasta la cantidad de preguntas disponibles
    seleccion=[]
    for i in range(0, cant_preguntas):
        seleccion.append(i)

    #Quitamos tantos valores cómo sean necesarios para solo tener 10
    for i in range(0, cant_preguntas-10):
        seleccion.remove(random.choice(seleccion))

'''
#Variable para contar respuestas correctas
correctas=0
#Ciclo que repetirá 10 veces
for i in range(0,10):
    #Imprimir la pregunta
    print(f"\n{i+1}.- {pre_res[seleccion[i]][0]}")
    #Pedir la respuesta
    respuesta=input("\n>>> ")
    if respuesta==pre_res[seleccion[i]][1]:
        correctas+=1
'''

#data_file.save("datos.xlsx")

'''TKINTER'''
#Ventana madre
main=Tk()

#Imagenes
logo=PhotoImage(file="logo.png")
bg=PhotoImage(file="fondo1.png")

#Ventana de inicio
main.title("Quiz PLI")
main.geometry("500x800")
main.config(bg="#373D64")
main.columnconfigure(0, weight=1)
main.rowconfigure(0, weight=1)
main.rowconfigure(1, weight=1)
main.rowconfigure(2, weight=1)
main.resizable(0, 0)

#Ventana de Ingreso
w1=Toplevel(main)
w1.title("Ingreso")
w1.geometry("500x800")
w1.config(bg="#373D64")
w1.resizable(0, 0)
w1.columnconfigure(0, weight=1)
w1.rowconfigure(0, weight=1)
w1.rowconfigure(1, weight=1)
w1.rowconfigure(2, weight=1)
w1.rowconfigure(3, weight=1)

#Ventana de Registro
w2=Toplevel(main)
w2.title("Registro")
w2.geometry("500x800")
w2.config(bg="#373D64")
w2.resizable(0, 0)
w2.columnconfigure(0, weight=1)
for i in range(0,5):
    w2.rowconfigure(i, weight=1)

#Ventana de Bienvenida y Datos
w3=Toplevel(main)
w3.title("Quiz PLI")
w3.geometry("500x800")
w3.config(bg="#373D64")
w3.resizable(0, 0)
w3.columnconfigure(0, weight=1)
w3.rowconfigure(0, weight=1)
w3.rowconfigure(1, weight=1)
w3.rowconfigure(2, weight=1)
w3.rowconfigure(3, weight=1)

#Ventana de Preguntas
w4=Toplevel(main)
w4.title("Preguntas")
w4.geometry("500x800")
w4.config(bg="#373D64")
w4.resizable(0, 0)
w4.columnconfigure(0, weight=1)
w4.rowconfigure(0, weight=1)
w4.rowconfigure(1, weight=1)
w4.rowconfigure(2, weight=1)
w4.rowconfigure(3, weight=1)

#Ventana de Resultados
w5=Toplevel(main)
w5.title("Resultados")
w5.geometry("500x800")
w5.config(bg="#373D64")
w5.resizable(0, 0)
w5.columnconfigure(0, weight=1)
w5.rowconfigure(0, weight=1)
w5.rowconfigure(1, weight=1)
w5.rowconfigure(2, weight=1)
w5.rowconfigure(3, weight=1)

#Formatos
label_f = {"bg": ("#373D64"), "fg": ("White")}
button_f = {"fg": ("#373D64")}
title = {"font": (None, 40)}
subtitle = {"font": (None, 30)}
text = {"font": (None, 20)}

'''Funciones'''
#Cerrar y abrir ventanas
def abrir_ingreso():
    main.iconify()
    w1.deiconify()

def abrir_registro():
    main.iconify()
    w2.deiconify()

def ingresar():
    w1.iconify()
    w3.deiconify()

def registrar():
    w2.iconify()
    w3.deiconify()

def empezar_examen():
    w3.iconify()
    w4.deiconify()

def cerrar_sesion():
    w3.iconify()
    main.deiconify()
'''
def avanzar_preguntas():
    #Actualizar w4
'''    

def terminar_preguntas():
    w4.iconify()
    w5.iconify()

def repetir():
    w5.iconify()
    w4.deiconify()

def regresar():
    w5.iconify()
    w3.deiconify()

def salir():
    main.destroy()

#Colocar fondo
bgl_main=Label(main, image=bg, **label_f).place(x=-1, y=-1)
bgl_w1=Label(w1, image=bg, **label_f).place(x=-1, y=-1)
bgl_w2=Label(w2, image=bg, **label_f).place(x=-1, y=-1)
bgl_w3=Label(w3, image=bg, **label_f).place(x=-1, y=-1)
bgl_w4=Label(w4, image=bg, **label_f).place(x=-1, y=-1)
bgl_w5=Label(w5, image=bg, **label_f).place(x=-1, y=-1)

#Elementos Ventana Inicio
l1_main=Label(main, image=logo, **label_f).pack(pady=40)
b1_main=Button(main, text="Ingresar", **subtitle, command=sayHello).pack(pady=40)
b2_main=Button(main, text="Registrarse", **subtitle, **button_f).pack(pady=40)
b3_main=Button(main, text="Salir", **subtitle, **button_f).pack(pady=40)

#Elementos Ventana de Ingreso
l1_w1=Label(w1, text="Ingresar", **title, **label_f).grid(row=0, column=0)
l2_w1=Label(w1, text="Matrícula:", **subtitle, **label_f).grid(row=1, column=0, sticky=N)
l3_w1=Label(w1, text="Contraseña:", **subtitle, **label_f).grid(row=2, column=0, sticky=N)
e1_w1=Entry(w1, **subtitle).grid(row=1, column=0, sticky=N, pady=50)
e2_w1=Entry(w1, **subtitle).grid(row=2, column=0, sticky=N, pady=50)
b1_w1=Button(w1, text="Ingresar", **subtitle, **button_f).grid(row=3, column=0)

#Elementos Ventana de Registro
l1_w2=Label(w2, text="Registro", **title, **label_f).grid(row=0, column=0)
l2_w2=Label(w2, text="Matrícula:", **subtitle, **label_f).grid(row=1, column=0, sticky=N)
l3_w2=Label(w2, text="Contraseña:", **subtitle, **label_f).grid(row=2, column=0, sticky=N)
l4_w2=Label(w2, text="Nombre:", **subtitle, **label_f).grid(row=3, column=0, sticky=N)
e1_w2=Entry(w2, **subtitle).grid(row=1, column=0, sticky=N, pady=50)
e2_w2=Entry(w2, **subtitle).grid(row=2, column=0, sticky=N, pady=50)
e3_w2=Entry(w2, **subtitle).grid(row=3, column=0, sticky=N, pady=50)
b1_w2=Button(w2, text="Ingresar", **subtitle, **button_f).grid(row=4, column=0)

#Elementos Ventana de Bienvenida y Datos
l1_w3=Label(w3, text="Bienvenido, usuario", **title, **label_f).grid(row=0, column=0)
l2_w3=Label(w3, text="Calificación\nactual: 90/100", **subtitle, **label_f).grid(row=1, column=0)
b1_w3=Button(w3, text="Realizar examen", **subtitle, **button_f).grid(row=2, column=0)
b2_w3=Button(w3, text="Cerrar sesión", **subtitle, **button_f).grid(row=3, column=0)

#Elementos Ventana Preguntas
l1_w4=Label(w4, text="1.-¿Pregunta?", **text, **label_f).grid(row=0, column=0)
l2_w4=Label(w4, text="Respuesta:", **subtitle, **label_f).grid(row=1, column=0)
e1_w4=Entry(w4, **subtitle).grid(row=1, column=0, sticky=N, pady=50)
b1_w4=Button(w4, text="Siguiente", **subtitle, **button_f).grid(row=2, column=0)

#Elementos Ventana de Bienvenida y Datos
l1_w5=Label(w5, text="Felicidades usuario, has aprobado", **title, **label_f).grid(row=0, column=0)
l2_w5=Label(w5, text="Tú calificación\nes de: 99/100", **subtitle, **label_f).grid(row=1, column=0)
b1_w5=Button(w5, text="Repetir examen", **subtitle, **button_f).grid(row=2, column=0)
b2_w5=Button(w5, text="Regresar", **subtitle, **button_f).grid(row=3, column=0)

main.mainloop()