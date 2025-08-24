#include "Stepper.h"

const int stepsPerRevolution = 200;  // change this to fit the number of steps per revolution
// for your motor


// initialize the stepper library on pins 8 through 11:
Stepper myStepper(stepsPerRevolution, 1, 2, 3, 5);

void setup() {
  // put your setup code here, to run once:
  myStepper.setSpeed(150);
  
  

}

void loop() {
  // put your main code here, to run repeatedly:

  myStepper.step(200);
  delay(1000);
}
