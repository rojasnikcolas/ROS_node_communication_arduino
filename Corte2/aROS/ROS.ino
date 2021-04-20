#include <ros.h>
#include <std_msgs/String.h>

String tstring="";
bool Vbool=0;
int Vint=0;
float Vfloat=0.0;
char Send[30];
int b;

ros::NodeHandle arduinoNode;
std_msgs::String talked;

ros::Publisher arduinoP("aROS", &talked);

void callback(const std_msgs::String& heared)
{
  if((String)heared.data == "Low")
  {
    analogWrite(9,25);
  }
  if((String)heared.data == "Medium")
  {
    analogWrite(9,127);
  }
  if((String)heared.data == "High")
  {
    analogWrite(9,255);
  }
}

ros::Subscriber<std_msgs::String> arduinoS("StringArduino", callback);

void setup(){
  pinMode(9, OUTPUT);
  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  pinMode(A2, INPUT);  
  arduinoNode.initNode();
  arduinoNode.advertise(arduinoP);
  arduinoNode.subscribe(arduinoS);
}

void loop(){
  Vint=floor(map(analogRead(A0), 0, 1023, 0, 10));
  Vfloat=map(analogRead(A1), 0, 1023.0, 0, 1000)*1/100.0;
  b=digitalRead(A2);
  Serial.println(Vfloat);
  tstring="Bool " + (String)b + " Int " + (String)Vint + "Float " + (String)Vfloat;
  tstring.toCharArray(Send,30);
  talked.data=Send;
  arduinoP.publish(&talked);
  arduinoNode.spinOnce();
}
