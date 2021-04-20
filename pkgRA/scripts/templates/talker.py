#!/usr/bin/env python

#Asegura que todo el Script se ejecute como Python (NO MODIFICAR!!)

#------LIBRERIAS-----------

import rospy
#Necesario siempre que se escriban nodos en ROS
from std_msgs.msg import String
#Importar "String" de std_msgs /permite reutilizar el contenedor string para publicar mensajes/

#------Define la Clase (Atributos y Metodos)-----
def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10) 	
    #El nodo talker publica en el topic "chatter" un String 
    rospy.init_node('talker', anonymous=True)
    #Nombra (launch) el nodo como "talker", siendo este nombre unico (anonymous=true) (IMPORTANTE)  
    rate = rospy.Rate(10) 
    #Frecuencia del bucle (Tiempo de muestreo) 10veces*s 10hz
    #------------Work------------
    while not rospy.is_shutdown():
    #bucle "mientras no" verifx|ica el indicador rospy.is_shutdown()	
        hello_str = "hello world %s" % rospy.get_time()
	#Crea la variable "hello_str" y le asigna esos caracteres
        rospy.loginfo(hello_str)
	#Imprime en el terminal la variable
        pub.publish(hello_str)
	#Asigna la variable creada anteriormente al topic y lo publica
        rate.sleep()
	#Detiene el bucle hasta cumplir la frecuencia (rate)

#--------MAIN-----------
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
