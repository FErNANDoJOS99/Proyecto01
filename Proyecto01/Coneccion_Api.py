#from importlib import import_module
#from importlib.metadata import requires
#from webbrowser import get
import requests
#import time 
import pandas as pd   ## pd es el objeto sque se creo con pandas
pd._version  
#import numpy as np
#from functools import lru_cache
#from Writerr import WriterrReader

class Coneccion_Api:
    __diccionario_Weathers={}
    def __init__(self,clave):
        self.clave=clave      
        self.__diccionario_Weathers={}


    def check_Url(self):

        try:
            url ="https://api.openweathermap.org/data/2.5/weather?lat=19.3371&lon=-99.566&appid={}".format(self.clave)
            res=requests.get(url)        
            if res.status_code==401:     #401 falla por credenciales 
                                         #400 falla por un mal dato en la peticion (como malas coordenadas)
                print("Ingresa una Key correcta ")
                return False
            else:
                return True
        except:
            print("\n\nAlgo salio mal verifica tu internet \n")
            return False
        

    

        


    def request_Api_OpenW(self,lati1,longi1):
        diccionario_temp={}
        url="https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}".format(lati1,longi1,self.clave)
        res =requests.get (url)   #le habla a la API  para que la analizen 
        data =res.json()  #con este comando se hace que la informacion que mando la API este mejor estructurada y asi manipulas mejor 
        temp=data ["main"]["temp"]  # se pone asi porque temp esta dentro del diccionario main 
        wind_speed =data["wind"]["speed"]
        
        latitude =data ["coord"]["lat"]
        longitude =data ["coord"] ["lon"]
        description =data ["weather"][0]["description"]  # Description es una lista por eso se ponde desde cero 
        name=data ["name"]
        
        print("Espere ,cargando informacion")
        '''
        print("nombre de la ciudad ",name)
        print("temperature",temp)
        print("Velocidad del viento:",wind_speed,"m/s")
        print("latitude:",latitude)
        print ("longitud:",longitude)
        print("description:",description)

        
        '''

        diccionario_temp={"nombre":name,"temperatura":temp,"viento":wind_speed,"latitude":latitude,"longitud":longitude,"description":description}
        return diccionario_temp







        '''

        Hace las llamadas con las direcciones se salen del IATA que estan en el diccionario_ABC
        y los valores de la solucitud los guarda en un diccionario llamado 
        __diccionario_Weathers

        '''

    def seacher_Weather(self,diccionario_ABC):
            contador=0

            for i in diccionario_ABC:
                print("\n",contador,"\n")
                self.__diccionario_Weathers[i]=self.request_Api_OpenW(diccionario_ABC[i][0],diccionario_ABC[i][1])
                contador=contador+1



        
        

        ## Es para imprimir el diccionario de una forma bonita 
        #si no se pasa el diccionario , entonces imprime lo de solo un distino 
        #pero por defecto busca un diccionario
    def drawing_Coordenada(self,dict1=__diccionario_Weathers,clave="0"):
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
        a=self.__diccionario_Weathers
        return a

    def setWeathers(self,newClima):
        self.__diccionario_Weathers=newClima


    '''
    Recibe 2 cadenas , origen y destino 
    y ocupa el for para irlas recorriendo ya que estas contienen las claves 
   que usaremos en el diccionario y estos valores son los que vamos a 
   imprimir bonito 
    
    '''
        
    

    def put_out_everything2(self,origin,destine):
        
       
        contador=0
        for i in range(0,len(destine)):
            contador=contador+1
            j=origin[i]
            k=destine[i]
            print ("\n\n###### ORIGEN ######")
            print("Clima  de  ",j,"  " )
            self.drawing_Coordenada(self.__diccionario_Weathers,j)
            print ("\n\n###### DESTINO ######")
            print("Clima  de ",k," ")
            self.drawing_Coordenada(self.__diccionario_Weathers,k)
            print("\n\n\n Registro ",i," #####################\n")
            if contador ==100:
                z= input("\n\nBusca el vuelo que necesites o \nDa un enter para continuar \n\n\n") 
                contador=0

    


