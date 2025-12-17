#include <Servo.h>
#include <IRremote.hpp>

#define IR_PIN 9

const int TOP_R = A3, TOP_G = A1, TOP_B = A2;
const int BOT_R = 2, BOT_G = 4, BOT_B = 3;
const int TRIG_PIN = 13; 
const int ECHO_PIN = 12; 
const int LED_RED = 7;
const int LED_YELLOW = 6;
const int LED_GREEN = 5; 
const int BUZZER_PIN = 11;
const int SIREN_BUZZER_PIN = 8;
const int MOISTURE_PIN = A0;
const int SERVO_PIN = 10;

unsigned long BTN_4     = 0xEB14BF00;
unsigned long BTN_6     = 0xE916BF00;
unsigned long BTN_LIGHT = 0xEF10BF00;
unsigned long BTN_SIREN = 0x718BF00; 

bool blinkTop = false, blinkBot = false, headlights = false;
bool sirenState = false;

unsigned long lastBlink = 0;
bool blinkState = false;
unsigned long lastIRTime = 0;

const int DIST_RED = 80; 
const int DIST_YELLOW = 100; 
const float MIN_DISTANCE_CM = 15.0; 

const int MOISTURE_THRESHOLD = 512;

Servo myServo;

void setRGB(int rPin, int gPin, int bPin, int r, int g, int b) {
  analogWrite(rPin, r); analogWrite(gPin, g); analogWrite(bPin, b);
}

void updateFrontLEDs() {
  if (millis() - lastBlink > 500) {
    lastBlink = millis();
    blinkState = !blinkState;

    if (blinkTop) setRGB(TOP_R, TOP_G, TOP_B, blinkState ? 255 : 0, blinkState ? 255 : 0, 0);
    else if (!headlights) setRGB(TOP_R, TOP_G, TOP_B, 0,0,0);

    if (blinkBot) setRGB(BOT_R, BOT_G, BOT_B, blinkState ? 255 : 0, blinkState ? 255 : 0, 0);
    else if (!headlights) setRGB(BOT_R, BOT_G, BOT_B, 0,0,0);
  }

  if (headlights) {
    setRGB(TOP_R, TOP_G, TOP_B, 255,255,255);
    setRGB(BOT_R, BOT_G, BOT_B, 255,255,255);
  }
}


unsigned long lastUltrasonic = 0;
const unsigned long ULTRASONIC_INTERVAL = 50;

void updateObstacleSystem() {
  if (millis() - lastUltrasonic < ULTRASONIC_INTERVAL) return;
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

  Serial.print("Distance: ");
  Serial.println(distance);

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
// ------------------------------------------------


void updateMoistureSystem() {
  int m = analogRead(MOISTURE_PIN);
  if (m > MOISTURE_THRESHOLD) myServo.write(0);
  else myServo.write(90);
}

void setup() {
  Serial.begin(9600);
  IrReceiver.begin(IR_PIN);

  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);

  pinMode(LED_GREEN, OUTPUT);
  pinMode(LED_YELLOW, OUTPUT);
  pinMode(LED_RED, OUTPUT);

  pinMode(BUZZER_PIN, OUTPUT);
  pinMode(SIREN_BUZZER_PIN, OUTPUT);

  myServo.attach(SERVO_PIN);
  myServo.write(90);

  Serial.println("System Initialized.");
}

void loop() {
  Serial.println("Loop is running..."); 
  
  if (IrReceiver.decode()) {
    unsigned long raw = IrReceiver.decodedIRData.decodedRawData;

    if (millis() - lastIRTime > 200) {
      if (raw == BTN_4) { blinkTop=true; blinkBot=false; headlights=false; }
      else if (raw == BTN_6) { blinkTop=false; blinkBot=true; headlights=false; }
      else if (raw == BTN_LIGHT) { headlights=!headlights; blinkTop=false; blinkBot=false; }
      else if (raw == BTN_SIREN) { sirenState = !sirenState; }

      lastIRTime = millis();
    }

    IrReceiver.resume();
  }

  updateFrontLEDs();
  updateObstacleSystem();
  updateMoistureSystem();

  if (sirenState) tone(SIREN_BUZZER_PIN, 1500);
  else noTone(SIREN_BUZZER_PIN);
}
