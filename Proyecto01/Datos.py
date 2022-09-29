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
        """Lee el csv y eso lo guarda en el diccionario (datos)"""
        self.datos=pd.read_csv(nombreCSV,header=0)  ## header es igual al encabezado de la primer fila 
      
        
        
    '''
    list1 =origin
    list2 = destine 
    Genera un conjunto de IATA no repetidos 
    '''

    def generate_set(self,list1,list2):
        """Genera un conjunto de con elementos no repetidos \n"""
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
        """Busca los argumentos de dos diccionarios segun una clave.\n
        return los argumentos , si no los encuentra retorna diccionario vacio """
        indice=0
        for i in coleccion1:
            
            if i==ABC:
                return   [coleccion2.iloc[indice],coleccion3[indice]]                         

            indice =indice+1 
        return []



    def make_dict(self,ABC,latitude,altitude,dict):
        """Hace un diccionario con claves ABC y por contenido un 
        string con latitud y longitud """
        dict[ABC]=[latitude,altitude]

    ## ayuda a crear el diccionario de IATA con sus longitudes 
    def __aux__ (self):
        for i in self.conjunto:
                coordenada=self.search_coord(i,self.origen,self.origin_latitude,self.origin_longitude)
                if coordenada==[]:
                    coordenada=self.search_coord(i,self.destine,self.destin_latitude,self.destin_longitude)
                if len(coordenada)==2:
                    self.make_dict(i,coordenada[0],coordenada[1],self.__diccionario_ABC)


 


  
    def getDictionary(self,IATA=""):
        """Retun el diccionario_ABC o solo un argumento de el, eso depende
        si se le pone parametros al metodo """
        if IATA =="":
            return self.__diccionario_ABC
        
        else:
            return self.__diccionario_ABC[IATA]
        

    