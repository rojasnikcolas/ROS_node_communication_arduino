#!/usr/bin/env python
#Asegura que todo el Script se ejecute como Python (NO MODIFICAR!!)

#------LIBRERIAS-----------
#Necesario siempre que se escriban nodos en ROS
import rospy
#importamos float y string para trabajarlos
#Importar "int/bool/float" de std_msgs /permite reutilizar el contenedor string para publicar mensajes/
from std_msgs.msg import Float32
from std_msgs.msg import String
#importamos euler de math
from math import e

#Declaramos la variable global
hfloat=5.5

def callback(data):
	global hfloat 			#Globalizamos la variable para trabajarla en todo el codigo
	hfloat=data.data		#hfloat = data obtenida del topic float (A -float> D)
	#rospy.loginfo(data.data)
	
def nodeD():

	rospy.init_node('D', anonymous=False)				#Creamos el nodo D
	rospy.Subscriber('float', Float32, callback)			#Conectamos por medio de float
	pubS = rospy.Publisher('DString', String, queue_size=10)	#Creamos el topic DString
	rate=rospy.Rate(1)	#Freq de envio 1s

	#Proceso

	while not rospy.is_shutdown():
		
		#Funciones de membresia (sigmoides y gausianas / sigmf - gaussmf)

		by=1.0/(1.0+e**(3.0*(hfloat-2.5)))*100.0
		my=e**(-((hfloat-5.0)**2.0)/2.0)*100.0
		ay=1.0/(1.0+e**(-3.0*(hfloat-7.5)))*100.0

		#Condicionales para asegurar los limites

		if by>100 or by<0:by=0
		if my>100 or my<0:by=0
		if ay>100 or ay<0:by=0

		stringPub="High %f Medium %f Low %f"%(ay,my,by)		#Mensaje a enviar
		pubS.publish(stringPub)					#Publica el mensaje
		rospy.loginfo(stringPub)
		
		#Debug	
		rospy.loginfo(hfloat)
		
		rate.sleep()

if __name__ == '__main__':
	try:
    		nodeD()
	except rospy.ROSInterruptException:
		pass

