void setup() {
  // Start serial and arm motor
  Serial.begin(115200);
  pinMode(10, OUTPUT);
  motor.attach(10, 1024, 2047);
  //motor.writeMicroseconds(1024);
  analogWrite(10, 0);
  delay(3000);

  //motor.writeMicroseconds(1024);
  analogWrite(10, 0);
}

void loop() {
  // put your main code here, to run repeatedly:

}
