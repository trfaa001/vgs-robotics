#include <Servo.h>

Servo myservo;  // create Servo object to control a servo

int pos = 0;    // variable to store the servo position

const int servoPin = 9;
const int trigPin = 10;
const int echoPin = 11;

int i = 0;
int repeat = 5;


long duration;  // variable for how long time it took before the ultra sonic sensor receiver it sound back
int distance;   // Variable for the distance between the ultra sonic sensor and what reflected the sound back
int theReadDistance; // The distance read

void setup() {
  // put your setup code here, to run once:
  pinMode(2, OUTPUT); // S1, FWD
  pinMode(4, OUTPUT); // S2, REV
  pinMode(5, OUTPUT); // PWM, RIGHT SIDE
  pinMode(6, OUTPUT); // PWM, LEFT SIDE
  pinMode(7, OUTPUT); // S3, REV
  pinMode(8, OUTPUT); // S4, FWD
  pinMode(12, INPUT); // IR 2, LEFT
  pinMode(13, INPUT); // IR 1, RIGHT

  pinMode(servoPin, OUTPUT); // Servo
  pinMode(trigPin, OUTPUT); // Trigger pin ultrasonic sensor
  pinMode(echoPin, INPUT); // Echo pin ultrasonic sensor

  myservo.attach(9);  // attaches the servo on pin 9 to the Servo object

  // Serial.begin(9600);

  delay(500);
}
 
void loop() {
  // put your main code here, to run repeatedly:
  turnRight();

  delay(10000);

}
 
int readDistance() {


  // code block to be executed
  digitalWrite(trigPin, LOW);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
 
  duration = pulseIn(echoPin, HIGH); // waits for echo pin go from low to high and starts timing and returns the lenght of the the pulse in microseconds
 
  distance = duration * 0.034 / 2; // calculate the distance in centimeter

  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println("cm");
  return distance;
}

void check() {

  Serial.println("Check");

  myservo.write(0);  // see Right
  delay(15);  // waits 15 ms for the servo to reach the position

  if (readDistance() > 11){
    turnRight();
  }
  else {
    myservo.write(180); // turn the servo left
    if (readDistance() > 11){
      turnLeft();
    }

  }
}

void turnRight() {

  // Serial.println("turnRight");
  digitalWrite(2, HIGH); // Start state is FWD
  digitalWrite(8, HIGH); // ----||----
 
  analogWrite(5, 0);
  analogWrite(6, 100);

  delay(3000);

  stop();
}

void turnLeft() {

  Serial.println("turnLeft");

  digitalWrite(2, LOW);
  digitalWrite(4, LOW);
  digitalWrite(7, HIGH);
  digitalWrite(8, HIGH);
 
  analogWrite(5, 256);
  analogWrite(6, 256);
}

void driveFWD() {

  Serial.println("driveFWD");

  // Make the Robot MOVE FWD
  digitalWrite(4, LOW);
  digitalWrite(7, LOW);
  digitalWrite(2, HIGH); // Start state is FWD
  digitalWrite(8, HIGH); // ----||----
 
  // justeringer på hastigheten er mulig
  analogWrite(5, 512); // Max speed
  analogWrite(6, 512); // Max speed
}

void stop() {

  // Serial.println("stop");

  // digitalWrite(4, LOW);
  // digitalWrite(7, LOW);
  // digitalWrite(2, LOW);
  // digitalWrite(8, LOW);
 
  // justeringer på hastigheten er mulig
  analogWrite(5, 0); // Max speed
  analogWrite(6, 0); // Max speed
}