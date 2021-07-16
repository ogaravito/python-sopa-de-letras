from tkinter import *
import itertools

matriz = []
palabras = []
lista_labels = []
lista_botones = []
botones_presionados=[]
ultimo_indice = None
direccion = None
palabra=''

with open("palabras.txt", "r") as f:
    palabras = [ linea.strip("\n") for linea in f]

with open("sopa.txt","r") as f:
    matriz = [ linea.split() for linea in f ]

def limpiar():
    global palabra
    global ultimo_indice
    global direccion
    palabra = ''
    ultimo_indice=None
    direccion=None
    for i in botones_presionados:
        btn = lista_botones[i]
        btn.configure(bg="lightgray")

def clic_boton(pos_btn,indice):
    global palabra
    global ultimo_indice
    global direccion
    global botones_presionados
    
    dif_fila=0
    dif_col=0
    
    if ultimo_indice == None:
        ultimo_indice = indice[:]

    dif_fila = indice[0]-ultimo_indice[0]
    dif_col = indice[1]-ultimo_indice[1]

    if dif_fila in [-1,0,1] and dif_col in range(-1,2):
        
        if direccion == None and (dif_fila!=0 or dif_col!=0):
            direccion = (dif_fila,dif_col)
        if direccion != None:
            if (dif_fila,dif_col) != direccion:
                return 
        btn = lista_botones[pos_btn]
        btn.configure(bg="lightblue")
        botones_presionados.append(pos_btn)
        palabra += btn['text']
        lst_palabra = list(palabra)
        permutaciones = list(itertools.permutations(lst_palabra))
        for i in range(len(permutaciones)):
            word = "".join(permutaciones[i])
            if word in palabras:
                for label in lista_labels:
                    if label['text']==word:
                        label.configure(bg="orange")
                        botones_presionados=[]
                        limpiar()
                        return
        ultimo_indice = indice[:]

ventana = Tk()
ventana.title("SOPA DE LETRAS")

indice_boton = 0
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        pos = [i,j]
        boton = Button(ventana, text=matriz[i][j], command=lambda arg1=indice_boton,arg2=pos:clic_boton(arg1,arg2), bg="lightgray")
        boton.grid(row=i, column=j,  sticky="nsew")
        lista_botones.append(boton)
        indice_boton+=1
k=0
for i in palabras:
    texto = Label(ventana, text=i)
    texto.grid(row=k, column=j+1)
    lista_labels.append(texto)
    k+=1

boton = Button(ventana, text="Limpiar", command=limpiar, bg="#666", fg="white")
boton.grid(row=0, column=j+2,  sticky="nsew", rowspan=2)

ventana.mainloop()