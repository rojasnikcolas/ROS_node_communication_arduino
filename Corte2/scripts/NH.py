#!/usr/bin/env python
#Asegura que todo el Script se ejecute como Python (NO MODIFICAR!!)

#------LIBRERIAS-----------
import rospy
#Necesario siempre que se escriban nodos en ROS
from std_msgs.msg import String
from std_msgs.msg import Char
#Importar "String" de std_msgs /permite reutilizar el contenedor string para publicar mensajes/

#Declaramos la variable
Echar=00
Fchar=00
Gchar=00

def callbackE(data):
	global Echar			#Globalizamos la variable para trabajarla en todo el cod
	Echar=data.data			#hstring=dato recibido de (B -Bstring> E)
	#rospy.loginfo(data.data)
def callbackF(data):
	global Fchar			#Globalizamos la variable para trabajarla en todo el cod
	Fchar=data.data			#hstring=dato recibido de (B -Bstring> E)
	#rospy.loginfo(data.data)
def callbackG(data):
	global Gchar			#Globalizamos la variable para trabajarla en todo el cod
	Gchar=data.data			#hstring=dato recibido de (B -Bstring> E)
	#rospy.loginfo(data.data)
    
def nodeH():
	
	rospy.init_node('H', anonymous=False)			#Creamos el nodo E
	rospy.Subscriber('Echar', Char, callbackE)		#Char Bool
	rospy.Subscriber('Fchar', Char, callbackF)		#Char Int
	rospy.Subscriber('Gchar', Char, callbackG)		#Char Float
	pubS=rospy.Publisher('StringArduino', String, queue_size=10)	#Creamos el topic de de arduino
	rate=rospy.Rate(0.2)	#Freq 2s

	#Proceso	
	
	while not rospy.is_shutdown():
		
		string=None
		if Echar==72:
			if Fchar==72:
				if Gchar==72 or Gchar==77:
					string="High"
				elif Gchar==76:
					string="Medium"
			elif Fchar==77:
				if Gchar==72:
					string="High"
				elif Gchar==77:
					string="Medium"
				elif Gchar==76:
					string="Low"
			elif Fchar==76:
				if Gchar==72:
					string="Medium"
				elif Gchar==77 or Gchar==76:
					string="Low"
		elif Echar==76:
			if Fchar==72:
				if Gchar==72:
					string="Medium"
				elif Gchar==77 or Gchar==76:
					string="Low"
			elif Fchar==77:
				string="Low"
			elif Fchar==76:
				string="Low"
		

		rospy.loginfo(string)
		pubS.publish(string)		
				
		#DEBUG
		
		#rospy.loginfo(Echar)
		#rospy.loginfo(Fchar)
		#rospy.loginfo(Gchar)
		

		rate.sleep()	#rate.sleep


if __name__ == '__main__':
	try:
    		nodeH()
	except rospy.ROSInterruptException:
		pass
    
