//include library for lcd
#include <LiquidCrystal_I2C.h>

//set lcd info
LiquidCrystal_I2C lcd(0x3F,16,2);

//set pins for component
const int potpin = A0;
const int startpin = 2;
const int stoppin = 3;
const int addpin = 4;
const int rmvpin = 7;

//make variable for potensiometer value and btn states
int potWiper;
int startstate;
int stopstate;
int addstate;
int rmvstate;


//variables for if the state has changed
int startchange = 0;
int stopchange = 0;

//unsigned long values for debounce
unsigned long lastDebounceTime = 0;
unsigned long lastDebounceTimebtn1 = 0;
unsigned long lastDebounceTimebtn2 = 0;
unsigned long debounceDelay = 500;

//counter value
int counter = 0;



void setup() {
  //set pinmode for used pins
  pinMode(potpin, INPUT);
  pinMode(startpin, INPUT_PULLUP);
  pinMode(stoppin, INPUT_PULLUP);
  pinMode(addpin, INPUT_PULLUP);
  pinMode(rmvpin, INPUT_PULLUP);

  //start communication to lcd and turn on backlight on lcd
  lcd.init();
  lcd.backlight();

  //print text that doesnt need to change
  lcd.setCursor(0, 0);
  lcd.print("PotVal:");

  lcd.setCursor(0, 1);
  lcd.print("Start:");
  lcd.setCursor(9, 1);
  lcd.print("Stop:");

  Serial.begin(9600);
}

void loop() {
  //set that the button havent been pushed yet
  startchange = 0;
  stopchange = 0;

  //read state of buttons
  startstate = digitalRead(startpin);
  stopstate = digitalRead(stoppin);
  addstate = digitalRead(addpin);
  rmvstate = digitalRead(rmvpin);
  
  potWiper = analogRead(potpin); //read value of potensiometer
  potWiper = map(potWiper, 0, 1023, 0, 100+1); //convert the value of the potensiometer to a value from 0 to 100


  //clean the area where pot value is written to remove junk
  lcd.setCursor(8, 0);
  lcd.print("    ");

  //write pot value to lcd
  lcd.setCursor(8, 0);
  lcd.print(potWiper);
  lcd.print("%");

  if ((startstate == LOW) && ((millis() - lastDebounceTimebtn1) > debounceDelay)){ //if button is pushed and enough time has gone
    startchange = 1; //set that the button has been pushed
    lastDebounceTimebtn1 = millis(); // set the last time the btn1 has bounced to now
  }
  

  if ((stopstate == LOW) && ((millis() - lastDebounceTimebtn2) > debounceDelay)){
    stopchange = 1;
    lastDebounceTimebtn2 = millis();
  }

  //if button 2 changed state write 1 for stop and 0 for start
  lcd.setCursor(15, 1);
  if (stopchange == 1){
    lcd.print("1");
    lcd.setCursor(7, 1);
    lcd.print("0");
  }

  //if button 1 changed state write 1 for start and 0 for stop
  lcd.setCursor(7, 1);
  if (startchange == 1){
    lcd.print("1");
    lcd.setCursor(15, 1);
    lcd.print("0");
  }

  // if both buttons were pushed reset counter value and set stop and start to 0
  if ((startchange == 1) && (stopchange == 1)){
    lcd.setCursor(7, 1);
    lcd.print("0");
    lcd.setCursor(15, 1);
    lcd.print("0");
    counter = 0;
  }

  // if enought time has gone and button 3 is pushed add 1 to counter
  if ((addstate == LOW) && ((millis() - lastDebounceTime) > debounceDelay)){
    counter++;
    lastDebounceTime = millis();
  }
  
  // if enought time has gone and button 4 is pushed remove 1 from counter
  if ((rmvstate == LOW) && ((millis() - lastDebounceTime) > debounceDelay)){
    counter--;
    lastDebounceTime = millis();
  }

  //write counter value and remove junk after the counter
  lcd.setCursor(13, 0);
  lcd.print(counter);
  lcd.print("   ");
  Serial.println(addstate);
}