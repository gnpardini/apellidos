"""Escribir un programa que lea un archivo de texto conteniendo un conjunto de
apellidos y nombres en formato "Apellido, Nombre" y guarde en el archivo
ARMENIA.TXT los nombres de aquellas personas cuyo apellido terminan con la
cadena "IAN", en el archivo ITALIA.TXT los terminados en "INI" y en el archivo
ESPAÑA.TXT los terminados en "EZ". Descartar el resto. Ejemplo:
Arslanian, Gustavo
Rossini, Giuseppe
Pérez, Juan
Smith, John
–>
–>
–>
–>
ARMENIA.TXT
ITALIA.TXT
ESPAÑA.TXT
descartar
El archivo de entrada puede ser creado mediante el Block de Notas o el IDLE. No
escribir un programa para generarlo."""


#Funciones


def leerArchivo():
    
    archivoNombres = open("nombres.txt","r")
    
    return archivoNombres

def abrirArchivo(nombre):

    archivo = open(nombre,"w")

    return archivo

def obtenerUltimosCaracteres(apellido,cantidad):
    
    primerCaracterBuscado = len(apellido)   - cantidad
    
    subcadena = apellido[primerCaracterBuscado : len(apellido)]
    
    
    
    return subcadena
        
    
    
        
        
    
def guardarNombreArmenio(nombres,archivoArmenia,caracteresBuscados,apellido):
    
    
    
    subcadena = obtenerUltimosCaracteres(apellido,3)
    
    for registro in nombres:
        
        if subcadena == "ian":
        
            archivoArmenia.write(nombres[0] + "," +  nombres[1] + "\n")
            
            
def guardarNombreItaliano(nombres,archivoItalia,caracteresBuscados,apellido):
    
    
    
    subcadena = obtenerUltimosCaracteres(apellido,3)
    
    if subcadena == "ini":
        
        archivoItalia.write(nombres[0] + "," + nombres[1] + "\n")
        
        
def guardarNombreEspañol(nombres,archivoEspaña,caracteresBuscados,apellido):
    
    subcadena = obtenerUltimosCaracteres(apellido,2)
        
    if subcadena == "ez":
            
        archivoEspaña.write(nombres[0] + "," + nombres[1] + "\n")
    
    


def guardarNombresPorTerminacion():
    
    try:
        
        archivoNombres = leerArchivo()
        archivoArmenia = abrirArchivo("ARMENIA.TXT")
        archivoItalia = abrirArchivo("ITALIA.TXT")
        archivoEspaña = abrirArchivo("ESPAÑA.TXT")
       
    except(IOError):
        
        print("No se puede leer/escribir el archivo. Revise el nombre del archivo")
        
        
    else:
        
        ultimosCaracteres = 0
        
        for registro in archivoNombres :
            
            registro = registro.strip()
            nombres = registro.split(",")
            apellido = nombres[0]
        
           
    
            caracteresBuscados = obtenerUltimosCaracteres(apellido,3)
            guardarNombreArmenio(nombres,archivoArmenia,caracteresBuscados,apellido)
            guardarNombreItaliano(nombres,archivoItalia,caracteresBuscados,apellido)
            caracteresBuscados = obtenerUltimosCaracteres(apellido,2)
            guardarNombreEspañol(nombres,archivoEspaña,caracteresBuscados,apellido)
            
            
           
            
            
        
    finally:
        
        archivoNombres.close()
        archivoArmenia.close()
        archivoEspaña.close()
        archivoItalia.close()
        
                
                
       
        
            
            
           
            
                
            
        
            
        
        
        
        
        
#Programa principal

guardarNombresPorTerminacion()
