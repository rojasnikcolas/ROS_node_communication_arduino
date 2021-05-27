# CONEXIÓN ROS - ARDUINO(Arduino como Nodo) PARCIAL1

## INTRODUCCIÓN


Este paquete contiene nodos ROS desde la A hasta la H, que publican y suscriben diferentes tipos de variables (Bool, Int16, FLoat32, Char y String) para, posteriormente, comunicarse con arduino, el cual está usado como un nodo y simular una implementación real de un caso en particular.

## SCRIPTS

- Nodo A: Se suscribe a un "topic" proveniente del nodo de arduino y recibe una variable de tipo Char, posteriormente separa los valores y publica 3 lineas de "topics" enviando las variables separadas de tipo Bool, Int y Float.  
- Nodo B: Se suscribe al "topic" que envía A y recibe los valores Bool. Publica un topic donde se envía una variable de tipo String que dice el valor que representa High y Low.
- Nodo C: Se suscribe al "topic" que envía A y recibe los valores Int. Publica un topic donde se envía una variable de tipo String que dice el valor que representa High, medium y Low del valor recibido según logica difusa.
- Nodo D: Se suscribe al "topic" que envía A y recibe los valores Float. Publica un topic donde se envía una variable de tipo String que dice el valor que representa High, medium y Low del valor recibido según logica difusa.
- Nodo E: Se suscribe al "topic" que envía B y recibe los valores del String. Publica un Char que es elegido mediante unos condicionales en cascada seleccionando el valor mas representativo.
- Nodo F: Se suscribe al "topic" que envía B y recibe los valores del String. Publica un Char que es elegido mediante unos condicionales en cascada seleccionando el valor mas representativo.
- Nodo G: Se suscribe al "topic" que envía C y recibe los valores del String. Publica un Char que es elegido mediante unos condicionales en cascada seleccionando el valor mas representativo.
- Nodo H: Se suscribe a un topic y recibe una variable Char de los nodos E, F y G y Publica un topic para enviar 
- Nodo arduino: Se suscribe a un topic String desde el Nodo H, utiliza su valor para establecer la velocidad del motor, también toma el valor de 3 sensores y publica un String con el valor de los sensores. Publica el resultado al Nodo A


## EJECUTAR ARDUINO COMO NODO


- Necesario dar permisos al puerto de conexión del arduino
- 
> $ sudo chmod 777 /dev/ttyUSB0 (Puede ser que en vez de "ttyUSB0" sea "ttyACM0")

- Cargar el codigo en el arduino y correr el puerto serial:

> $ rosrun rosserial_python serial_node.py /dev/ttyUSB0 


# AUTORES

- Mauricio Gómez Menjura
- Eymer S. Tapias
- Nikcolas Rojas
