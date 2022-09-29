import pickle
from io import open
colecion=None

class WriterrReader:

    clave=""
    def __init__(self):
        self.clave=""

    def save(self , coleccion):
        """Guarda una coleccion en un fichero llamado , almacen"""
        fichero_binario=open("almacen","wb")
        pickle.dump(coleccion,fichero_binario)
        fichero_binario.close()
    
    def recover(self,nombreArchivo):
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
      
    def existFile(self):
        """Verifica que exista el archivo ,Introduce_tu_key \n
        return True si lo encuentra"""
        try:
            archivo_texto=open("Introduce_tu_key.txt","r")
            texto=archivo_texto.read()
            archivo_texto.close()
            return True

        except:
            return False
    

    def makeFile(self):
        """Crea un archivo vacio llamado Introduce_tu_key.txt"""
        archivo_texto=open ("Introduce_tu_key.txt","w")
        archivo_texto.write("")
        archivo_texto.close()


    def readFile (self):
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
        if(self.existFile()):
            clave1=self.readFile()
            claveLimpia=clave1.strip()
            self.clave=claveLimpia
            
            return True
        else:
            return False

    def get_key(self):
        return self.clave