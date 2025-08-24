//To optimize we could reduce the delay for the servo turning time, this is in the check function
//Some variable names could be improved
//A revision using sweep and dynamic turning could be made

#include <Servo.h>

Servo myservo;  // create Servo object to control a servo

int pos = 0;    // variable to store the servo position


const int S1 = 2; // Motor 1, FWD
const int S2 = 4; // Motor 1, REV
const int S3 = 7; // Motor 2, FWD
const int S4 = 8; // Motor 2, REV
const int PWM_R = 5; // PWM, Right
const int PWM_L = 6; // PWM, Left
const int IRL = 12; // IR 2, Left
const int IRR = 13; // IR 1, Right

// Pins for sensor
const int servoPin = 9;
const int trigPin = 10;
const int echoPin = 11;

const int checkDistance = 35; // Distance checked

const int servoRotateTime = 1000; //The time it takes for the servo to turn 90 degrees

int servoDefault = 90; // Value for when the servo points forward


long duration;  // variable for how long time it took before the ultra sonic sensor receiver it sound back
int distance;   // Variable for the distance between the ultra sonic sensor and what reflected the sound back
// int theReadDistance; // The distance read

// Neuron Activation
void setup() {
  // put your setup code here, to run once:
  pinMode(S1, OUTPUT); // S1, FWD
  pinMode(S2, OUTPUT); // S2, REV
  pinMode(PWM_R, OUTPUT); // PWM, RIGHT
  pinMode(PWM_L, OUTPUT); // PWM, LEFT
  pinMode(S3, OUTPUT); // S3, REV
  pinMode(S4, OUTPUT); // S4, FWD
  pinMode(IRL, INPUT); // IR 2, LEFT
  pinMode(IRR, INPUT); // IR 1, RIGHT

  pinMode(servoPin, OUTPUT); // Servo
  pinMode(trigPin, OUTPUT); // Trigger pin ultrasonic sensor
  pinMode(echoPin, INPUT); // Echo pin ultrasonic sensor

  myservo.attach(9);  // attaches the servo on pin 9 to the Servo object

  Serial.begin(9600);

  myservo.write(servoDefault); // turn the servo back to default state

  delay(15); //Allow the arduino to fully initialize
}

// If robot too close to wall robot stop, then check the sides
void loop() {

  if (readDistance() > checkDistance){
    driveFWD();
  } else {
    stop();
    check();
  }
  
}

// Robot check if it too close like an introvert 
int readDistance() {
  // code block to be executed
  digitalWrite(trigPin, LOW);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
 
  duration = pulseIn(echoPin, HIGH); // waits for echo pin go from low to high and starts timing and returns the lenght of the the pulse in microseconds
 
  distance = duration * 0.034 / 2; // calculate the distance in centimeter

  //Why is this here?
  //Dont remove the robot kills itself without it
  delay(50);

  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println("cm");
  return distance;
}

// Robot check for hot single robots in your area 
void check() {

  Serial.println("Check");

  myservo.write(0);  // see right
  delay(servoRotateTime);  // wait for the servo to reach position

  if (readDistance() > checkDistance){
    Back_up(); //It takes some time for the robot to stop so we need to back up a little
    turnRight(); //The robot takes a 90 degree turn to the right
    myservo.write(servoDefault);
    delay(servoRotateTime);
  }
  else {

    //We could probably use less time waiting for the servo to turn
    myservo.write(180); // turn the servo left, this should takes more time than the others
    delay(servoRotateTime);
    if (readDistance() > checkDistance){
      Back_up();
      turnLeft();
      myservo.write(servoDefault);
      delay(servoRotateTime);
    }

  }
}

// Robot turn right the right way
void turnRight() {

  Serial.println("turnRight");

  digitalWrite(S4, LOW); // Start state is FWD
  digitalWrite(S3, LOW); // ----||----

  digitalWrite(S1, HIGH); // Start state is FWD
  digitalWrite(S4, HIGH); // ----||----
 
  analogWrite(PWM_R, 0);
  analogWrite(PWM_L, 100);

  delay(500);
  stop();
}

// robot turn left with exquisite poise 
void turnLeft() {

  Serial.println("turnLeft");

  digitalWrite(S1, HIGH); // Start state is FWD
  digitalWrite(S4, HIGH); // ----||----
 
  analogWrite(PWM_R, 100);
  analogWrite(PWM_L, 0);

  delay(500);
  stop();
}

// Robot retreats in a cowardly manner 
void Back_up() {
  // Make the Robot MOVE FWD
  digitalWrite(S1, LOW); // Start state is REV
  digitalWrite(S4, LOW); // ----||----

  digitalWrite(S2, HIGH); // Start state is FWD
  digitalWrite(S3, HIGH); // ----||----

  analogWrite(PWM_R, 80); // Max speed
  analogWrite(PWM_L, 80); // Max speed

  delay(15);
}

// Robot bravely advances
void driveFWD() {

  Serial.println("driveFWD");

  digitalWrite(S2, LOW); //
  digitalWrite(S3, LOW); // ----||----

  // Make the Robot MOVE FWD
  digitalWrite(S1, HIGH); // Start state is FWD
  digitalWrite(S4, HIGH); // ----||----
 
  analogWrite(PWM_R, 80); // Max speed
  analogWrite(PWM_L, 80); // Max speed

}

//Robot stop, wait a minute :)
void stop() {

  Serial.println("stop");

  digitalWrite(S1, LOW); // Start state is FWD
  digitalWrite(S4, LOW); // ----||----
 
  // justeringer på hastigheten er mulig
  analogWrite(PWM_R, 0); // Max speed
  analogWrite(PWM_L, 0); // Max speed
}