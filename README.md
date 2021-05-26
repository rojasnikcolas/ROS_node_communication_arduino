# CONEXIÓN ROS - ARDUINO(Arduino como Nodo)

## INTRODUCCIÓN


Este paquete contiene nodos ROS desde la A hasta la H, que publican y suscriben diferentes tipos de variables (Bool, Int16, FLoat32, Char y String) para, posteriormente, comunicarse con arduino, el cual está usado como un nodo y simular una implementación real de un caso en particular.

   --> B --> E -->
A  --> C --> F --> H --> arduino -|
^  --> D --> G -->                |
|---------------------------------|

## NODES

- A Node: Subscribes to a String topic from Arduino and substract from it the value of each sensor. It publishes each value on a differen topic: Bool, Int16 and Float32  
- B Node: It subscribes to a a Bool topic from Node A, calculates the low/medium/high level. It publishes a String wich contains each of calculated values.
- C Node: It subscribes to an Int topic from Node A, calculates the low/medium/high level. It publishes a String wich contains each of calculated values.
- D Node: It subscribes to a Float topic from Node A, calculates the low/medium/high level. It publishes a String wich contains each of calculated values.
- E Node: It subscribes to a String topic from Node B, Extracts the low/medium/high level and compares their values. Finally,it publishes a char with the letter of the highest value.
- F Node: It subscribes to a String topic from Node C, Extracts the low/medium/high level and compares their values. Finally,it publishes a char with the letter of the highest value.
- G Node: It subscribes to a String topic from Node D, Extracts the low/medium/high level and compares their values. Finally,it publishes a char with the letter of the highest value.
- H Node: It subscribes to a char topic from Nodes B,C and D, wich are converted to a 0 - 100% value wich is published on a String topic.
- Arduino Node: It subscribes to a String topic from Node H, it uses te value to set a motor Speed, it also takes the value from 3 sensors and publishes a String with the sensors value. 

## TOPICS

1. From A Node:

- Booleano: It publishes binary numbers (0 or 1) as ROS Bool type variable at 10 hertz frequency. 
- Entero: It publishes int numbers as ROS Int16 type variable at 10 hertz frequency. 
- FLotante: It publishes float numbers as ROS FLoat32 type variable at 10 hertz frequency. 
2. From B Node: 
- String_B: It publishes a ROS String with the following format: "Alto=<High_value>%/Medio=<Med_value>%/Bajo=<Low_value>% at 1 hertz frequency.

3. From C Node: 
- String_C: It publishes a ROS String with the following format: "Alto=<High_value>%/Medio=<Med_value>%/Bajo=<Low_value>% at 1 hertz frequency.

4. From D Node: 
- String_D: It publishes a ROS String with the following format: "Alto= <High_value> %/Medio= <Med_value> %/Bajo= <Low_value> % at 1 hertz frequency.

5. From E Node: 
- Char_E: It publishes a ROS char which can be 65, 77 or 66 to represent A, M and B respectively at 0.5 hertz frequency.


6. From F Node: 
- Char_F: It publishes a ROS char which can be 65, 77 or 66 to represent A, M and B respectively at 0.5 hertz frequency.


7. From G Node: 
- Char_G: It publishes a ROS char which can be 65, 77 or 66 to represent A, M and B respectively at 0.5 hertz frequency.


8. From H Node: 
- Int_H: It publishes int numbers as ROS Int16 type variable at 0.2 hertz frequency. 


9. From Arduino Node: 
- String_Ard: It publishes a ROS String type variable with the following format: Bool= <boolean_value> Int=<Int_value> Float= <float_value> at 100 hertz frequency. 

## EXECUTION

**To execute the program, it may be done on this way:**

1. Execute roscore:
> $ roscore

2. Execute the following command from a different terminal:
> rosrun <folder_name> <scrypt_name>.py

3. To visualize the correct linking between nodes, this command can be used:
> $ rqt_graph

## ARDUINO NODE EXECUTION

- In order tu execute Arduino node, the first thing must be done is to give permisions to the serial port, it can be done this way:
> $ sudo chmod 777 /dev/ttyACM0
o
> $ sudo chmod 777 /dev/ttyUSB0

- Load the code on the Arduino board and execute the following command:

> $ rosrun rosserial_python serial_node.py /dev/ttyACM0 


# AUTHORS

- Mauricio Gómez Menjura
- Eymer S. Tapias
- Nikcolas Rojas
