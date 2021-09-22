#define TC_PIN A0          // set to ADC pin used
#define AREF 5.0           // set to AREF, typically board voltage like 3.3 or 5.0
#define ADC_RESOLUTION 10  // set to ADC bit resolution, 10 is default

float reading, voltage, temperature;

float get_voltage(int raw_adc) {
  return raw_adc * (AREF / (pow(2, ADC_RESOLUTION)-1));  
}

float get_temperature(float voltage) {
  return (voltage - 1.25) / 0.005;
}

void setup() {
  Serial.begin(9600);
}

void loop() {
  reading = analogRead(TC_PIN);
  voltage = get_voltage(reading);
  temperature = get_temperature(voltage);
//  Serial.print("Temperature = ");
  Serial.println(voltage);
//  Serial.println(" C");
//  Serial.print("Voltage = ");
//  Serial.print(voltage);
//  Serial.println(" V");
  delay(100);
}
