#include <Servo.h>

Servo myservo;  // create Servo object to control a servo

int pos = 0;    // variable to store the servo position

const int servoPin = 9;
const int trigPin = 10;
const int echoPin = 11;

const int checkDistance = 35;

int i;
int repeat = 5;

int servoDefault = 90; //Value for when the servo points forward


long duration;  // variable for how long time it took before the ultra sonic sensor receiver it sound back
int distance;   // Variable for the distance between the ultra sonic sensor and what reflected the sound back
int theReadDistance; // The distance read



void setup() {
  // put your setup code here, to run once:
  pinMode(2, OUTPUT); // S1, FWD
  pinMode(4, OUTPUT); // S2, REV
  pinMode(5, OUTPUT); // PWM, RIGHT
  pinMode(6, OUTPUT); // PWM, LEFT
  pinMode(7, OUTPUT); // S3, REV
  pinMode(8, OUTPUT); // S4, FWD
  pinMode(12, INPUT); // IR 2, LEFT
  pinMode(13, INPUT); // IR 1, RIGHT

  pinMode(servoPin, OUTPUT); // Servo
  pinMode(trigPin, OUTPUT); // Trigger pin ultrasonic sensor
  pinMode(echoPin, INPUT); // Echo pin ultrasonic sensor

  myservo.attach(9);  // attaches the servo on pin 9 to the Servo object

  Serial.begin(9600);

  myservo.write(servoDefault); // turn the servo back to default state

  delay(15);
}

void loop() {

  if (readDistance() > checkDistance){
    driveFWD();
  } else {
    stop();
    check();
  }
  
}

int readDistance() {


  // code block to be executed
  digitalWrite(trigPin, LOW);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
 
  duration = pulseIn(echoPin, HIGH); // waits for echo pin go from low to high and starts timing and returns the lenght of the the pulse in microseconds
 
  distance = duration * 0.034 / 2; // calculate the distance in centimeter

  delay(50);

  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println("cm");
  return distance;
}

void check() {

  Serial.println("Check");

  myservo.write(0);  // see right
  delay(1000);  // waits 15 ms for the servo to reach the position

  if (readDistance() > checkDistance){
    turnRight();
    myservo.write(servoDefault);
    delay(1000);
  }
  else {
    myservo.write(180); // turn the servo left
    delay(1000);
    if (readDistance() > checkDistance){
      turnLeft();
      myservo.write(servoDefault);
      delay(1000);
    }

  }
}

void turnRight() {

  Serial.println("turnRight");

  digitalWrite(2, HIGH); // Start state is FWD
  digitalWrite(8, HIGH); // ----||----
 
  analogWrite(5, 0);
  analogWrite(6, 100);

  delay(500);
  stop();
}

void turnLeft() {

  Serial.println("turnLeft");

  digitalWrite(2, HIGH); // Start state is FWD
  digitalWrite(8, HIGH); // ----||----
 
  analogWrite(5, 100);
  analogWrite(6, 0);

  delay(500);
  stop();
}

void driveFWD() {

  Serial.println("driveFWD");

  // Make the Robot MOVE FWD
  digitalWrite(2, HIGH); // Start state is FWD
  digitalWrite(8, HIGH); // ----||----
 
  // justeringer på hastigheten er mulig
  analogWrite(5, 80); // Max speed
  analogWrite(6, 80); // Max speed

}

void stop() {

  Serial.println("stop");

  digitalWrite(2, LOW); // Start state is FWD
  digitalWrite(8, LOW); // ----||----
 
  // justeringer på hastigheten er mulig
  analogWrite(5, 0); // Max speed
  analogWrite(6, 0); // Max speed
}