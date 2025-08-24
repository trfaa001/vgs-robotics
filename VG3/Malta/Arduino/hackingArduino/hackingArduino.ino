#include <TimerOne.h>


const int sigPin = 11;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); //Initialize communication with pc
  pinMode(sigPin, OUTPUT);
  Timer1.initialize(40); //25kHz
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println("Enter the motor speed (0-1023)");
  while(Serial.available()==0); //Stop the code while there is no serial connection
  int value = Serial.parseInt(); //Take integer from serial connection
  Timer1.pwm(sigPin, value);
  Serial.println("The motor speed has been set to ");
  Serial.println(value);
}
