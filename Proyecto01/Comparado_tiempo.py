from datetime import datetime, timedelta
from io import open

class  Comparador_tiempo():


    tiempoActual=None
    tiempoPasado=None
    tiempoLimite=None


    def __init__(self,intervalo):
        self.intervaloMinutes=intervalo
    



    def set_timeCurrent(self):
        self.tiempoActual=datetime.now()



    def get_timePast(self ):
        return self.tiempoPasado

    def set_timePast (self,tiempo):
        self.tiempoPasado=tiempo
        self.makefile()

    def get_limit(self):
        return self.tiempoLimite

    def compareTime (self):
        minutoDelta =timedelta(minutes=self.intervaloMinutes)
        try:
            tiempoPasado=self.readfile()
            self.tiempoPasado=self.turnToDate(tiempoPasado)
            tiempo_limite =self.tiempoPasado+minutoDelta
            tiempo_limite=self.turnToDate(self.turnToString(tiempo_limite))   #para cambiarle el formato al tiempo
            
            print("tiempo vigente=  ",tiempo_limite  )
            print("tiempo actual =  ",self.turnToDate(self.turnToString(self.tiempoActual)),"\n\n\n")
           
            

            if tiempo_limite>self.tiempoActual:
                return True
            else: return False

        except:
            return True 

        
    def turnToString (self,hora):   
        fechaTexto=datetime.strftime(hora,'%d/%m/%Y %H:%M:%S')
        return fechaTexto

    def turnToDate(self,fecha_Texto):
        fechaFecha =datetime.strptime(fecha_Texto,'%d/%m/%Y %H:%M:%S')
        return fechaFecha




    def makefile(self):
        archivo_texto=open ("UltimateUpdateData.txt","w")
        archivo_texto.write(self.turnToString(self.tiempoPasado))
        archivo_texto.close()


    def readfile (self):
        archivo_texto=open("UltimateUpdateData.txt","r")
        texto=archivo_texto.read()
        archivo_texto.close()
        return texto
        















