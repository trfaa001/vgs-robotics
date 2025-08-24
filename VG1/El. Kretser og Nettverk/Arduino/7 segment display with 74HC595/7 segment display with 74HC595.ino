//Pin connected to ST_CP (RCLK) of 74HC595
const int latchPin = 8;
//Pin connected to SH_CP (SRCLK) of 74HC595
const int clockPin = 12;
////Pin connected to DS (SER) of 74HC595
const int dataPin = 11;

int i = 0; //create variable i

//select pin modes and start serial communication
void setup() {
  pinMode(latchPin, OUTPUT);
  pinMode(clockPin, OUTPUT);
  pinMode(dataPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {} //checks for serial communication
    //read input from serial monitor
    i = Serial.parseInt();  

    switch (i) { //selects what should happen depending of the value of "i"
     case 0: //if i has the value of 0
       shiftReg(126); //calls the function shiftReg with value 126
       break; //breaks out of the case so the program can loop again
     case 1:
       shiftReg(18);
       break;
     case 2:
       shiftReg(188);
       break;
     case 3:
       shiftReg(182);
       break;
     case 4:
       shiftReg(210);
       break;
     case 5:
       shiftReg(230);
       break;
     case 6:
       shiftReg(238);
       break;
     case 7:
       shiftReg(50);
       break;
     case 8:
       shiftReg(254);
       break;
     case 9:
       shiftReg(246);
       break;
     default: // if the input isnt one of the numbers 0-9
       Serial.println("!!INVALID INPUT!!"); //print out text to serial monitor
       break;
    
   }
}

//function to  function is called 
void shiftReg(int val){
  digitalWrite(latchPin, LOW); // sets latchPin off
  shiftOut(dataPin, clockPin, LSBFIRST, val); //sends least bits by least significent to most when bit is avaible
  digitalWrite(latchPin, HIGH); // sets latchPin on
  delay(500); //delay to make the number display in half a second
}