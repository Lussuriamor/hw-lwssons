const int sensorPin = A0;     
const int ledPin = 8;        
const int buzzerPin = 7;      

int melody[] = {262, 294, 330, 349, 392, 440, 494};
int noteDuration = 250;      

void setup() {
  pinMode(sensorPin, INPUT);
  pinMode(ledPin, OUTPUT);
  pinMode(buzzerPin, OUTPUT);
  digitalWrite(ledPin, LOW);
  digitalWrite(buzzerPin, LOW);
}

void loop() {
  int sensorState = digitalRead(sensorPin);

  if (sensorState == HIGH) { 
    for (int i = 0; i < sizeof(melody)/sizeof(melody[i]); i++) {
      digitalWrite(ledPin, HIGH);
      tone(buzzerPin, melody[i]);
      delay(noteDuration);
      digitalWrite(ledPin, LOW);
      noTone(buzzerPin);
      delay(50); 
    }
  } else {
    digitalWrite(ledPin, LOW);
    noTone(buzzerPin);
  }
}
