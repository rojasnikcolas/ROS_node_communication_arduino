#!/usr/bin/env python

#Asegura que todo el Script se ejecute como Python (NO MODIFICAR!!)

#------LIBRERIAS-----------

import rospy
#Necesario siempre que se escriban nodos en ROS
from std_msgs.msg import Int16
from std_msgs.msg import Bool
from std_msgs.msg import Float32
#Importar "int/bool/float" de std_msgs /permite reutilizar el contenedor string para publicar mensajes/

#------Define la Clase (Atributos y Metodos)-----

def Ttalker():
	#--------Topics "Caminos de datos"
	pubB = rospy.Publisher('bool', Bool, queue_size=10)
	#Crea un camino de salida(nombre del topic, Tipo de variable, Memoria recibido) 
	pubI = rospy.Publisher('int', Int16, queue_size=10)
	pubF = rospy.Publisher('float', Float32, queue_size=10)

	#---------Nodo y Caracteristicas	
	rospy.init_node('Ttalker', anonymous=False)
	#Crea el nodo(nombre, unificacion"unico")
	rate = rospy.Rate(10)
	#Frecuancia propia del nodo
	
	#---------Variables a enviar
	d_bool=False
	d_int=5
	d_float=2.5
	#Muestra en el nodo A lo que va a enviar
	rospy.loginfo(d_bool)
	rospy.loginfo(d_int)
	rospy.loginfo(d_float)

	#---------Proceso en bucle
	while not rospy.is_shutdown():
	#Envia por el respectivo topic al nodo que se suscriba al topic	
		pubB.publish(d_bool)
		pubI.publish(d_int)
		pubF.publish(d_float)
		rate.sleep()
		#asegura que se cumpla la frecuencia para publicar datos

if __name__ == '__main__':
	try:
    		Ttalker()
		#nombre de la funcion principal
	except rospy.ROSInterruptException:
		pass

