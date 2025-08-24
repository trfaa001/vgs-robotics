#include "pitches.h"

// Pins to connected components
const int rLed = 3;
const int gLed = 5;
const int bLed = 6;
const int activeBuzzerPin = 8;
const int trigPin = 9;
const int echoPin = 10;

// Variables to know last time since the buzzer made sound
unsigned long lastDebounceMiddle = 0;
unsigned long lastDebounceShort = 0;

// Variables for the delay between when the buzzer last made sound for each mode
int debounceDelayShort = 100;
int debounceDelayMiddle = 200;

// Variable for which distance range the distance is currently in
int distanceMode;

long duration;  // variable for how long time it took before the ultra sonic sensor receiver it sound back
int distance;   // Variable for the distance between the ultra sonic sensor and what reflected the sound back

void setup() {
  pinMode(trigPin, OUTPUT); // Set the trigger pin to output so the program can send signal for when the sensor should send out ultra sonic sound
  Serial.begin(9600);   //Start communication to connected devices via usb at 9600 bits per second
}

void loop() {
  //turn the trigger pin to HIGH for 10 microseconds
  digitalWrite(trigPin, LOW); //
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH); // waits for echo pin go from low to high and starts timing and returns the lenght of the the pulse in microseconds

  distance = duration * 0.034 / 2; // calculate the distance in centimeter

  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println("cm");

  if (distance > 10){
    distanceMode = 3;
  }

  if (distance < 10){
    distanceMode = 2;
  }

  if (distance < 5){
    distanceMode = 1;
  }

  if ((distanceMode == 1) && ((millis() - lastDebounceShort) > debounceDelayShort)){
    RGBcolor(255, 0, 0);
    tone(activeBuzzerPin, NOTE_DS8, 50);

    lastDebounceShort = millis();
  }

  if ((distanceMode == 2) && ((millis() - lastDebounceMiddle) > debounceDelayMiddle)){
    RGBcolor(255, 255, 0);
    tone(activeBuzzerPin, NOTE_FS4, 50);

    lastDebounceMiddle = millis();
  }

  if (distanceMode == 3){
    RGBcolor(0, 255, 0);
  }

}

//function to easily select RGB Led's color
void RGBcolor(int rVal, int gVal, int bVal){
  analogWrite(rLed, rVal);
  analogWrite(gLed, gVal);
  analogWrite(bLed, bVal);
}
