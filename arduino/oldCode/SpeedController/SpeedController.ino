/**
 * Chicago Hyperloop
 * Fall 2021
 * Hyperloop DC motor speed calculation
 */

#include <Servo.h>
#define TC_PIN A0
#define LOWEST_OPERATING_SPEED 26

#define speedControlPin 9
Servo ESC;

volatile float revolutions;
volatile float prevRevolutions;
volatile float currRevolutions;

float rpm;
float speed;
int desiredSpeed;
int outputESC;
boolean sensingRPM;

int rpmErrorCount;

unsigned long currTime;
unsigned long prevTime;
unsigned long prevAdjustTime;

/**
 * setup
 * Program entry point
 * Initialize variables and begin serial output
 */
void setup() {
    // Begin speed output, desired speed input
  Serial.begin(115200);
  attachInterrupt(0, revolutionSensed, RISING);
  ESC.attach(speedControlPin, 1000, 2000);
  ESC.write(0);

  revolutions = 0;
  prevRevolutions = 0;
  sensingRPM = false;
  rpm = 0;
  currTime = 0;
  prevTime = 0;
  rpmErrorCount = 0;
  outputESC = LOWEST_OPERATING_SPEED;

  adjustMotorSpeed();
}

/**
 * loop
 * Main program loop
 * Calculate speed from given hall effect sensor pulses
 */
void loop() {
  // Get current time and revolutions prior to calculation to prevent
  // changes between calculation steps
  currTime = millis();
  
  // Only calculate when exceeding 100 rotations and 500 ms have passed
  if (revolutions >= 80 && (currTime - prevTime) > 400) {
    float newRpm = ((revolutions) / (currTime - prevTime));

    // 500 rpm variance to account for rotations missed between loop cycles
    if (newRpm > rpm + 500 && rpmErrorCount <= 3) {
      rpmErrorCount++;
      return;
    }

    rpm = newRpm;
    outputMotorData(revolutions, rpm);

    prevTime = millis();
    revolutions = 0;
    rpmErrorCount = 0;

    adjustMotorSpeed();
    sensingRPM = true;
  }

  // Handle speed increase until hall effect sensors work
  if (!sensingRPM && (currTime - prevAdjustTime) > 300) {
    adjustMotorSpeed();
    prevAdjustTime = millis();
  }

  // After .5 seconds of no movement, trigger initial motor adjustment
  if (revolutions == prevRevolutions && currTime - prevAdjustTime > 500) {
    sensingRPM = false;
    prevAdjustTime = millis();
  }

  // Take and set desired speed inputs
  acceptMotorDesiredSpeed();

  prevRevolutions = revolutions;
}

/**
 * revolutionSensed
 * Called when hall effect sensor gets activated
 */
void revolutionSensed() {
  revolutions++;
}

/**
 * outputMotorData
 * @param rev
 * @param rpm
 * Outputs motor data to serial connection
 */
void outputMotorData(int rev, float rpm) {
  // Calculate speed based on circumference
  speed = rpm * 0.24378758991 * 3600;

  // Ouput data:
  Serial.print("Revolutions: ");
  Serial.print(revolutions);
  Serial.print(" RPM: ");
  Serial.print(rpm * 60000, DEC);
  Serial.print(" Speed: ");
  Serial.print(speed, DEC);
  Serial.println(" kph");
}

/**
 * acceptMotorDesiredSpeed
 * Accepts user input from serial to set desired speed
 */
void acceptMotorDesiredSpeed() {
  
  // Input connection successful
  if (Serial.available() > 0) {
    int requestedSpeed = Serial.parseInt();

    // Validate speed (max KPH)
    if (requestedSpeed > 0 && requestedSpeed < 200) {
      desiredSpeed = requestedSpeed;
      Serial.println("------------ DESIRED SPEED ACCEPTED: " + String(desiredSpeed) + " ------------");
    } else if (requestedSpeed == -1) {
      ESC.write(0);
      desiredSpeed = 0;
      outputESC = LOWEST_OPERATING_SPEED;
      Serial.println("------------ MOTOR STOP RECEIVED ------------");
    } else if (requestedSpeed != 0) {
      Serial.println("------------ DESIRED SPEED INVALID: " + String(requestedSpeed) + " ------------");
    }
  }
}

/**
 * adjustMotorSpeed
 * Changes motor speed dependent on desired speed and current ESC value
 */
void adjustMotorSpeed() {
  // No change if stop desired
  if (desiredSpeed == 0) {
    return;
  }
  
  // Current speed too low
  if (desiredSpeed > speed + 4) {
    if (outputESC < 180) {
      outputESC++;
    }
  // Current speed too high
  } else if (desiredSpeed < speed - 4) {
    // Smallest operating level
    if (outputESC > LOWEST_OPERATING_SPEED) {
      outputESC--;
    }
  }

  ESC.write(outputESC);
}
