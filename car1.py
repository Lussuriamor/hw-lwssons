#include <IRremote.hpp>

#define IR_PIN 3   

const int M1_IN1 = 8;
const int M1_IN2 = 9;

const int M2_IN3 = 10;
const int M2_IN4 = 11;

const int M3_IN1 = 4;
const int M3_IN2 = 5;

const int M4_IN3 = 6;
const int M4_IN4 = 7;

const int ENA_M1_M2 = 12; 
const int ENA_M3 = 2;
const int ENA_M4 = 13;

unsigned long BTN_FORWARD = 0x11;  
unsigned long BTN_BACK    = 0x19;  
unsigned long BTN_STOP    = 0x15;  

void setup() {

  Serial.begin(9600);
  IrReceiver.begin(IR_PIN);

  pinMode(M1_IN1, OUTPUT);
  pinMode(M1_IN2, OUTPUT);
  pinMode(M2_IN3, OUTPUT);
  pinMode(M2_IN4, OUTPUT);
  pinMode(M3_IN1, OUTPUT);
  pinMode(M3_IN2, OUTPUT);
  pinMode(M4_IN3, OUTPUT);
  pinMode(M4_IN4, OUTPUT);

  pinMode(ENA_M1_M2, OUTPUT);
  pinMode(ENA_M3, OUTPUT);
  pinMode(ENA_M4, OUTPUT);

  digitalWrite(ENA_M1_M2, HIGH);
  digitalWrite(ENA_M3, HIGH);
  digitalWrite(ENA_M4, HIGH);

  stopAllMotors();
}


void setMotorDirection(int inPin1, int inPin2, bool forward) {
  if (forward) {
    digitalWrite(inPin1, HIGH);
    digitalWrite(inPin2, LOW);
  } else {
    digitalWrite(inPin1, LOW);
    digitalWrite(inPin2, HIGH);
  }
}

void allForward() {
  setMotorDirection(M1_IN1, M1_IN2, true);
  setMotorDirection(M2_IN3, M2_IN4, true);
  setMotorDirection(M3_IN1, M3_IN2, true);
  setMotorDirection(M4_IN3, M4_IN4, true);
}

void allBackward() {
  setMotorDirection(M1_IN1, M1_IN2, false);
  setMotorDirection(M2_IN3, M2_IN4, false);
  setMotorDirection(M3_IN1, M3_IN2, false);
  setMotorDirection(M4_IN3, M4_IN4, false);
}

void stopAllMotors() {
  digitalWrite(M1_IN1, LOW);
  digitalWrite(M1_IN2, LOW);
  digitalWrite(M2_IN3, LOW);
  digitalWrite(M2_IN4, LOW);
  digitalWrite(M3_IN1, LOW);
  digitalWrite(M3_IN2, LOW);
  digitalWrite(M4_IN3, LOW);
  digitalWrite(M4_IN4, LOW);
}


void loop() {

  if (IrReceiver.decode()) {
    unsigned long code = IrReceiver.decodedIRData.command;

    Serial.print("CODE: ");
    Serial.println(code, HEX);

    if (code == BTN_FORWARD) {
      allForward();
    }
    else if (code == BTN_BACK) {
      allBackward();
    }
    else if (code == BTN_STOP) {
      stopAllMotors();
    }

    IrReceiver.resume();
  }
}
