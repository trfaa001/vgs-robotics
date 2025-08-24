#include <Servo.h> //The library also works with ESC controllers

Servo ESC;     // create servo object to control the ESC

//From the datasheet of the motor
const int maxWidth = 2000; //The max pulse width in microseconds
const int minWidth = 1000;// Minimum

const int sigPin = 11; // ESC signal pin

void setup() {
  // Attach the ESC on pin 9
  ESC.attach(sigPin,minWidth,maxWidth); // (pin, min pulse width, max pulse width in microseconds) 

  Serial.begin(9600); //Begins serial communication at 9600 bits per seconds
}

void loop() {
  Serial.println("");
  Serial.println("Enter the motor speed (0-100)");

  while(Serial.available()==0); //Stop the code while there is no serial connection
  int value = Serial.parseInt(); //Take integer from serial connection

  Serial.println("The motor speed has been set to ");
  Serial.println(value);

  value = map(value, 0, 100, minWidth, maxWidth); //Map to the width that the ESC uses

  Serial.print("Microseconds: ");
  Serial.println(value);
  
  ESC.writeMicroseconds(value);    // Send the signal to the ESC
}
