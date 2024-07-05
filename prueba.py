#------NO CAMBIAR ---------
from autoHerramientas import *
#---------------------------
#puede cargar cualquier archivo cambiando este parametro
nombre_archivo = "Autos1"

#puede cambiar la forma de la lista entre:
#lista de diccionario -> tipo_lista = "diccionario"
#lista de listas -> tipo_lista = "lista"
tipo_lista = "diccionario"

lista_autos = obtenerAutos(nombre_archivo,tipo_lista)

#-----------------------------------------------------------------
def buscar_auto_marca_modelo(dato1:str)-> dict:
    return

print(("-")*100)



        
opcion_menu={
    "buscar auto por modelo":["buscar por modelo"],
    "buscar auto por color":["buscar por color"],
    "buscar auto por marca":["buscar por marca"],}

for llave in opcion_menu: 
    print(llave,"->",opcion_menu[llave])
    
    
print(("-")*100)        
selec=input("ingrese una de las opciones: ")

if selec in opcion_menu["buscar auto por marca"]:
    Pregunta_marca=input("ingrese la marca que desea buscar: ")
    m=Pregunta_marca.capitalize()
    for n in lista_autos:
        if m in n["marca"]:
            print(("-")*120)
            var1=print("marca :",n["marca"])
            var2=print("modelo :",n["modelo"])
            var3=print("año :",n["año"])
            var4=print("patente :",n["patente"])
            var5=print("color :",n["color"])
            

        
if selec in opcion_menu["buscar auto por modelo"]:#✔️
    pregunta_modelo=input("ingrese modelo de auto :")
    x=pregunta_modelo.capitalize()
    for i in lista_autos:
            if x in i["modelo"]:
                print(("*")*100)
                var1=print("marca :",i["marca"])
                var2=print("modelo :",i["modelo"])
                var3=print("año :",i["año"])
                var4=print("patente :",i["patente"])
                var5=print("color :",i["color"])
                
    

           


if selec in opcion_menu["buscar auto por color"]:
    pregunta=input("ingrese color: ")
    v=pregunta.capitalize()
    for i in lista_autos:
        if v in i["color"]:
            print(("-")*120)
            var1=print("marca :",i["marca"])
            var2=print("modelo :",i["modelo"])
            var3=print("año :",i["año"])
            var4=print("patente :",i["patente"])
            var5=print("color :",i["color"])
                                
