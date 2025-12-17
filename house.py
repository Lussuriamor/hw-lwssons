#include <Servo.h>


const int PIR_PIN = 12;
const int LED_GREEN = 5;
const int LED_RED = 6;


const int TMP_LEFT = A2;
const int TMP_RIGHT = A3;
const int TMP_LEFT_LED = 4;
const int TEMP_BUZZER = 11;


const int GAS_PIN = A4;
const int GAS_BUZZER = 7;


const int SOIL_PIN = A1;
const int SOIL_LED = 2;
const int SOIL_BUZZER = 3;


const int MOTOR_RELAY = 10; 


const int PHOTO_PIN = A0;
const int LAMP_PIN = 9;
const int SERVO_PIN = 8;


const int SERVO2_PIN = 13;

Servo myServo;
Servo myServo2;

float getTemperature(int pin) {
  int raw = analogRead(pin);
  float voltage = raw * (5.0 / 1023.0);
  return (voltage - 0.5) * 100.0;
}

void setup() {
  Serial.begin(9600);

  pinMode(LED_GREEN, OUTPUT);
  pinMode(LED_RED, OUTPUT);
  pinMode(TMP_LEFT_LED, OUTPUT);

  pinMode(GAS_BUZZER, OUTPUT);
  pinMode(TEMP_BUZZER, OUTPUT);

  pinMode(SOIL_LED, OUTPUT);
  pinMode(SOIL_BUZZER, OUTPUT);

  pinMode(MOTOR_RELAY, OUTPUT);

  pinMode(LAMP_PIN, OUTPUT);

  myServo.attach(SERVO_PIN);
  myServo2.attach(SERVO2_PIN);

  myServo.write(0);
  myServo2.write(0);

  digitalWrite(LED_GREEN, HIGH);
  digitalWrite(LED_RED, LOW);
}

void loop() {


  if (digitalRead(PIR_PIN)) {
    digitalWrite(LED_GREEN, LOW);
    digitalWrite(LED_RED, HIGH);
    delay(150);
    digitalWrite(LED_RED, LOW);
    delay(150);
  } else {
    digitalWrite(LED_RED, LOW);
    digitalWrite(LED_GREEN, HIGH);
  }

  
  int gasValue = analogRead(GAS_PIN);
  Serial.print("Gas: "); Serial.println(gasValue);

  if (gasValue > 300) {
    digitalWrite(GAS_BUZZER, HIGH);
  } else {
    digitalWrite(GAS_BUZZER, LOW);
  }

 
  float leftTemp = getTemperature(TMP_LEFT);
  Serial.print("Left TEMP: "); Serial.println(leftTemp);

  
  if (leftTemp > 90) {
    digitalWrite(TMP_LEFT_LED, HIGH);
    delay(100);
    digitalWrite(TMP_LEFT_LED, LOW);
    delay(100);
  } else {
    digitalWrite(TMP_LEFT_LED, LOW);
  }

  
  if (leftTemp > 80) {
    digitalWrite(TEMP_BUZZER, HIGH);
  } else {
    digitalWrite(TEMP_BUZZER, LOW);
  }


  float rightTemp = getTemperature(TMP_RIGHT);
  Serial.print("Right TEMP: "); Serial.println(rightTemp);

  if (rightTemp > 50) {
  	for (int pos = 0; pos <= 180; pos++) {
    	myServo2.write(pos);
    	delay(5);
  	}
  	for (int pos = 180; pos >= 0; pos--) {
    	myServo2.write(pos);
    	delay(5);
  	}
	} else {
  	  myServo2.write(0);
	}


  int soil = analogRead(SOIL_PIN);
  Serial.print("Soil: "); Serial.println(soil);

  if (soil > 600) {
    digitalWrite(SOIL_LED, HIGH);
    digitalWrite(SOIL_BUZZER, HIGH);
  } else {
    digitalWrite(SOIL_LED, LOW);
    digitalWrite(SOIL_BUZZER, LOW);
  }

  
  int lightValue = analogRead(PHOTO_PIN);

  if (lightValue > 512) {
    digitalWrite(LAMP_PIN, LOW);
    myServo.write(90);
  } else {
    digitalWrite(LAMP_PIN, HIGH);
    myServo.write(0);
  }

  delay(20);
}