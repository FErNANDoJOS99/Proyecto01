from datetime import datetime
from Coneccion_Api import Coneccion_Api 
from Datos import Datos 
import time
from  Writerr import WriterrReader
from Comparado_tiempo import Comparador_tiempo

try:
    datosCsv=Datos("dataset1.csv")  
except FileNotFoundError:
    print("No esta el archivo verifica que tiene el .csv ")
    exit()

coneccion=None
writer=WriterrReader()
tiempo=Comparador_tiempo(5)
contador=0

if writer.existFile()==True:
   
    clave=""
    clave=writer.readFile()
    claveLimpia=clave.strip()
    coneccion=Coneccion_Api(claveLimpia) 

    if coneccion.check_Url()==True:
    
        while True:  
            while True:  
                print("\n\nTienes 2 opciones\n ")
                print("**   Buscar una IATA en especifico    (1)")
                print("**   Ver los 3000 horarios de vuelo con origen y  destino     (2) ")
                i=input ("\nEscoge  1 o 2 \n")
                tiempo.set_timeCurrent()
                if i=="1":
                        try:
                            iata =input ("Escribe la IATA   ..........por ejemplo:  MEX , TLC , MTY  \n")
                            print("\n\n") 
                            if  writer.recover("almacen")==None or tiempo.compareTime() == False:
                                print("Hizo la solicitud \n\n")
                                coordenadas1=datosCsv.getDictionary(iata)    
                                coneccion.drawing_Coordenada(coneccion.request_Api_OpenW(coordenadas1[0],coordenadas1[1]))
                                break
                            else: 
                                print("Saco del diccionario \n\n")
                                coneccion.drawing_Coordenada(writer.recover("almacen"),iata)

                            break
                        except:
                            print ("\n\n Algo salio mal , verifica la IATA  o tu conexion a Internet \n\n ")
                elif i=="2":

                    try :
                            if  writer.recover("almacen")==None or tiempo.compareTime() == False  : # si no se ha ejecutado el archivo ninguna vez 
                                                                                                    #o el tiempo de validez del archivo ya expiro entonces 
                                                                                                    # hacer la busqueda completa de nuevo
                                print("La demora tarda aprox 45 seg\n\n ")
                                time.sleep(4)
                                coneccion.seacher_Weather(datosCsv.getDictionary())
                                writer.save(coneccion.getWeathers())                  ## guarda externamente el diccionario 
                                coneccion.put_out_everything2(datosCsv.origen,datosCsv.destine)
                                tiempo.set_timePast(datetime.now())  
                                break
                                

                            else:
                                time.sleep(4)
                                coneccion.setWeathers(writer.recover("almacen"))
                                coneccion.put_out_everything2(datosCsv.origen,datosCsv.destine)
                                break
                    except:
                        print("Algo salio mal verifica tu internet ")

                            
            
                        
                else:print("No escogiste un valor correcto ")

            print("\n\nRegresar al menu principal (1)\nQuieres salir(2)")
            i=input ("Escoge  1 o 2 \n\n\n")
            print("\n\n\n")

            if i=="2":   
                break
            elif i!="1":
                break
   
            
else:
    print ("\n\n\n Escribe una key correcta en el archivo  'Introduce_tu_key'\n\n\n ")
    writer.makeFile()


  
        













