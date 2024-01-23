

void setup() {
  Serial.begin(9600);  // Initialize Serial communication
  pinMode(13, OUTPUT);  // Set Pin 13 as an output
  Serial.flush();
}

void loop() {
  if (Serial.available() > 0) {  // Check if data is available to read
    String receivedString = Serial.readStringUntil('\n');  // Read the incoming data until a newline character is received
    ///receivedString.trim();
    
    
    if (receivedString == "START") {  // Check if the received string is "START"
      digitalWrite(13, HIGH);  // Turn on Pin 13
      
    } else if (receivedString == "STOP") {
      digitalWrite(13, LOW);  // Turn off Pin 13
    }
  }
  
  // Add any other code you want to run in the loop here
}

