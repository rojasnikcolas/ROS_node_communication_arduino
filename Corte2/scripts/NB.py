#!/usr/bin/env python
#Asegura que todo el Script se ejecute como Python (NO MODIFICAR!!)

#------LIBRERIAS-----------
#Necesario siempre que se escriban nodos en ROS
import rospy
#Importar "int/bool/float" de std_msgs /permite reutilizar el contenedor string para publicar mensajes/
from std_msgs.msg import Bool
from std_msgs.msg import String

#Declaramos la variable global
hbool=True

def callback(data):
	global hbool			#Globalizamos la variable para trabajarla en todo el codigo
	hbool=data.data			#hbool toma el valor de lo obttenido del topic bool del nodo A
	#rospy.loginfo(data.data)	
	
def nodeB():

	rospy.init_node('B', anonymous=False)				#Creamos el nodo B
	rospy.Subscriber('bool', Bool, callback)			#recibimos data del topic bool
	pubS = rospy.Publisher('BString', String, queue_size=10)	#creamos el topic bstring
	
	rate=rospy.Rate(1)		#Freq de envio
	d_StringT = "High 1 Low 0"	#Mensaje si recibe 1
	d_StringF = "High 0 Low 1"	#Mensaje si recibe 0
	
	#Proceso	
		
	while not rospy.is_shutdown():

	#Envia por el respectivo topic al nodo B	
		if hbool==True:		
			pubS.publish(d_StringT)	#Envia data por el topic BString
			rospy.loginfo(d_StringT)
		else:
			pubS.publish(d_StringF)	#Envia data por el topic BString
			rospy.loginfo(d_StringF)
		
		rate.sleep() #rate.sleep

if __name__ == '__main__':
	try:
    		nodeB()
	except rospy.ROSInterruptException:
		pass

