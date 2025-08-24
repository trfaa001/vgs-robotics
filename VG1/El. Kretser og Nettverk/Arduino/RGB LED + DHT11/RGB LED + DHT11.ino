#include "DHT.h" //adds the DHT library

#define DHTPIN 2 //Digital pin connected to the DHT sensor

#define DHTTYPE DHT11 //sets DHT type to 11

//sets RGB led pins
const int rLed = 3;
const int gLed = 5;
const int bLed = 6;

DHT dht(DHTPIN, DHTTYPE); //makes an object

void setup() {
  Serial.begin(9600);

  dht.begin();
}

void loop() {
  float t = dht.readTemperature(); // Read temperature as Celsius and sets the the value a float
  
  if (t >= 24){ //if its 24 degrees or over
    RGBcolor(255, 0, 0); //sets the RGB led color values
  } else if(t <= 15){ //if its 15 degrees or under
    RGBcolor(0, 0, 255);
  } else{ //if its not over 24 or under 15
    RGBcolor(0, 255, 0);
  }

  Serial.println(t); //prints out how hot/cold it is in celsius
  delay(1000); //1 second delay
}

//function to easily select RGB Led's color
void RGBcolor(int rVal, int gVal, int bVal){
  analogWrite(rLed, rVal);
  analogWrite(gLed, gVal);
  analogWrite(bLed, bVal);
}