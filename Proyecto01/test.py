from logging import exception
import unittest
from Datos import Datos
from Comparado_tiempo import Comparador_tiempo
from Coneccion_Api import Coneccion_Api
from Writerr import WriterrReader

class TestMethodes(unittest.TestCase):


    #Verifica que mande una exception 
    #Se le pasa un numbre incorrecto de archivo 
    # para que verifique  que no esta el archivo y mande error 
    def test_verificar_BaseDatos(self):
           
            with self.assertRaises(FileNotFoundError): 
                   datos=Datos("dataset2.csv")  
              
    

    #Verifica que la Api si regrese un diccionario 
    def test_verificar_Json(self):

            writer=WriterrReader()
            clave=None

            if writer.existFile()==True:
    
                clave=writer.readFile()
                claveLimpia=clave.strip()
                
                coneccion=Coneccion_Api(claveLimpia) 

            coneccion=Coneccion_Api(claveLimpia)
            json1=coneccion.request_Api_OpenW("19.3371","-99.566")
            self.assertIsInstance(json1, dict)
           


    #Verifica si se encuestra las IATA en el diccionario que se quedo 
    # Guardado en el archivo "almacen "
    #         
    def test_diccionarioClimas (self):
        writerr=WriterrReader()
        diccionarioClimas=writerr.recover("almacen")
      
        self.assertIn("TLC",diccionarioClimas)
        self.assertIn("MEX",diccionarioClimas)
        
        self.assertIn("MTY",diccionarioClimas)

        self.assertIn("TAM",diccionarioClimas)





if __name__ =="main":
    unittest.main()
