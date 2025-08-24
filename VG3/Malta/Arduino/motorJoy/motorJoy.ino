#include "LatchingButton.h"

int value = 0;

LatchingButton button(6);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(5, OUTPUT); //EN
  pinMode(3, OUTPUT); //IN1
  pinMode(4, OUTPUT); //IN2

  pinMode(6, INPUT); //Switch
  pinMode(A0, INPUT); //VRY
  pinMode(A1, INPUT); //VRX

 
}

void loop() {

  Serial.println(digitalRead(6));

  int direction = analogRead(A1);
  int speed = analogRead(A0);
  //Serial.println(speed);

  if (button.pushed()){
    speed = 0;
    //Serial.println("Stopped");
  }

  analogWrite(5, speed);


  if (direction >= 550){
    digitalWrite(3, HIGH);
    digitalWrite(4, LOW);
    
  }
  if (direction < 450){
    digitalWrite(3, LOW);
    digitalWrite(4, speed);
  }



}
