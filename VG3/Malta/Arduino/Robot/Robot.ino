

bool didBack = false;
int rotated = 0;

void setup() {
  // put your setup code here, to run once:
  //Serial.begin(9600);
  pinMode(2, OUTPUT); // S1, FWD
  pinMode(4, OUTPUT); // S2, REV
  pinMode(5, OUTPUT); // PWM, RIGHT
  pinMode(6, OUTPUT); // PWM, LEFT
  pinMode(7, OUTPUT); // S3, REV
  pinMode(8, OUTPUT); // S4, FWD
  pinMode(12, INPUT); // IR 2, LEFT
  pinMode(13, INPUT); // IR 1, RIGHT
 
  // Make the Robot MOVE FWD
  digitalWrite(2, HIGH); // Start state is FWD
  digitalWrite(8, HIGH); // ----||----
  analogWrite(5, 0); // Start speed is 0 (RIGHT Motor)
  analogWrite(6, 0); // Start speed is 0 (LEFT motor)
}
 
void loop() {
  // put your main code here, to run repeatedly:
 
  if ((digitalRead(12) == LOW) && (digitalRead(13) == LOW)){
    if (rotated > 500){
      GO_back();
      didBack = false;
      rotated = 0;
    }
    if (didBack == false){
      Rotate();
      rotated += 1;
    }
    
    
  }
  else if (digitalRead(12) == LOW){
    MOVE_LEFT(); // raed the sig from sen IR 1
  }
 
  else if (digitalRead(13) == LOW){
    MOVE_RIGHT(); // read sig from sen IR 2
  }
  else {
    Rotate();
  }
}
 
 
// MOVE RIGHT
void MOVE_RIGHT() {
  analogWrite(5, 0); // 25% speed
  analogWrite(6, 100); // Max speed
}
 
// MOVE LEFT
void MOVE_LEFT() {
  // justeringer på hastigheten er mulig
  analogWrite(5, 100); // Max speed
  analogWrite(6, 0); // 25% speed
}
 
// MOVE FWD
void Rotate() {
  // justeringer på hastigheten er mulig
  analogWrite(5, 50); // Max speed
  analogWrite(6, 0); // Max speed
}

void GO_back() {
  digitalWrite(2, LOW);
  digitalWrite(4, LOW);
  digitalWrite(7, HIGH);
  digitalWrite(8, HIGH);
  
}