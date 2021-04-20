#!/usr/bin/env python
#Asegura que todo el Script se ejecute como Python (NO MODIFICAR!!)

#------LIBRERIAS-----------
import rospy
#Necesario siempre que se escriban nodos en ROS
from std_msgs.msg import String
#Importar "String" de std_msgs /permite reutilizar el contenedor string para publicar mensajes/
#se pueden agregar mas

def callback(data):
#data=valor obtenido del topic suscrito
#si se quiere trabajar con esta variable toca convertirla en global
	rospy.loginfo(data.data)
	#muestra el valor
    
def Tlistener():
	rospy.init_node('Tlistener', anonymous=False)
	#Crea el nodo(nombre,nombre anonimo para unicos nombres)
	rospy.Subscriber('string', String, callback)
	#El nodo se suscribe al topic(nombre,tipo de variable,llama a la funcion)
	rospy.spin()
	#hace que no se salga del proceso suscrito

if __name__ == '__main__':
	try:
    		Tlistener()
		#llama la funcion principal
	except rospy.ROSInterruptException:
		pass
    
