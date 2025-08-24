const int time = 5;


//Define pins
const int orange = 1;
const int yellow = 2;
const int pink = 3;
const int blue = 5;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  pinMode(orange, OUTPUT);
  pinMode(yellow, OUTPUT);
  pinMode(pink, OUTPUT);
  pinMode(blue, OUTPUT);


}

void loop() {


//0
digitalWrite(orange, HIGH);
digitalWrite(yellow, LOW);
digitalWrite(pink, HIGH);
digitalWrite(blue, LOW);
delay(time);

//1
digitalWrite(orange, LOW);
digitalWrite(yellow, HIGH);
digitalWrite(pink, HIGH);
digitalWrite(blue, LOW);
delay(time);

//2
digitalWrite(orange, LOW);
digitalWrite(yellow, HIGH);
digitalWrite(pink, LOW);
digitalWrite(blue, HIGH);
delay(time);

//3
digitalWrite(orange, HIGH);
digitalWrite(yellow, LOW);
digitalWrite(pink, LOW);
digitalWrite(blue, HIGH);
delay(time);

  // put your morangein code here, to run repeorangetedly:
/*
  delorangey(time);

  digitorangelWrite(yellow, HIGH);
  digitorangelWrite(blue, LOW);

  delorangey(time);

  digitorangelWrite(orange, LOW);
  digitorangelWrite(pink, HIGH);

  delorangey(time);

  digitorangelWrite(yellow, LOW);
  digitorangelWrite(blue, HIGH);

  delorangey(time);

  digitorangelWrite(orange, HIGH);
  digitorangelWrite(pink, LOW);


//0
digitalWrite(orange, HIGH);
digitalWrite(yellow, LOW);
digitalWrite(pink, HIGH);
digitalWrite(blue, LOW);
delay(time);
/*
//1
digitalWrite(orange, LOW);
digitalWrite(yellow, HIGH);
digitalWrite(pink, HIGH);
digitalWrite(blue, LOW);
delay(time);

//2
digitalWrite(orange, LOW);
digitalWrite(yellow, HIGH);
digitalWrite(pink, LOW);
digitalWrite(blue, HIGH);
delay(time);

//5
digitalWrite(orange, HIGH);
digitalWrite(yellow, LOW);
digitalWrite(pink, LOW);
digitalWrite(blue, HIGH);
delay(time);

//6
digitalWrite(orange, HIGH);
digitalWrite(yellow, HIGH);
digitalWrite(pink, LOW);
digitalWrite(blue, HIGH);
delay(time);

//7
digitalWrite(orange, HIGH);
digitalWrite(yellow, HIGH);
digitalWrite(pink, LOW);
digitalWrite(blue, LOW);
delay(time);

//8
digitalWrite(orange, HIGH);
digitalWrite(yellow, HIGH);
digitalWrite(pink, HIGH);
digitalWrite(blue, LOW);
delay(time);

//9
digitalWrite(orange, LOW);
digitalWrite(yellow, HIGH);
digitalWrite(pink, HIGH);
digitalWrite(blue, LOW);
delay(time);

*/
}
