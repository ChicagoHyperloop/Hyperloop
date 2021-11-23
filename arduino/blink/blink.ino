//this sketch is a test to blink an LED on an arduino
//this tests if we can upload code from the Rpi to the arduino
//programmed on WSLS ubuntu ssh into Rpi and ubuntu ssh

void setup() {

	Serial.begin(9600);
	pinMode(13,OUTPUT);
	Serial.println("setup");

}


void loop() {

	
	digitalWrite(13,HIGH);
	delay(1000);
	digitalWrite(13,LOW);
	delay(1000);
	Serial.println("one blink past");

}
