const int trigPin = 8;
const int echoPin = 9;
const int greenLED = 10;
const int yellowLED = 11;
const int redLED = 12;
const int buzzer = 7;

long duration;
float distance;

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  pinMode(greenLED, OUTPUT);
  pinMode(yellowLED, OUTPUT);
  pinMode(redLED, OUTPUT);
  pinMode(buzzer, OUTPUT);

  Serial.begin(9600);
}

void loop() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH);
  distance = duration * 0.034 / 2;  

  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");
  
  digitalWrite(greenLED, LOW);
  digitalWrite(yellowLED, LOW);
  digitalWrite(redLED, LOW);
  noTone(buzzer);
  
  if (distance > 30) {
    digitalWrite(greenLED, HIGH);
  } 
  else if (distance <= 30 && distance >15) {
    digitalWrite(yellowLED, HIGH);
  } 
  else if (distance <= 15 && distance > 5) {
    digitalWrite(redLED, HIGH);
  } 
  else {
    digitalWrite(redLED, HIGH);
    tone(buzzer, 3000);
  }

  delay(200);
}
