#!/usr/bin/env python

#Asegura que todo el Script se ejecute como Python (NO MODIFICAR!!)

#------LIBRERIAS-----------

import rospy
#Necesario siempre que se escriban nodos en ROS
import random
from std_msgs.msg import Int16
from std_msgs.msg import Bool
from std_msgs.msg import Float32
from std_msgs.msg import String
#Importar "int/bool/float" de std_msgs /permite reutilizar el contenedor string para publicar mensajes/

#------Define la Clase (Atributos y Metodos)-----

ARDstring=None
def callback(data):
	global ARDstring		#Globalizamos la variable para trabajarla en todo el cod
	ARDstring=data.data		#hstring=dato recibido de (B -Bstring> E)
	#rospy.loginfo(data.data)

def nodeA():
	#--------Topics
	pubB = rospy.Publisher('bool', Bool, queue_size=10)
	pubI = rospy.Publisher('int', Int16, queue_size=10)
	pubF = rospy.Publisher('float', Float32, queue_size=10)
	rospy.Subscriber('aROS', String, callback) 		#Topic de Ros creado en arduino
	rospy.init_node('A', anonymous=False)
	rate = rospy.Rate(10)
	

	
	while not rospy.is_shutdown():
	#Bool 1 Int 12 Float 21
			
		Vbool=bool(int(ARDstring[5]))						#valor bool
		Vint=int(ARDstring[ARDstring.find("Int")+4:ARDstring.find("Float")])	#valor int
		Vfloat=float(ARDstring[ARDstring.find("Float")+6:len(ARDstring)])	#valor float
		pubB.publish(Vbool)	#Enviamos en el topic bool
		pubI.publish(Vint)	#enviamos en el topic int
		pubF.publish(Vfloat)	#enviamos en el topic float
		
		#Muestra en el nodo A lo que va a enviar
		rospy.loginfo(ARDstring)
		rospy.loginfo(Vbool)
		rospy.loginfo(Vint)
		rospy.loginfo(Vfloat)
		rate.sleep()

if __name__ == '__main__':
	try:
    		nodeA()
	except rospy.ROSInterruptException:
		pass

