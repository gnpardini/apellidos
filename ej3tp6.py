"""GrabarRangoAlturas() Graba en un archivo las alturas de los atletas de distintas
disciplinas, los que se ingresan desde el teclado. Cada dato se debe grabar en una
línea distinta. Ejemplo:
<Deporte 1>
<altura del atleta
<altura del atleta
< . . . >
<Deporte 2>
<altura del atleta"""


class ErrorNumerosNegativos(Exception):
    
    pass

class ErrorDeCaracteres(Exception):
    
    pass

class ErrorCaracteresAlfabeticos(Exception):
    
    pass


def crearArchivo():
    
    archivo = open("rangoAlturas.txt","w")
    
    return archivo
    

            
        
def pedirDeporteYAltura(archivo):
    
        
    alturaStr = 0
    
    while True:
        
        try:
            deporte = input("Ingrese un deporte")
            
            if deporte == "":
                
                
                break
    
            
            elif deporte.isdigit() == True:
                
                raise ErrorDeCaracteres
            
            elif deporte != "":
                
                archivo.write(deporte + "\n")
                
            
            while True:
            
                try:
                    altura = input("Ingrese una altura")
                            
                    if altura == "":
                                
                        break
                            
                    elif altura.isalpha() == True:
                                    
                        raise ErrorCaracteresAlfabeticos
                                
                    else:
                                    
                        alturaFloat = float(altura)
                                    
                        if alturaFloat <= 0:
                            
                            raise ErrorNumerosNegativos
                                    
                        else:
                            
                            if alturaFloat > 0:
                
                
                                alturaStr = str(alturaFloat) + "\n"
                                archivo.write(alturaStr)
                                
                except(ErrorCaracteresAlfabeticos):
                        
                    print("Solo se permite el ingreso de números")
                        
        except(ErrorCaracteresAlfabeticos):
            
            print("Solo se permite el ingreso de números")
            
        except (ErrorNumerosNegativos):
            
            print("No se permite el ingreso menores o igual a 0")
            
    return deporte,alturaStr
             
                    
def grabarAlturas(archivo):
    
    try:
    
       archivo = crearArchivo()
       deporte,alturaFloat = pedirDeporteYAltura(archivo)
                
       
       
    except(IOError):
        
        print("No se pudo abrir el archivo")
    
    
    finally:
            
        archivo.close()
        

def leerYCrearArchivos():

    archivoAlturas = open("rangolAturas.txt","r")
    
    archivoPromediosAlturas = open("promediosAlturas.txt","w")
        
  
        
    return archivoAlturas,archivoPromediosAlturas
        

    
    
    
    
def grabarPromedio():
    
    contador = 0
    
    while True:
    
        try:
        
          archivoAlturas,archivoPromediosAlturas = leerYCrearArchivos()
      
          for registro in archivoAlturas:
          
              if registro.isdigit == True():
                  
                  contador = contador + 1
              
                  altura = float(registro)
                  suma = altura + suma
                  
                  if registro.isalpha() == True:
                      
                      break
                    
        
              
              
              
            
          
          
        except(IOError):
        
            print("No se puede leer/escribir el archivo")
        
    
        
                
                
        
            
        
        
        
        
    
    
    
    
 
                
                
                
        
        
    
        
        
        
        
        
        
        
        
            
            











#Main


archivoAlturas = crearArchivo()
grabarAlturas(archivoAlturas)

grabarPromedio()

