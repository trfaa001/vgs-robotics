//define global variables
const int red_light_pin= 3; //RGB red-anode connected in series with 220 Ohm resister to pin 9 
const int green_light_pin = 6;
const int blue_light_pin = 5;
 
//declare inputs and outputs
void setup() {
  pinMode(red_light_pin, OUTPUT); //define RGB red-anode pin as OUTPUT
  pinMode(green_light_pin, OUTPUT);
  pinMode(blue_light_pin, OUTPUT);
}
 
//fade single color off and on
 
void loop() {
  analogWrite(red_light_pin, 255); // Red 100%
  delay(1000);
  analogWrite(red_light_pin, 127); // Red 50%
  delay(1000);
  analogWrite(red_light_pin, 64); // Red 25%
  delay(1000);

  //changes the strength of green
  analogWrite(green_light_pin, 255); // green 100%
  delay(1000);
  analogWrite(green_light_pin, 127); // green 50%
  delay(1000);
  analogWrite(green_light_pin, 64); // green 25%
  delay(1000);
}
