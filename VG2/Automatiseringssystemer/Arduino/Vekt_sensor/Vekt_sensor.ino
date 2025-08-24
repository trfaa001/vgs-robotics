const int btnPin = 2;
const int outPin = 12;

int btnState;

unsigned long lastDebounceTime;

int debounceDelay = 1000;

void setup(){
  pinMode(btnPin, INPUT_PULLUP);
  pinMode(outPin, OUTPUT);

  Serial.begin(9600);
}

void loop(){

  btnState = digitalRead(btnPin);

  if ((btnState == LOW) && ((millis() - lastDebounceTime) > debounceDelay)){
    lastDebounceTime = millis();
    Serial.println("Button has been pressed");

    digitalWrite(outPin, HIGH);
  }
}