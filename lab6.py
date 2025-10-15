int ldrPin = A0;
int potPin = A1;
int ledPin = 8;
int buzzerPin = 9;

int lightValue = 0;
int potValue = 0;
unsigned long darkStart = 0;
bool isDark = false;

void setup() {
  pinMode(ledPin, OUTPUT);
  pinMode(buzzerPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  lightValue = analogRead(ldrPin);
  potValue = analogRead(potPin);
  int threshold = map(potValue, 0, 1023, 200, 400);

  if (lightValue < threshold) {
    digitalWrite(ledPin, HIGH);
    if (!isDark) {
      isDark = true;
      darkStart = millis();
    }
    if (millis() - darkStart > 5000) {
      tone(buzzerPin, 1000, 300);
      delay(300);
    }
  } else {
    digitalWrite(ledPin, LOW);
    noTone(buzzerPin);
    isDark = false;
  }

  delay(100);
}
