const int ledPin = 5;
const int buzzerPin = 4;
const int armBtn = 6;
const int sensorBtn = 7; 
const int potPin = A0;

bool armed = false;

void setup() {
  pinMode(ledPin, OUTPUT);
  pinMode(buzzerPin, OUTPUT);
  pinMode(armBtn, INPUT_PULLUP);
  pinMode(sensorBtn, INPUT_PULLUP);
}

void loop() {
  if (digitalRead(armBtn) == LOW) {
    armed = !armed;
    delay(300);
  }
  
  if (armed && digitalRead(sensorBtn) == LOW) {
    int timeMs = map(analogRead(potPin), 0, 1023, 1000, 10000);
    runAlarm(timeMs);
  }
}

void runAlarm(int duration) {
  unsigned long start = millis();
  while (millis() - start < duration) {
    digitalWrite(ledPin, HIGH);
  	digitalWrite(buzzerPin, HIGH);
  	delay(200);
  	digitalWrite(ledPin, LOW);
  	digitalWrite(buzzerPin, LOW);
  	delay(200);
   }
}