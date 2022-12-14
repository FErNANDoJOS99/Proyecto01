import pickle
from io import open
colecion=None

class Utilities:
    """ Utilities es un conjunto de metodos que ayuda a administrar 2 tipos de informacion , creacion y lectura de archivos.txt  asi como tambien 
    Archivos donde se guarda informacion binaria que contendra colecciones. """
    clave=""
    def __init__(self):
        self.clave=""

    def save_collection(self , coleccion):
        """Guarda una coleccion en un fichero llamado , almacen"""
        fichero_binario=open("almacen","wb")
        pickle.dump(coleccion,fichero_binario)
        fichero_binario.close()
    
    def recover_collection(self,nombreArchivo):
        """Obtiene la coleccion que se encuentra con el atributo nombre\n
        return la coleccion si esta el archivo,
        return None si no la encuentra"""
        try:
            ficheroApertura=open(nombreArchivo,"rb")
            dataRecover=pickle.load(ficheroApertura)
            ficheroApertura.close
           
            return dataRecover
        except:

            return None
      

    def is_the_file(self,nombreArchivo):
        """Verifa que se encuentre el archivo , binario, pasado como argumento 
        si lo esta return True , si no return False"""
        try:
            ficheroApertura=open(nombreArchivo,"rb")
            ficheroApertura.close
            return True
        except:

            return False
        
    ######
      
    def __exist_File(self):
        """Verifica que exista el archivo ,Introduce_tu_key \n
        return True si lo encuentra"""
        try:
            archivo_texto=open("Introduce_tu_key.txt","r")
            texto=archivo_texto.read()
            archivo_texto.close()
            return True

        except:
            return False
       
    

    def make_File_to_key(self):
        """Crea un archivo vacio llamado Introduce_tu_key.txt"""
        archivo_texto=open ("Introduce_tu_key.txt","w")
        archivo_texto.write("")
        archivo_texto.close()


    def read_file_key (self):
        """
        Va a leer el archivo llamado "Introduce_tu_key.txt\n
        return el contenido del archivo 
        """
        archivo_texto=open("Introduce_tu_key.txt","r")
        texto=archivo_texto.read()
        archivo_texto.close()
        return texto
        
    def exist_key(self):
        """
        Verifica si existe la clave para entrar al progrma 
        y si existe ,guarda la clave dentro de sus parametros
        """
        if(self.__exist_File()):
            clave1=self.read_file_key()
            claveLimpia=clave1.strip()
            self.clave=claveLimpia
            
            return True
        else:
            return False

    def get_key(self):
        return self.clave