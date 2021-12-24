/**
 * Chicago Hyperloop
 * 09/22/2021
 * DC Motor ESC Contoller
 */

#include <Servo.h>

#define speedControlPin 9
Servo ESC;

int speed = 0;

/**
 * Setup code
 * Run once
 */
void setup() {
  // Arm ESC
  ESC.attach(speedControlPin, 1000, 2000);

  // Attach serial outputs
  Serial.begin(9600);
  while (!Serial);
  Serial.println("Speed 0 to 180");
}

/**
 * Loop code
 * Repeat
 */
void loop() {
  // Connection successful
  if (Serial.available() > 0) {
    int newSpeed = Serial.parseInt();
    if (newSpeed != 0 && newSpeed != -1) {
      speed = newSpeed;
    } else if (newSpeed == -1) {
      speed = 0;
    }
  }

  // Set speed (1-byte restriction)
  if (speed >= -180 && speed <= 180) {
    ESC.write(speed);
    Serial.println(speed);
  }
}
