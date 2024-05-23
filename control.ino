#include<SoftwareSerial.h>
SoftwareSerial bt(10, 11);
int in1 = 4;
int in2 = 5;
int in3 = 6;
int in4 = 7;

void setup() {
  // put your setup code here, to run once:
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  bt.begin(9600);
  Serial.begin(9600);

}

void loop() {
  if(bt.available()>0){
    char data = bt.read();
    switch (data){
      case '0':
        analogWrite(in1, 0);
        analogWrite(in2, 0);
        analogWrite(in3, 0);
        analogWrite(in4, 0);
        break;
      case '1':
        analogWrite(in1, 255);
        analogWrite(in2, 0);
        analogWrite(in3, 0);
        analogWrite(in4, 50);
        break;
      case '2':
        analogWrite(in1, 50);
        analogWrite(in2, 0);
        analogWrite(in3, 0);
        analogWrite(in4, 255);
        break;
      case '3':
        analogWrite(in1, 255);
        analogWrite(in2, 0);
        analogWrite(in3, 0);
        analogWrite(in4, 255);
        break;
      case '4':
        analogWrite(in1, 0);
        analogWrite(in2, 255);
        analogWrite(in3, 50);
        analogWrite(in4, 0);
        break;
      case '5':
        analogWrite(in1, 0);
        analogWrite(in2, 50);
        analogWrite(in3, 255);
        analogWrite(in4, 0);
        break;
      case '6':
        analogWrite(in1, 0);
        analogWrite(in2, 255);
        analogWrite(in3, 255);
        analogWrite(in4, 0);
        break; 
    }
  }
}
