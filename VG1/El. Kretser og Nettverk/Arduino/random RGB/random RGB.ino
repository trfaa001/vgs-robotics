const int redPin = 3;
const int bluePin = 5;
const int greenPin = 6;


void setup() {
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
}


void loop() {
  int Val1 = random(255);
  int Val2 = random(255);
  int Val3 = random(255);

  analogWrite(redPin, Val1);
  analogWrite(greenPin, Val2);
  analogWrite(bluePin, Val3);

  delay(1000);
}
