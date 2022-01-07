//this sketch is a test to blink an LED on an arduino
//this tests if we can upload code from the Rpi to the arduino
//programmed on WSLS(ubuntu) ssh into Rpi and ubuntu ssh

//this program is a modified blink
//the arduino waits for a int input from the rpi
//if the arduino recieves an int input from the rpi it changes
//the delay between blinks to timesec
//it also tests client receive by sending data back to the rpi

// time in seconds
int timeSec = 1;

void setup() {

	Serial.begin(9600);
	pinMode(13,OUTPUT);

    // begin Codes
	while (true) {

	    String word = Serial.readString();
        Serial.println(word);

        if (word == "B:") {

            digitalWrite(13, HIGH);
            Serial.println("LED:ON");
            delay(500);
            digitalWrite(13, LOW);
            Serial.println("LED:OFF");
            delay(500);
            digitalWrite(13, HIGH);
            Serial.println("LED:ON");
            delay(500);
            digitalWrite(13, LOW);
            Serial.println("LED:OFF");

            break;

        }

	}
}

void loop() {

    String word = Serial.readString();
    Serial.println(word);

    if (word == "O:") {

        digitalWrite(13, HIGH);
        Serial.println("LED:ON");

    } else if (word == "F:") {

        digitalWrite(13, LOW);
        Serial.println("LED:OFF");

    }

    delay(100);
/*


	if (Serial.available() > 0) {

		timeSec = Serial.parseInt();
		Serial.println("delay changed: " + timeSec);
	
	}
	
	digitalWrite(13,HIGH);
	delay(1000 * timeSec);

	digitalWrite(13,LOW);
	delay(1000 * timeSec);

	Serial.println("one blink past");
*/
}
