/**
 * Chicago Hyperloop
 *
 * RPM Library
 * @attr https://forum.arduino.cc/u/cattledog/summary
 * Spring 2022
 **/

volatile byte count = 0;
byte numCount = 8;

volatile unsigned long startTime;
volatile unsigned long endTime;
unsigned long copy_startTime;
unsigned long copy_endTime;

volatile boolean finishCount = false;
float period;

unsigned int rpm = 0;

/**
 * Setup
 **/
void setup() {
  Serial.begin(115200);

  // Interrupt
  attachInterrupt(digitalPinToInterrupt(3), isrCount, FALLING);
}

/**
 * Loop
 **/
void loop() {
  if (finishCount == true) {
    finishCount = false;

    // Disable interrupts, make protected copy of time values
    noInterrupts();
    copy_startTime = startTime;
    copy_endTime = endTime;
    count = 0;
    interrupts();

    // Micros to millis
    period = (copy_endTime - copy_startTime) / 1000.0;

    // Three count per revolution
    rpm = numCount * 20.0 * (1000.0 / period);

    // Monitor output
    Serial.print("RPM = ");
    Serial.println(rpm);
  }
}

/**
 * Counts the interrupt
 **/
void isrCount() {
  if (count == 0) {
    startTime = micros();
  }

  if (count == numCount) {
    endTime = micros();
    finishCount = true;
  }

  count++;
}
