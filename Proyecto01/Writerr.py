import pickle
from io import open
colecion=None

class WriterrReader:

    

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
        
