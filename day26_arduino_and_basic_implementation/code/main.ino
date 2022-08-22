//https://wokwi.com/projects/340585047953244755
#include <Servo.h>
#define TRIG 7
#define ECHO 8

// v ultrasonic = 340m/s
// s = (340m/s*t)/2;

long t;
float v = 0.034;

Servo door;

void setup() {
  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);
  Serial.begin(9600);
  door.attach(3);
  door.write(0);
}

void loop() {
  distance();
}

void servo(int x){
  door.write(x);
}

void distance(){
  digitalWrite(TRIG, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG, LOW);

  t = pulseIn(ECHO,HIGH);

  double s=v*t/2;

  Serial.print("Jarak: ");Serial.println(s);

  if(s<10) servo(0);
  else servo(180);
}
