# -*- coding: utf-8 -*-
"""
Created on Sun May 10 17:08:19 2020

@author: juanj
"""
#%%

import matplotlib.pyplot as plt
import webbrowser
import sys

# Set the encoding to UTF-8 for stdout
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8')

import matplotlib.pyplot as plt
import webbrowser
print(" ʕ•́؈•̀) Clínica Pediatra 'Patucos' ʕ•́؈•̀) ")
print("Bienvenido a la clínica Pediatra Patucos estaremos encantados de atenderle.")
print("En especial en este departamento se atenderá  durante los dos primeros años de vida de su bebé. ")
print("    ~~ʕ´•ᴥ•`ʔ~~ʕ´•ᴥ•`ʔ~~ʕ´•ᴥ•`ʔ~~ʕ´•ᴥ•`ʔ~~ʕ´•ᴥ•`ʔ~~ʕ´•ᴥ•`ʔ~~ʕ´•ᴥ•`ʔ~~ʕ´•ᴥ•`ʔ~~")

def menuprincipal():
        
    while True:
        print("¿En qué le podemos ayudar?")
        print("Elija el numero delante de las opciones para ejecutarla.")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("1.¿Es la primera vez que viene?, De de alta a su hijo.")
        print("2.¿Desea buscar a su hijo en el registro?")
        print("3.Imprimir número de niños dados de alta y sus datos.")
        print("4.Dar de baja a su hijo")
        print("5.Calculo teórico del peso del bebé.")
        print("6.Gráfica de lactancia")
        print("7.Para finalizar el programa y guardar los datos.")
        try:
            opcion = int(input("Opcion: "))
            if opcion > 0 and opcion < 8:
                break 
            else:
                print("¯\_(ツ)_/¯ERROR en opcion, introduzca un número entre esas opciones.¯\_(ツ)_/¯")
        except:
            print("¯\_(ツ)_/¯Ha sucedido un ERROR, la edad debe introducirse como número.¯\_(ツ)_/¯")
    return opcion




def añadir(niños):
    """
    Devuelve una lista con todos los datos del niño que el propio usuario introduzca.
    
    Valor de retorno:
        Si el valor que se asigna a edad es correcto se añade a la lista.
        Si por el contrario es negativo o mayor que los 24 meses salta un error.
        
        Si el valor que se asigna a sangre es correcto se añade a la lista.
        Si por el contrario la opción para el grupo sanguíneo no existe salta un error.
        
        Si el valor que se asigna a dni es correcto se añade a la lista.
        Si por el contrario es un valor diferente de 8 o no es un dígito salta un error.
        
        Si el valor que se asigna a pecho es correcto se añade a la lista.
        Si por el contrario la opción de lactancia no existe ,salta un error.
        
        Si el valor que se asigna a nummeses de pesos es correcto se introduce el valor que se 
        le asigne a pesos tantas veces como sea el vaor de numeses y se añade a la lista.
        
    """
    apellidos= input("Apellidos del bebé: ")
    while apellidos == "":
        apellidos = input("Apellidos del bebé:")
    while True:
        try:
            edad = int(input("Edad del niño al darse de alta (en meses): "))
            if edad > 0 and edad < 24:
                break 
            else:
                print("¯\_(ツ)_/¯Ha sucedido un ERROR introduce una edad valida en meses dentro de los 2 años¯\_(ツ)_/¯")
        except:
            print("¯\_(ツ)_/¯Ha sucedido un ERROR, la edad debe introducirse como número.¯\_(ツ)_/¯")
    while True:
        print("¿Seleccione cual es el grupo sanguíneo del niño?")
        print("1==>A")
        print("2==>B")
        print("3==>AB")
        print("4==>0")
        grupo= int(input("Introduzca el número correspondiente al número sanguíneo del niño: "))
        sangre=""
        if grupo < 1 or grupo > 4:
            print("¯\_(ツ)_/¯Error a la hora de elegir.¯\_(ツ)_/¯")
        else:
            if grupo==1:
                sangre="A"
            elif grupo==2:
                sangre="B"
            elif grupo==3:
                sangre="AB"
            elif grupo==4:
                sangre="0"
            break   
    
    while True: 
        dni = input("Introduzca el dni del padre/madre o tutor legal del niño asociado (sin letra): ")
        if len(dni)!= 8 or not dni.isdigit():
            print("¯\_(ツ)_/¯Error. El dni no es valido¯\_(ツ)_/¯")
        else:
            break
    sexo = input("Sexo del niño(V/H): ")
    while sexo != "V" and sexo != "H" and sexo != "v" and sexo != "h":
        sexo = input(" ¯\_(ツ)_/¯ERROR,Introduzca de nuevo el sexo del bebé (V/H): ¯\_(ツ)_/¯")
    
    while True:
        print("Seleccione cual es la lactancia del niño")
        print("1==>natutal")
        print("2==>artificial")
        print("3==>neutra")
        clase= int(input("Introduzca el número correspondiente a la lactancia del niño: "))
        pecho=""
        if clase < 1 or clase > 3:
            print("¯\_(ツ)_/¯Error a la hora de elegir.¯\_(ツ)_/¯")
        else:
            if clase==1:
                pecho="natural"
            elif clase==2:
                pecho="artificial"
            elif clase==3:
                pecho="neutra"
            break  
    while True:
        try:
            print("El peso del niño se mide cada mes")
            nummeses = int(input("¿Cuantos meses se han pesado al niño?"))
            if nummeses>0 and nummeses<24:
                break
            else:
                print("¯\_(ツ)_/¯ERROR, introducir un número menor a 24 meses o positivo.¯\_(ツ)_/¯")
        except:
            print("¯\_(ツ)_/¯ERROR, introducir un número.¯\_(ツ)_/¯")
    pesos= []
    for i in range(nummeses):
        while True:
            try:
                peso = float(input("Peso del niño (Kg)"))
                break
            except:
                print("¯\_(ツ)_/¯Error. El peso debe ser un valor numerico¯\_(ツ)_/¯")
        pesos.append(peso)
   
    niños[dni] = (apellidos,edad,sangre,sexo,pecho,pesos)
    
def imprimir(niños):
    """
    Devuelve la información de los niños que se pasa como parámetro de un diccionario niños.txt si introduces 
    la contraseña correcta. La contraseña se podrá encontrar en los comentarios del video adjuntado. 
    En caso de que no disponga de cuenta en youtube , LA CONTRASEÑA ES : patucos2020.
    
    Argumentos:
        niños-- diccionario donde se encuentran almacenada la inforamción de todos los niños de la clínica.
        contraseña--clave para ejucutar la función.
    Valor de retorno:
        La información archivada de todos los niños del diciionario.
    """
    while True:
        print("A esta opción solo pueden asisitir los trabajadores de la clínica. ")
        print("Si la contraseña es incorrecta automaticamente se abrirá un video de una pediatría")
        print("con la que también trabajamos,en los comentarios del propio video podrá encontrar la contraseña.")
        print("En caso de que no tenga cuennta en youtube acceda a la contraseña en los comentarios de la función con help(imprimir).")
        contraseña=input("Introduce la contraseña:")
        if contraseña=="patucos2020":
            for dni in niños:
                niño = niños[dni]
                print("Apellido niño: ", niño[0])
                print("Edad del niño al darse de alta: ", niño[1])
                print("Grupo sanguíneo del niño: ", niño[2])
                print("Sexo: ", niño[3])
                print("Lactancia: ", niño[4])
                pesos = niño[5]
                for peso in pesos:
                    print(peso, end = " ")

                print("    ~~ʕ´•ᴥ•`ʔ~~ʕ´•ᴥ•`ʔ~~ʕ´•ᴥ•`ʔ~~ʕ´•ᴥ•`ʔ~~ʕ´•ᴥ•`ʔ~~ʕ´•ᴥ•`ʔ~~ʕ´•ᴥ•`ʔ~~ʕ´•ᴥ•`ʔ~~")
            break
        else:
            webbrowser.open("https://www.youtube.com/watch?v=67_Gh8dwErk",new=2,autoraise=True)
            break

def archivar(niños):
    """Archiva los datos introducidos por el usuario de cada niño en el diccionario niños.txt"""
    #     0         1      2      3     4       5
    #  (apellidos, edad, sangre, sexo, pecho, pesos)
    
    fichero = open("niños.txt", "w")
    for dni in niños:
        niño = niños[dni]
        fichero.write(dni + "," + niño[0] + "," + str(niño[1]) + "," +  niño[2] + "," + niño[3] + "," + niño[4])
        fichero.write("|")
        medidas = [str(x) for x in niño[5]]
        cadena = ",".join(medidas)        
        fichero.write(cadena + "\n")
    fichero.close()

def buscar(niños):
    """
    Devuelve la información del niño que se pasa como parámetro de un diccionario niños.txt
    
    Argumentos:
        niño-- mediante el dni asignado a este niño del cual, quieres conocer sus datos.
        niños-- diccionario donde se encuentran almacenada la información de todos los niños de la clínica.
        
    Valor de retorno:
        La información del niño que pasas como parámetro si el dni es correcto.
        Si el dni no esta en el diccionario , el dni es diferente a 8 o no es un dígito, salta  un error.
    """
    while True: 
        dni = input("Introduzca el dni del padre/madre o tutor legal del niño: ")
        if len(dni)!= 8 or not dni.isdigit():
            print("¯\_(ツ)_/¯Error. El dni no es valido¯\_(ツ)_/¯")
        else:
            break
    if dni not in niños:
        print("¯\_(ツ)_/¯Niño no encontrado, de de alta a su hijo en el menú principal¯\_(ツ)_/¯")
    else:
        niño = niños[dni]
        print("Apellido niño:", niño[0])
        print("Edad del niño al darse de alta: ", niño[1])
        print("Grupo sanguíneo del niño: ", niño[2])
        print("Sexo: ", niño[3])
        print("Lactancia: ", niño[4])
        pesos = niño[5]
        for peso in pesos:
            print(peso, end = " ")
    print("    ~~ʕ´•ᴥ•`ʔ~~ʕ´•ᴥ•`ʔ~~ʕ´•ᴥ•`ʔ~~ʕ´•ᴥ•`ʔ~~ʕ´•ᴥ•`ʔ~~ʕ´•ᴥ•`ʔ~~ʕ´•ᴥ•`ʔ~~ʕ´•ᴥ•`ʔ~~") 
       
def baja(niños):
    """
    Elimina la información del niño que se pasa como parámetro de un diccionario niños.txt.
    
    Argumentos:
        niño-- mediante el dni asignado a este niño del cual, quieres eliminar sus datos del diccionario.
        niños-- diccionario donde se encuentran almacenada la inforamción de todos los niños de la clínica.
        
    Valor de retorno:
        Elimina información del niño que pasas como parámetro si el dni es correcto.
        Si el dni no está en el diccionario , el dni es diferente a 8 o no es un dígito, salta  un error.
    """
    
    while True: 
        dni = input("Introduzca el dni del padre/madre o tutor legal del niño: ")
        if len(dni)!= 8 or not dni.isdigit():
            print("¯\_(ツ)_/¯Error. El dni no es valido¯\_(ツ)_/¯")
        else:
            break
    if dni not in niños:
        print("¯\_(ツ)_/¯No se puede encontar a ningun niño con este dni asignado¯\_(ツ)_/¯")
    else:
        del niños[dni]
        print("El niño seleccionado ya ha sido dado de baja")
    print("    ~~ʕ´•ᴥ•`ʔ~~ʕ´•ᴥ•`ʔ~~ʕ´•ᴥ•`ʔ~~ʕ´•ᴥ•`ʔ~~ʕ´•ᴥ•`ʔ~~ʕ´•ᴥ•`ʔ~~ʕ´•ᴥ•`ʔ~~ʕ´•ᴥ•`ʔ~~") 
    
def calculo(niños):
    """
    Devuelve un valor teórico del peso del bebe según su edad.
    
    Argumentos:
        niño-- mediante el dni asignado a este niño del cual, quieres conocer el valor del peso teórico según su edad.
        niños-- diccionario donde se encuentran almacenada la inforamción de todos los niños de la clínica.
        
    Valor de retorno:
        Si el dni es correcto, se calcula el peso del niño asociado al dni introducido por el usuario
        haciendo uso de la edad de este y unas operaciones matemáticas acordes a cada una.
        Si el dni no esta en el diccionario , el dni es diferente a 8 o no es un dígito, salta  un error.
    """
    
    print("Mediante esta opción puede calcular el peso teórico de su bebé desde los 3 meses ")
    print("Para ello se hace uso  de una serie de calculos matemáticos que en teoría se obtiene la media de peso de un niño para cada edad")
    while True: 
        dni = input("Introduzca el dni del padre/madre o tutor legal del niño: ")
        if len(dni)!= 8 or not dni.isdigit():
            print("¯\_(ツ)_/¯Error. El dni no es valido¯\_(ツ)_/¯")
        else:
            break
    calculototal = 0
    for dni in niños:
        niño = niños[dni] 
        if niño[1]>=3 and niño[1]<=12:
            f=niño[1]+9
            calculototal=f/2
        if niño[1]>12 and niño[1]<=24:
            f=niño[1]/2
            calculototal=f+5     
    print("Para el dni asignado el valor del peso teórico del niño es de",calculototal,"Kg") 
    print("    ~~ʕ´•ᴥ•`ʔ~~ʕ´•ᴥ•`ʔ~~ʕ´•ᴥ•`ʔ~~ʕ´•ᴥ•`ʔ~~ʕ´•ᴥ•`ʔ~~ʕ´•ᴥ•`ʔ~~ʕ´•ᴥ•`ʔ~~ʕ´•ᴥ•`ʔ~~")
    
def contar(niño,nivel):
    """
    Devuelve la cantidad de tipos de lactancia de todos los niños del diccionario niños.txt.
    
    Argumentos:
        niños-- diccionario donde se encuentran almacenada la inforamción de todos los niños de la clínica.
        nivel-- se usa como contador.
        
    Valor de retorno:
        Un contador con la cantidad total de lactancias separada por sus tipos.
    """
    pecho = niño[4]
    if pecho == "natural":
        nivel[0] += 1
    elif pecho == "artificial":
        nivel[1] += 1
    elif pecho == "neutra":
        nivel[2] += 1

def grafica_barras(niños):
    """
    Devuelve un gráfico de barras con todos los tipos de lactancia.
    
    Argumentos:
        niños-- diccionario donde se encuentran almacenada la inforamción de todos los niños de la clínica.
        nivel-- se usa como contador.
        
    Valor de retorno:
        Un gráfico de barras con el total de niños segmentado por los diferentes tipos de lactancias.
    """
    print("La clínica asiduamente hace estudios como este, que tratan la frecuencia")
    print("de la opción de lactancia de los padres a sus hijos.")
    nivel = [0, 0, 0]
    lactancia = ["natural", "artificial", "neutra"]
    for niño in niños:
        contar(niños[niño],nivel)
    
    print(nivel)
    posicion=range(len(nivel))
    plt.title("--Gráfico tipos de lactancias--")
    plt.bar(posicion,nivel)
    plt.xticks(posicion,lactancia)
    plt.yticks(nivel)
    plt.show()



# (apellidos, edad, sangre, sexo, pecho, pesos)
def cargar(niños):
    """
    Carga los nuevos datos añadidos de los nuevos bebes al diccionario niños.txt.
    
    """
    fich = open("niños.txt", "r")
    for linea in fich:
        datos, medidas = linea.rstrip().split("|")
        dni, nombre, edad, sangre, genero, pecho = datos.rstrip().split(",")
        lista_medidas = medidas.rstrip().split(",")
        lista_medidas = [float(x) for x in lista_medidas]
        edad = int(edad)
        niños[dni] = (nombre, edad, sangre, genero, pecho, lista_medidas)
    fich.close()

def principal():
    """
    Ejecuta todas las opciones del programa dependiendo de la opción que introduzca el usuario.
    
    Argumentos:
        Opción-- mediane la cual se elige que acción quiere realizar el usuario
    """
    niños = {}
    cargar(niños)
    while True:
        opcion = menuprincipal()
        if opcion == 1:
            añadir(niños)
        elif opcion == 2:
            buscar(niños)
        elif opcion == 3:
            imprimir(niños)
        elif opcion == 4:
            baja(niños)
        elif opcion == 5:
            calculo(niños)
        elif opcion == 6:
            grafica_barras(niños)
        elif opcion == 7:
            archivar(niños)
            print("Gracias por confiar en nosotros, sus datos han sido cargados.")
            break
principal()