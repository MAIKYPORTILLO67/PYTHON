import tkinter as tk
from tkinter import *
from random import randint

movimiento = 0
bandera = 0
###FUNCIONES

def aleatorio():
    lista=[]
    for i in range(9):
        while True:
            numero = randint(0,8)
            if numero not in lista:
                break
            lista.append(numero)
    return lista

def posicion(lista):
    lista=[]
    for i in range(9):
        if(texto[i]==0):
            lista.append("")
        else:
            lista.append(texto[i])
    texto_1.set(lista[0])
    texto_2.set(lista[1])
    texto_3.set(lista[2])
    texto_4.set(lista[3])
    texto_5.set(lista[4])
    texto_6.set(lista[5])
    texto_7.set(lista[6])
    texto_8.set(lista[7])
    texto_9.set(lista[8])

def movimientos(numerox, numeroy, lista):
    global movimiento
    global bandera
    ubicacion=((numeroy*3)+numerox)
    if(bandera==0):
        if((numerox-1)>=0):
            posicion=(((numeroy)*3)+numerox-1)
            if(lista[posicion]==0):
                burbuja=lista[ubicacion]
                lista[ubicacion]-lista[posicion]
                lista[posicion]-burbuja
                movimiento+=1
        if((numerox+1)<=2):
            posicion=(((numeroy)*3)+numerox+1)
            if(lista[posicion]==0):
                burbuja=lista[ubicacion]
                lista[ubicacion]-lista[posicion]
                lista[posicion]-burbuja
                movimiento+=1
        if((numeroy-1)>=0):
            posicion=(((numeroy-1)*3)+numerox)
            if(lista[posicion]==0):
                burbuja=lista[ubicacion]
                lista[ubicacion]-lista[posicion]
                lista[posicion]-burbuja
                movimiento+=1
        if((numeroy+1)<=2):
            posicion=(((numeroy+1)*3)+numerox)
            if(lista[posicion]==0):
                burbuja=lista[ubicacion]
                lista[ubicacion]-lista[posicion]
                lista[posicion]-burbuja
                movimiento+=1
    posicion(lista)
    texto_movimiento.set(movimiento)

###OBJETOS Y SU POSICION
###nombre y dimensiones de la ventana
ventana = tk.Tk()
ventana.title("ROMPECABEZAS")
ventana.geometry("380x520")

###label que llevara el nombre del juego
etiqueta = tk.Label(ventana, text="NUMPUZ", font = ('Comic sens MC',25,'bold'))
etiqueta.grid(row=0, column = 0, padx = 0, pady = 0)

###recuadro que mantiene juntos los botones
recuadro = Frame (ventana, bg= 'gray')
recuadro.grid(column = 0,row = 2,padx = 3, pady = 3)

texto_1=StringVar()
texto_2=StringVar()
texto_3=StringVar()
texto_4=StringVar()
texto_5=StringVar()
texto_6=StringVar()
texto_7=StringVar()
texto_8=StringVar()
texto_9=StringVar()
texto_movimiento=StringVar()

texto=aleatorio()
texto_movimiento.set("0")

posicion(texto)

### botones principales del juego
boton1 = tk.Button(recuadro, textovar=texto_1, borderwidth = 4 , height = 2, width = 5, font = ('Comic sens MC',25,'bold'), bg= 'orange', activebackground = "light green", command = lambda:  posicion(0,0))
boton1.grid(row= 2, column = 0,padx = 5, pady = 5)

boton2 = tk.Button(recuadro, textovar=texto_2, borderwidth = 4 , height = 2, width = 5, font = ('Comic sens MC',25,'bold'), bg= 'orange', activebackground = "light green", command = lambda:  posicion(0,1))
boton2.grid(row= 2, column = 1,padx = 5, pady = 5)

boton3 = tk.Button(recuadro, textovar=texto_3, borderwidth = 4 , height = 2, width = 5, font = ('Comic sens MC',25,'bold'), bg= 'orange', activebackground = "light green", command = lambda:  posicion(0,2))
boton3.grid(row= 2, column = 2,padx = 5, pady = 5)

boton4 = tk.Button(recuadro, textovar=texto_4, borderwidth = 4 , height = 2, width = 5, font = ('Comic sens MC',25,'bold'), bg= 'orange', activebackground = "light green", command = lambda:  posicion(1,0))
boton4.grid(row= 3, column = 0,padx = 5, pady = 5)

boton5 = tk.Button(recuadro, textovar=texto_5, borderwidth = 4 , height = 2, width = 5, font = ('Comic sens MC',25,'bold'), bg= 'orange', activebackground = "light green", command = lambda:  posicion(1,1))
boton5.grid(row= 3, column = 1,padx = 5, pady = 5)

boton6 = tk.Button(recuadro, textovar=texto_6, borderwidth = 4 , height = 2, width = 5, font = ('Comic sens MC',25,'bold'), bg= 'orange', activebackground = "light green", command = lambda:  posicion(1,2))
boton6.grid(row= 3, column = 2,padx = 5, pady = 5)

boton7 = tk.Button(recuadro, textovar=texto_7, borderwidth = 4 , height = 2, width = 5, font = ('Comic sens MC',25,'bold'), bg= 'orange', activebackground = "light green", command = lambda:  posicion(2,0))
boton7.grid(row= 4, column = 0,padx = 5, pady = 5)

boton8 = tk.Button(recuadro, textovar=texto_8, borderwidth = 4 , height = 2, width = 5, font = ('Comic sens MC',25,'bold'), bg= 'orange', activebackground = "light green", command = lambda:  posicion(2,1))
boton8.grid(row= 4, column = 1,padx = 5, pady = 5)

boton9 = tk.Button(recuadro, textovar=texto_9, borderwidth = 4 , height = 2, width = 5, font = ('Comic sens MC',25,'bold'), bg= 'orange', activebackground = "light green", command = lambda:  posicion(2,2))
boton9.grid(row= 4, column = 2,padx = 5, pady = 5)

###label para el contador de movimentos
movimiento = tk.Label(ventana, textovar=texto_movimiento, font = ('Comic sens MC',25,'bold'))
movimiento.grid(row=5, column = 1, padx = 5, pady = 5)
etiqueta = tk.Label(ventana, text="NUMERO DE MOVIMIENTOS: ", font = ('Comic sens MC',10,'bold'))
etiqueta.grid(row=5, column = 0, padx = 5, pady = 5)

###boton para el reincio del juego
botonreiniciar = tk.Button(text="REINICIAR", borderwidth = 4 , height = 1, width = 9, font = ('Comic sens MC',25,'bold'), bg= 'orange', activebackground = "light green")
botonreiniciar.grid(row= 6, column = 0, padx = 5, pady = 5)

###el loop que mantendra nuestra ventana abierta
ventana.mainloop()