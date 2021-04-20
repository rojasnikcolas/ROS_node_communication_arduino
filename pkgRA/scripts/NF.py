#!/usr/bin/env python
#Asegura que todo el Script se ejecute como Python (NO MODIFICAR!!)

#------LIBRERIAS-----------
import rospy
#Necesario siempre que se escriban nodos en ROS
from std_msgs.msg import String
from std_msgs.msg import Char
#Importar "String" de std_msgs /permite reutilizar el contenedor string para publicar mensajes/

#Declaramos la variable
hstring="High 100 Medium 0 Low 0"

def callback(data):
	global hstring			#Globalizamos la variable para trabajarla en todo el cod
	hstring=data.data		#hstring=dato recibido de (B -Bstring> E)
	#rospy.loginfo(data.data)
    
def nodeF():
	
	rospy.init_node('F', anonymous=False)			#Creamos el nodo E
	rospy.Subscriber('CString', String, callback)		#Susribimos y recibimos data de Bstr
	pubS=rospy.Publisher('Fchar', Char, queue_size=10)	#Creamos el topic de Echar
	rate=rospy.Rate(0.5)	#Freq 2s

	#Proceso	
	
	while not rospy.is_shutdown():

		Vint=[0,0,0]	#Definir
		Vint[0]=int(hstring[4:hstring.find("Medium")-1])			#valor alto
		Vint[1]=int(hstring[hstring.find("Medium")+7:hstring.find("Low")-1])	#valor medio
		Vint[2]=int(hstring[hstring.find("Low")+4:len(hstring)])		#valor bajo
		
		#DEBUG
		
		#rospy.loginfo(Vint[0])
		#rospy.loginfo(Vint[1])
		#rospy.loginfo(Vint[2])

		c=0	#Valor mayor rempasable
		b=0	#Bandera valor
		i=0	#Contador

		for n in Vint:			#For que pasa por todo el vector
			if Vint[i]>c:		#Queda guardado el valor mayor de las 3 posiciones
				c=Vint[i]			
				b=i	#Me dice que posicion del vector 0-H 1-M 2-L
			i=i+1

		if b==0: 
			sendChar=72	#ASCII High - H
		elif b==1: 
			sendChar=77	#ASCII Medium - M
		elif b==2: 
			sendChar=76	#ASCII Low - L

		pubS.publish(sendChar)
		rospy.loginfo(sendChar)
		#rospy.loginfo(b)

		rate.sleep()	#rate.sleep


if __name__ == '__main__':
	try:
    		nodeF()
	except rospy.ROSInterruptException:
		pass
    
