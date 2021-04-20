#!/usr/bin/env python
#Asegura que todo el Script se ejecute como Python (NO MODIFICAR!!)

#------LIBRERIAS-----------
import rospy
#Necesario siempre que se escriban nodos en ROS
from std_msgs.msg import String
from std_msgs.msg import Char
#Importar "String" de std_msgs /permite reutilizar el contenedor string para publicar mensajes/

#Declaramos la variable
hstring="0123456789112"
def callback(data):
	global hstring			#Globalizamos la variable para trabajarla en todo el cod
	hstring=data.data		#hstring=dato recibido de (B -Bstring> E)
	#rospy.loginfo(data.data)
    
def nodeE():
	
	rospy.init_node('E', anonymous=True)			#Creamos el nodo E
	rospy.Subscriber('BString', String, callback)		#Susribimos y recibimos data de Bstr
	pubs=rospy.Publisher('Echar', Char, queue_size=10)	#Creamos el topic de Echar
	rate=rospy.Rate(0.5)	#Freq 2s

	#Proceso	
	
	while not rospy.is_shutdown():

		Vbool=[0,0]			#Definir
		Vbool[0]=str(hstring[5])	#tomamos el valor de alto

		if Vbool[0]=="1":		#si lo recibido de alto es True (1)
			sendChar=72	#ASCII de H
		else:				#si es bajo False (0)
			sendChar=76	#ASCII de L

		pubs.publish(sendChar)
		rospy.loginfo(sendChar)
		
		#DEBUG

		#rospy.loginfo(dato)
		#rospy.loginfo(hstring[5])
		#rospy.loginfo(hstring[12])
		#rospy.loginfo(Vbool[0])

		rate.sleep()	#rate.sleep


if __name__ == '__main__':
	try:
    		nodeE()
	except rospy.ROSInterruptException:
		pass
    
