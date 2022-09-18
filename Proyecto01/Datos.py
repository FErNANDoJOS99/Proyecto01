import pandas as pd   
pd._version  


class Datos:   

    def __init__(self,direction_file):
        self.conjunto =set()
        self.conjunto={""}
        self.datos={}
        self.__diccionario_ABC={}
        self.direction_file=direction_file
        self.read_csv(direction_file)
        self.origen=self.datos['origin'] 
        self.destine=self.datos['destination']
        self.origin_latitude=self.datos['origin_latitude']
        self.origin_longitude=self.datos['origin_longitude']
        self.destin_latitude=self.datos['destination_latitude']
        self.destin_longitude=self.datos['destination_longitude']
      
        self.generate_set(self.origen,self.destine)
        self.__aux__()
        
       



    def read_csv(self,nombreCSV):
        self.datos=pd.read_csv(nombreCSV,header=0)  ## header es igual al encabezado de la primer fila 
      
        
        
    '''
    list1 =origin
    list2 = destine 
    Genera un conjunto de IATA no repetidos 
    '''

    def generate_set(self,list1,list2):
        for i in range(0,len(list1)):
            self.conjunto.add(list1[i])
        for i in range(1,len(list2)-1):
            self.conjunto.add(list2[i])


    '''
    Busca las coordeanadas segun la IATA
    ABC Las claves IATA que estan en el conjunto 
    coleccion1 = La columna de  los lugares de IATA
    coleccion2 =la columna de latitudes
    coleccion3 =la columna de longitudes

    '''

    def search_coord(self,ABC,coleccion1,coleccion2,coleccion3):
        indice=0
        for i in coleccion1:
            
            if i==ABC:
                return   [coleccion2.iloc[indice],coleccion3[indice]]                         

            indice =indice+1 
        return []



## Hace un diccionario con claves IATA y por contenido un 
## string con latitud y longitud 

    def maker_dict(self,ABC,latitude,altitude,dict):
        dict[ABC]=[latitude,altitude]

    ## ayuda a crear el diccionario de IATA con sus longitudes 
    def __aux__ (self):
        for i in self.conjunto:
                coordenada=self.search_coord(i,self.origen,self.origin_latitude,self.origin_longitude)
                if coordenada==[]:
                    coordenada=self.search_coord(i,self.destine,self.destin_latitude,self.destin_longitude)
                if len(coordenada)==2:
                    self.maker_dict(i,coordenada[0],coordenada[1],self.__diccionario_ABC)


    '''
    Regresea solo las coordenadas de una IATA en especifico o 
    todo el diccionario IATA
    '''
    def getDictionary(self,IATA=""):
        if IATA =="":
            return self.__diccionario_ABC
        
        else:
            return self.__diccionario_ABC[IATA]
        

    