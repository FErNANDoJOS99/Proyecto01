Readme 

Antes de correr el programa debes de asegurarte en tener 
python instalado 
Tambien vas a requerir la libreria de pandas para el procesamiento 
de datos. 
      Para verificar si tienes pandas , en la terminal puedes escribir 
      python
      import pandas as pd 
      si no te aparece nada entonces si la tienes instalado 
      de lo contrario hay que instalarlo 
      para mas informacion sobre esto , puede visitar 
      https://www.ingeniusworlds.com/libreria-pandas-y-python/
      info adicional  para linux 
      sudo apt-get install python-pip   o   sudo apt-get install python3-pip  
      despues sudo pip install pandas   o   sudo pip3 install pandas 
      con los anteriores comandos se puede instalar el instalador de paquetes de 
      python y pandas 

Antes de poder ejecutar el programa vas a necesitar una clave que la vas a 
poder obtener en https://home.openweathermap.org/
Despues de obtener tu clave debes de escribirla en el archivo de texto 
que se llama "Introduce_tu_key.txt"  sin dejar espacio al principio de la clave y 
en la primer fila. 
      Nota: Si no te aparece este archivo , trata de ejecutar el archivo 
            principal que es ProyectoClima.py 
            y en ese momento aparecera el archivo 
            "Introduce_tu_key"

Correr el programa:
	Poner en la terminal (python ProyectoClima.py)



Ya dentro del programa te dara 2 opciones 
   - Ver la informacion de una IATA en especifico  o mostrarte las 3000 opciones 
      en caso de escoger la segunda opcion tardara aproximadamente 37 segundos en obtenerlas 
      todas

    -Una vez que se ejecute el caso 2 se creara el archivo "almacen" que contendra un 
        diccionario con todos los pronosticos del clima ,este tiene una vigencia 
        de 5 minutos . por lo tanto si se requiere la informacion de nuevo , se podra tener 
        acceso inmediato si se hace dentro del rango , si se demora mas tiempo entonces el sistema volvera a 
        llamar  a la Api de Openweather , esto se realiza para mantener la información Actualizada 

Hay un apartado que dice tiempo vigencia eso es el tiempo  que todavia se tiene  para hacer una solicitud del clima 
y que salgan de inmediato 



Pruebas unitarias : Son tres y se encuentran en test.py 
para utilizarlas es necesario que se tenga internet para que 
se conecte a la Api y en la terminal escribir "python -m unittest"
con eso correra las pruebas 



Versión 1.1.0
Informacion de contacto : licfernandoc@ciencias.unam.mx
WhatsApp : 5582307606




