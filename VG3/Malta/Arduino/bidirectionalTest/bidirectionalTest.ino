
int value = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(3, OUTPUT); //EN
  pinMode(2, OUTPUT); //IN1
  pinMode(4, OUTPUT); //IN2


}

void loop() {

  Serial.println("Please write: FWD, REV, STOP or SPEED");

  
  // put your main code here, to run repeatedly:
  while(Serial.available()==0); //Stop the code while there is no new message from pc
  String prompt = Serial.readString();
  

  prompt.trim(); //remove non user input
  prompt.toUpperCase(); //Make entire input upper case

  Serial.println(prompt);
   
  if (prompt == "SPEED"){
    Serial.println("Enter the motor speed (0-1023)");
    while(Serial.available()==0);
    int value = Serial.parseInt(); //Take integer from serial connection
    Serial.println(value);
    analogWrite(5, value);

  }

  if (prompt == "FWD"){
    digitalWrite(3, HIGH);
    digitalWrite(4, LOW);
  }
  if (prompt == "REV"){
    digitalWrite(3, LOW);
    digitalWrite(4, HIGH);
  }
  if (prompt == "STOP"){
    digitalWrite(3, LOW);
    digitalWrite(4, LOW);
  }
}
