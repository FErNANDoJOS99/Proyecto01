from datetime import datetime, timedelta
from io import open

class  Comparador_tiempo():


    tiempoActual=None
    tiempoPasado=None
    tiempoLimite=None


    def __init__(self,intervalo):
        self.intervaloMinutes=intervalo
    



    def set_current_time(self):
        self.tiempoActual=datetime.now()



    def get_past_time(self ):
        return self.tiempoPasado

    def set_past_time (self,tiempo):
        self.tiempoPasado=tiempo
        self.make_file_last_update()


    def get_limit(self):
        """Retorna el tiempo limite """
        return self.tiempoLimite

    
    def compare_time (self):
        """Compara el tiempo actual con el tiempo limite \n
        Si el tiempo limite es mayor entonces retorna True si no entonces
        retorna False"""
        minutoDelta =timedelta(minutes=self.intervaloMinutes)
        try:
            tiempoPasado=self.read_file_last_update()
            self.tiempoPasado=self.turn_to_date(tiempoPasado)
            tiempo_limite =self.tiempoPasado+minutoDelta
            tiempo_limite=self.turn_to_date(self.turn_to_string(tiempo_limite))   #para cambiarle el formato al tiempo
            
            print("tiempo vigente=  ",tiempo_limite  )
            print("tiempo actual =  ",self.turn_to_date(self.turn_to_string(self.tiempoActual)),"\n\n\n")
           
            

            if tiempo_limite>self.tiempoActual:
                return True
            else: return False

        except:
            return True 

        
    def turn_to_string (self,hora):  
        """Cambia una hora(Datetime) a un String""" 
        fechaTexto=datetime.strftime(hora,'%d/%m/%Y %H:%M:%S')
        return fechaTexto

    def turn_to_date(self,fecha_Texto):
        """ Cambia un string a un dato tipo DateTime"""
        fechaFecha =datetime.strptime(fecha_Texto,'%d/%m/%Y %H:%M:%S')
        return fechaFecha




    def make_file_last_update(self):
        """Crea el archivo UltimateUpdateData.txt \n
           Su contenido sera una fecha y hora """
        archivo_texto=open ("UltimateUpdateData.txt","w")
        archivo_texto.write(self.turn_to_string(self.tiempoPasado))
        archivo_texto.close()


    def read_file_last_update (self):
        """Lee el archivo UltimateUpdateData.txt\n
        return un string con la fecha """

        archivo_texto=open("UltimateUpdateData.txt","r")
        texto=archivo_texto.read()
        archivo_texto.close()
        return texto
        















