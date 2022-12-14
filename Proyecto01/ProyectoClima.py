from datetime import datetime
from Coneccion_Api import Coneccion_Api 
from Datos import Datos 
import time
from  Utilities import Utilities
from Comparado_tiempo import Comparador_tiempo
from set_of_climate import set_of_climate
try:
    datosCsv=Datos("dataset1.csv")  
except FileNotFoundError:
    print("No esta el archivo verifica que tiene el .csv ")
    exit()


coneccion=None
utility=Utilities()

def main ():

    tiempo=Comparador_tiempo(5)  # Establece la cantidad en minutos para la vigencia de los archivos 
    
    while True:  
        while True:  
            print("\n\nTienes 2 opciones\n ")
            print("**   Buscar una IATA en especifico    (1)")
            print("**   Ver los 3000 horarios de vuelo con origen y  destino     (2) ")
            i=input ("\nEscoge  1 o 2 \n")
            tiempo.set_current_time()
            if i=="1":
                    try:
                        print("Escribe la IATA que necesitas , abajo te apareceran algunas: \n\n")
                        IATAS=str(datosCsv.get_Dictionary().keys())
                        print(IATAS[9:])
                        iata =input ("\n")
                        if  utility.is_the_file("almacen")==False or tiempo.compare_time() == False:
                            print("Hizo la solicitud \n\n")
                            coordenadas1=datosCsv.get_Dictionary(iata)    
                            coneccion.drawing_Weather(coneccion.request_Api_OpenW(coordenadas1[0],coordenadas1[1]))
                            break
                        else: 
                            print("Saco del diccionario \n\n")
                            coneccion.drawing_Weather(utility.recover_collection("almacen"),iata)

                        break
                    except:
                        print ("\n\n Algo salio mal , verifica la IATA  o tu conexion a Internet \n\n ")
            elif i=="2":

                try :       #  si no se ha ejecutado el archivo ninguna vez o el tiempo de validez del archivo ya expiro entonces hacer la busqueda completa de nuevo
                        if  utility.is_the_file("almacen")==False or tiempo.compare_time() == False  :
                            print("La demora tarda aprox 37 seg\n\n ")
                            time.sleep(4)
                            coneccion.search_climates(datosCsv.get_Dictionary())                
                            utility.save_collection(coneccion.get_Weathers())                  #  guarda externamente el diccionario 
                            coneccion.print_all(datosCsv.origen,datosCsv.destine)
                            tiempo.set_past_time(datetime.now())  
                            break
                            

                        else:
                            time.sleep(4)
                            coneccion.set_Weathers(utility.recover_collection("almacen"))  # Actualiza el 
                            coneccion.print_all(datosCsv.origen,datosCsv.destine)
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



#  Esta seccion se encarga de verificar las precondiciones ,antes de entrar al metodo main.

if utility.exist_key():
    coneccion=set_of_climate(utility.get_key())
    if coneccion.check_Url():
        main()
    else:
        print ("\n\n\n Escribe una key correcta \n\n\n ")
else:
    print("Escribe una key en el archivo 'Introduce_tu_key'")
    utility.make_File_to_key()









