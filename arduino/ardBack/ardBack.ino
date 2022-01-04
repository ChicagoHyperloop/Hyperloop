//this sketch is a test to fancy blink an LED on an arduino
//this is part of the request based model client side
//programmed on WSLS(ubuntu) ssh into Rpi3B and ubuntu ssh

//this program is a modified blink
//there is a fake sensor that will be sending data
//there is a controllable object (2xLEDs)

const int TIMEOUT = 3000;

unsigned long lastComTime = 0;
unsigned long loopStart = 0;
unsigned long loopEnd = 0; 
unsigned long lastLEDChange = 0;

int timeMS = 500;
int LEDState = LOW;

void setup() {

	// hardware setup
	pinMode(13,OUTPUT);

	//Communications setup
	Serial.begin(9600);

	// wait for Serial port to connect
	while (!Serial) {
		; // this was there to begin with in the code I copypasta
	}

	while (true) { // wait for Begin command
		
		if (Serial.available > 0 && Serial.read() == "B:") {

			Serial.println("Begun:");
			break;
		
		}
		
	}

}


void EStop(){

	while (true) {
		
		Serial.println("Stopped:");
		delay(10000);
	
	}

}

// I just hope this fucking works
void loop() {

	loopStart = millis();

	if ((millis() - lastComTime) > TIMEOUT) {

		//send Emergency signal
		Serial.println("ES:");
		EStop();

	}

	// recieved Command
	if (Serial.available() > 0) {
		
		lastComTime = millis();
		
		String inData = Serial.readString();

		int colonIndex = indexOf(':',0);
		String prepend = inData.subString(0,colonIndex - 1);
		String data = inData.subString(colonIndex + 1);

		if (prepend == "ES") {

			EStop();

		} else if (prepend == "S") { // Status update

			// this is supposed to be command for status update
			// will include temp and speed
			// as well as any other regularly sending sensor data

		} else if (prepend == "L") { // do somn with LEDS

			timeMS = int(data);
			
		} else {
			// arduino doesnt understand now die
			Serial.println("ES:");
			EStop();
		}


	}

	// actually do hardware stuff now
	// executes 1 frame of thing

	if (millis() - lastLEDChange > timeMS) {

		LEDState = !LEDState;
		digitalWrite(13,LEDState);
		timeMS += 50;
	}

	// TODO: we can find loop times with this, if its too low the arduino commit suicide
	loopEnd = millis();

}
