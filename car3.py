const int TRIG_PIN = 4;
const int ECHO_PIN = 5;
const int LED_GREEN = 10;
const int LED_YELLOW = 9;
const int LED_RED = 8;
const int BUZZER_PIN = 11;
const float DIST_YELLOW = 100.0; 
const float DIST_RED = 50.0;    
const float MIN_DISTANCE_CM = 2.0; 

unsigned long lastUltrasonic = 0;
const unsigned long ULTRASONIC_INTERVAL = 50; 

void setup() {
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);

  pinMode(LED_GREEN, OUTPUT);
  pinMode(LED_YELLOW, OUTPUT);
  pinMode(LED_RED, OUTPUT);

  pinMode(BUZZER_PIN, OUTPUT);

  Serial.begin(9600);
}

void loop() {
  if (millis() - lastUltrasonic >= ULTRASONIC_INTERVAL) {
    lastUltrasonic = millis();

    digitalWrite(TRIG_PIN, LOW);
    delayMicroseconds(2);
    digitalWrite(TRIG_PIN, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIG_PIN, LOW);

    long duration = pulseIn(ECHO_PIN, HIGH, 30000); 
    float distance;
    if (duration == 0) distance = 400; 
    else distance = duration * 0.034 / 2;

    if (distance < MIN_DISTANCE_CM) distance = MIN_DISTANCE_CM;

    Serial.print("Distance: "); Serial.println(distance);

    digitalWrite(LED_GREEN, LOW);
    digitalWrite(LED_YELLOW, LOW);
    digitalWrite(LED_RED, LOW);
    noTone(BUZZER_PIN);

    if (distance < DIST_RED) {
      digitalWrite(LED_RED, HIGH);
      tone(BUZZER_PIN, 1000); 
    } 
    else if (distance < DIST_YELLOW) {
      digitalWrite(LED_YELLOW, HIGH);
    } 
    else {
      digitalWrite(LED_GREEN, HIGH);
    }
  }
}
