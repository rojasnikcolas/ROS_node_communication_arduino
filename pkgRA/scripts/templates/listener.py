#!/usr/bin/env python
#Asegura que todo el Script se ejecute como Python (NO MODIFICAR!!)

#------LIBRERIAS-----------
import rospy
#Necesario siempre que se escriban nodos en ROS
from std_msgs.msg import String
#Importar "String" de std_msgs /permite reutilizar el contenedor string para publicar mensajes/

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)
    #Se conecta con la linea 17. (data)=recibe de chatter. Imprime <ID del nodo que llama (suscriptor) , data=lo que recibe del topic chatter linea 17>
def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('chatter', String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
