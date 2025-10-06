int potPin = A0;
int ledPin = 11;
int potValue = 0;
int ledValue = 0;

void setup()
{
  pinMode(ledPin, OUTPUT);
}

void loop()
{
  potValue = analogRead(potPin);
  ledValue = map(potValue, 0, 1023, 0, 255);
  analogWrite(ledPin, ledValue);
  delay(10);
}
