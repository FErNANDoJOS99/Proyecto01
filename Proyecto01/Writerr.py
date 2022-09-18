import pickle
from io import open
colecion=None

class WriterrReader:

    

    def save(self , coleccion):
        fichero_binario=open("almacen","wb")
        pickle.dump(coleccion,fichero_binario)
        fichero_binario.close()
    
    def recover(self,nombreArchivo):
        try:
            ficheroApertura=open(nombreArchivo,"rb")
            dataRecover=pickle.load(ficheroApertura)
            ficheroApertura.close
            return dataRecover
        except:

            return None
      
    def existFile(self):
        try:
            archivo_texto=open("Introduce_tu_key.txt","r")
            texto=archivo_texto.read()
            archivo_texto.close()
            return True

        except:
            return False
    

    def makeFile(self):
        archivo_texto=open ("Introduce_tu_key.txt","w")
        archivo_texto.write("")
        archivo_texto.close()


    def readFile (self):
        archivo_texto=open("Introduce_tu_key.txt","r")
        texto=archivo_texto.read()
        archivo_texto.close()
        return texto
        


    ## creacion de archivo para la llave 
    ## Descargar la info en un archivo de texto 
    