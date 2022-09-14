from importlib import import_module
from re import S
import requests
import time 
import pandas as pd   ## pd es el objeto sque se creo con pandas
pd._version  
#import numpy as np
from functools import lru_cache

class Coneccion_Api:

    clave=""
    diccionario_Weathers={}

    def __init__(self,clave="d1611b9fdfa424b8749ea02becc6d1c8"):
        self.clave=clave
        


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
        diccionario_Weathers

        '''

    def seacher_Weather(self,diccionario_ABC):
            contador=0

            for i in diccionario_ABC:
                print("\n",contador,"\n")
                self.diccionario_Weathers[i]=self.request_Api_OpenW(diccionario_ABC[i][0],diccionario_ABC[i][1])
                contador=contador+1



        
        

        ## Es para imprimir el diccionario de una forma bonita 
        #si no se pasa el diccionario , entonces imprime lo de solo un distino 
        #pero por defecto busca un diccionario
    def drawing_Coordenada(self,dict1=diccionario_Weathers,clave="0"):
            if clave!="0":
                info=dict1[clave]
            else:info=dict1
            nombre=info["nombre"]
            temperatura=info["temperatura" ]
            viento=info["viento"]
            latitude=info["latitude"] 
            longitude=info["longitud"]
            description=info[ "description"]   

            print("El nombre de la ciudad es ",nombre)
            print("temperature",temperatura)
            print("Velocidad del viento:",viento,"m/s")
            print("latitude:",latitude)
            print ("longitud:",longitude)
            print("description:",description)
            print("\n")
            
            







    def put_out_everything(self,origin,destine):
        
        
        for i in range(0,len(destine)):
            j=origin[i]
            k=destine[i]
            print("Clima  de origen  ",j,"  " )
            self.drawing_Coordenada(self.diccionario_Weathers,j)
            print("\nClima  de destino ",k," ")
            self.drawing_Coordenada(self.diccionario_Weathers,k)
            print("\n\n\n Registro ",i," #####################\n")
