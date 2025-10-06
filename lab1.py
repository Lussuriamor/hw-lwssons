int red = 12;      
int yellow = 11;  
int green = 10;     

int buttonON = 5;   
int buttonOFF = 4;  

boolean isRunning = false;

void setup() {
  pinMode(red, OUTPUT);
  pinMode(yellow, OUTPUT);
  pinMode(green, OUTPUT);

  pinMode(buttonON, INPUT_PULLUP);  
  pinMode(buttonOFF, INPUT_PULLUP);

  digitalWrite(red, LOW);
  digitalWrite(yellow, LOW);
  digitalWrite(green, LOW);
}

void loop() {
  if (digitalRead(buttonON) == LOW) {
    isRunning = true;
  }
  if (digitalRead(buttonOFF) == LOW) {
    isRunning = false;
    digitalWrite(red, LOW);
    digitalWrite(yellow, LOW);
    digitalWrite(green, LOW);
  }

  if (isRunning) {
    digitalWrite(red, HIGH);
    digitalWrite(yellow, LOW);
    digitalWrite(green, LOW);
    delay(3000);

    if (!isRunning) return;
    digitalWrite(red, LOW);
    digitalWrite(yellow, HIGH);
    delay(1000);

    if (!isRunning) return;
    digitalWrite(yellow, LOW);
    digitalWrite(green, HIGH);
    delay(3000);

    if (!isRunning) return;
    digitalWrite(green, LOW);
    digitalWrite(yellow, HIGH);
    delay(1000);

    digitalWrite(yellow, LOW);
  }
}