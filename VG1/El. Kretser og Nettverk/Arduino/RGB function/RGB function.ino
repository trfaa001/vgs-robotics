//define global variables
const int rLed = 3;
const int gLed = 6;
const int bLed = 5;
 
//declare inputs and outputs
void setup() {
  pinMode(rLed, OUTPUT);
  pinMode(gLed, OUTPUT);
  pinMode(bLed, OUTPUT);
}
 
void loop() {
  RGBcolor(255, 0, 255);
  delay(1000);
  RGBcolor(255, 255, 0);
  delay(1000);
}

//a function to set RGB Led color
void RGBcolor(int rVal, int gVal, int bVal){
  analogWrite(rLed, rVal);
  analogWrite(gLed, gVal);
  analogWrite(bLed, bVal);
}