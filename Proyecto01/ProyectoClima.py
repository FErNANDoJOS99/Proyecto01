from Coneccion_Api import Coneccion_Api 
from Datos import Datos 
          
datosCsv=Datos("dataset1.csv")  
coneccion=Coneccion_Api()  

contador=0
while True:    
    print("Tienes 2 opciones ")
    print("Buscar una IATA en especifico    (1)")
    print("Ver todo los horarios de vuelo con su destino     (2) ")
    i=input ("Escoge  1 o 2 \n")
    if "2"<i<"1":
        print("No escogiste opcion correcta ")
    else:
        if i=="1":
            iata =input ("Escribe la IATA\n") 
            coordenadas1=datosCsv.diccionario_ABC[iata]   
            print(coordenadas1)
            coneccion.drawing_Coordenada(coneccion.request_Api_OpenW(coordenadas1[0],coordenadas1[1]))
        
        if i=="2":
            if contador==0:
                coneccion.seacher_Weather(datosCsv.diccionario_ABC)
                contador=2
            coneccion.put_out_everything(datosCsv.origen,datosCsv.destine)
    print("Quieres mas informacion (1)\nQuieres salir(2)")
    i=input ("Escoge  1 o 2 \n")
    print("\n\n\n")
    if "2"<i<"1":
        ("No escogiste opcion correcta , adios")
        break
    else:
        if i=="2":
            break 















