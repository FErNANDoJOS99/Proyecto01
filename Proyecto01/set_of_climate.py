from Coneccion_Api import Coneccion_Api
 
class set_of_climate(Coneccion_Api):
    __weather_dictionary={}   #diccionario de climas 
    def __init__(self,clave):
        super().__init__(clave)
      
 
    def search_climates(self,diccionario_ABC):
        """Crea el diccionario de climas \n
        Hace las llamadas con las direcciones se salen del IATA que estan en el diccionario_ABC
        y los valores de la solucitud los guarda en un diccionario llamado 
        __weather_dictionary"""
        contador=0

        for i in diccionario_ABC:
            print("\n",contador,"\n")
            self.__weather_dictionary[i]=self.request_Api_OpenW(diccionario_ABC[i][0],diccionario_ABC[i][1])
            contador=contador+1


  
    def drawing_Weather(self,dict1=__weather_dictionary,clave="0"):

        """Imprime el diccionario que recibe, de una forma bonita. \n
        Si no se pasa el diccionario , entonces imprime lo de solo un destino 
        pero por defecto busca un diccionario."""

        if clave!="0":
            info=dict1[clave] #se saca una IATA del diccionario de Climas 
        else:info=dict1
        nombre=info["nombre"]
        temperatura=info["temperatura" ]
        viento=info["viento"]
        latitude=info["latitude"] 
        longitude=info["longitud"]
        description=info[ "description"]   

        print("El nombre de la localidad  es ",nombre)
        print("temperature",temperatura)
        print("Velocidad del viento:",viento,"m/s")
        print("latitude:",latitude)
        print ("longitud:",longitude)
        print("description:",description)
        print("\n")
        
            

    def getWeathers(self):
        a=self.__weather_dictionary
        return a

    def setWeathers(self,newClima):
        self.__weather_dictionary=newClima

   
 
    def print_all(self,origin,destine):
        """Manda a llamar a drawing_Weather.\n 
        Ademas va haciendo la separacion entre vuelos 
        eh imprime el numero de vuelo que corresponde. """
       
        contador=0
        for i in range(0,len(destine)):
            contador=contador+1
            j=origin[i]
            k=destine[i]
            print ("\n\n###### ORIGEN ######")
            print("Clima  de  ",j,"  " )
            self.drawing_Weather(self.__weather_dictionary,j)
            print ("\n\n###### DESTINO ######")
            print("Clima  de ",k," ")
            self.drawing_Weather(self.__weather_dictionary,k)
            print("\n\n\n Registro ",i," #####################\n")
            if contador ==100:
                z= input("\n\nBusca el vuelo que necesites o \nDa un enter para continuar \n\n\n") 
                contador=0

    
