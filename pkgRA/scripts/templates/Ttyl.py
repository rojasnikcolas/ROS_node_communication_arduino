#!/usr/bin/env python
#Asegura que todo el Script se ejecute como Python (NO MODIFICAR!!)

#------LIBRERIAS-----------
import rospy
#Necesario siempre que se escriban nodos en ROS
from std_msgs.msg import Bool
from std_msgs.msg import String
#Importar "int/bool/float" de std_msgs /permite reutilizar el contenedor string para publicar mensajes/


def callback(data):
	rospy.loginfo(data.data)
	
def Ttyl():
	rospy.init_node('TtyL', anonymous=False)
	rospy.Subscriber('bool', Bool, callback)
	pubS = rospy.Publisher('string', String, queue_size=10)
	rate=rospy.Rate(1)
	BString = "ON"
	while not rospy.is_shutdown():
	#Envia por el respectivo topic al nodo B	
		pubS.publish(BString)
		rate.sleep()

if __name__ == '__main__':
	try:
    		Ttyl()
	except rospy.ROSInterruptException:
		pass

