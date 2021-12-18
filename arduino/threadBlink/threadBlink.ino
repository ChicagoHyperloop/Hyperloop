//this sketch is a test to fancy blink an LED on an arduino
//this tests if we can thread arduinos on the rpi
//programmed on WSLS(ubuntu) ssh into Rpi and ubuntu ssh

//this program is a modified blink
//there is a fake sensor that will be sending data
//there is a controllable object (2xLEDs)
//the rpi should be able to handle sending and recieving of LED data
//receiving "L:"+some string, will change blink status
//receiving "S:"+some string, will change sensor data status
//full scale test will happen on multiple arduino

// time in seconds
//int timeSec = 1;
int timeMS = 500;

void setup() {

	Serial.begin(9600);
	pinMode(13,OUTPUT);
	Serial.println("setup");

}


//fake sensor data is timeSec*2 which is dumb but o well


// I just hope this fucking works
void loop() {

	//this part handles input data
	//TODO: upgrade to serial Event
	if (Serial.available() > 0) {
		
		String inData = Serial.readString();

		char firstChar = inData.charAt(0);

		if (firstChar == 'L') {

			inData.remove(0,2);
			timeMS = inData.toInt();


		} else if (firstChar == 'S'){

			Serial.println(timeMS);

		} else {

			Serial.println("Shiiiiit");		

		}

	}


	// executes 1 frame of thing
	digitalWrite(13,HIGH);
	timeMS+=50;
	//Serial.print("timeMS: ");
	Serial.println(timeMS);
	delay(timeMS);

	digitalWrite(13,LOW);
	delay(timeMS);

	//Serial.println("one blink past");

}
