int ledPin = 6;
int buttonPin = 8;
int buzzerPin = 7;

void setup() {
  pinMode(ledPin, OUTPUT);
  pinMode(buzzerPin, OUTPUT);
  
  pinMode(buttonPin, INPUT_PULLUP);
}

void loop() {
  int buttonState = digitalRead(buttonPin);
  
  if (buttonState == LOW) { 
    
    digitalWrite(ledPin, HIGH);
    
    digitalWrite(buzzerPin, HIGH);
    
  } else 
  
  {
    
    digitalWrite(ledPin, LOW);
    
    digitalWrite(buzzerPin, LOW);
  }
}