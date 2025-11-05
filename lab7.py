#include <Wire.h>
#include <LiquidCrystal_I2C.h>

const int tempPin = A1;      
const int ldrPin = A0;       
const int potPin = A2;       
const int ledPin = 6;        
const int buzzerPin = 7;     

float tempThreshold = 30.0;   
int lightThreshold = 300;     

LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
  pinMode(buzzerPin, OUTPUT);
  
  lcd.init();            
  lcd.backlight();       
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Smart Monitor");
  delay(1000);
}

void loop() {
  int potValue = analogRead(potPin);

  tempThreshold = map(potValue, 0, 1023, 30, 60);    
  lightThreshold = map(potValue, 0, 1023, 300, 600); 

  int tempValue = analogRead(tempPin);
  float voltage = tempValue * (5.0 / 1023.0);
  float temperatureC = voltage * 100.0;  

  int lightValue = analogRead(ldrPin);

  Serial.print("Температура: ");
  Serial.print(temperatureC);
  Serial.print(" °C | Свет: ");
  Serial.print(lightValue);
  Serial.print(" | Потенциометр: ");
  Serial.print(potValue);
  Serial.print(" | Порог T: ");
  Serial.print(tempThreshold);
  Serial.print(" | Порог L: ");
  Serial.println(lightThreshold);

  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("T:");
  lcd.print(temperatureC, 1);
  lcd.print((char)223); 
  lcd.print("C L:");
  lcd.print(lightValue);

  lcd.setCursor(0, 1);
  lcd.print("ThrT:");
  lcd.print(tempThreshold, 0);
  lcd.print(" ThrL:");
  lcd.print(lightThreshold);

  if (temperatureC > tempThreshold || lightValue < lightThreshold) {
    digitalWrite(ledPin, HIGH);
    digitalWrite(buzzerPin, HIGH);
  } else {
    digitalWrite(ledPin, LOW);
    digitalWrite(buzzerPin, LOW);
  }

  delay(500);
}
