#!/usr/bin/env python
#Asegura que todo el Script se ejecute como Python (NO MODIFICAR!!)

#------LIBRERIAS-----------
#Necesario siempre que se escriban nodos en ROS
import rospy
import math

#Importar "int/bool/float" de std_msgs /permite reutilizar el contenedor string para publicar mensajes/
from std_msgs.msg import Int16
from std_msgs.msg import String

#Declaracion variable global

hint=int(5) 

def callback(data):
	global hint			#volvemos global para trabajar en todo el cod
	hint=data.data			#hint es el valor recibido del topic int
	#rospy.loginfo(data.data)
	
def nodeC():
	rospy.init_node('C', anonymous=False)				#Creacion del nodo "C"
	rospy.Subscriber('int', Int16 , callback)			#Conexion topic "int" (A -> C)
	pubS = rospy.Publisher('CString', String, queue_size=10)	#Creacion topic "Cstring"
	rate=rospy.Rate(1)						#Frecuencia

	#Proceso	
	
	while not rospy.is_shutdown():

		#Funciones de membresia (Rectas / trimf)

		by=(((-1.0/5.0)*(hint))+1.0)*100.0	#funcion para "Bajo" (((-1/4)*(hint))+1)*100
		muy=((1.0/2.0)*(hint-3.0))*100.0	#funcion para "Medio" (recta subiendo)
		mdy=((-1.0/2.0)*(hint-5.0)+1.0)*100.0	#funcion para "Medio" (recta bajando)
		ay=(1.0/5.0)*(hint-5.0)*100.0		#funcion para "Alto"
		
		#rospy.loginfo(hint)
		#rospy.loginfo(by)
		#rospy.loginfo(muy)
		#rospy.loginfo(mdy)
		#rospy.loginfo(ay)
		


		#Condicionales (Aseguran que los valores tengan los limites requeridos)

		if by>100 or by<0:by=0		
		if muy>100 or muy<0:muy=0		
		if mdy>100 or mdy<0:mdy=0		
		if ay>100 or ay<0:ay=0

		#dependiendo en cual recta de medio se encuentra hint"
		if muy!=0:
			stringPub="High %d Medium %d Low %d"%(ay,muy,by)		
		else:
			stringPub="High %d Medium %d Low %d"%(ay,mdy,by)

		pubS.publish(stringPub)		#Publica el mensaje
		rospy.loginfo(stringPub)	#Muestra lo que envia

		#debug
		#rospy.loginfo(hint)
		
		rate.sleep()	#rateSleep

if __name__ == '__main__':
	try:
    		nodeC()
	except rospy.ROSInterruptException:
		pass

