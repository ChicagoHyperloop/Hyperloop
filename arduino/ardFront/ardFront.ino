//this sketch is a test to blink an LED on an arduino
//this tests if we can upload code from the Rpi to the arduino
//programmed on WSLS(ubuntu) ssh into Rpi and ubuntu ssh

//this program is a modified blink
//the arduino waits for a int input from the rpi
//if the arduino recieves an int input from the rpi it changes
//the delay between blinks to timesec
//it also tests client receive by sending data back to the rpi

// time in seconds

#include <ArduinoJson.h>

int timeSec = 1;

void setup() {

	Serial.begin(9600);
	pinMode(13,OUTPUT);

    Serial.println("READY:");

    // begin Codes
	while (true) {

	    String word = Serial.readString();
        Serial.println(word);


        if (word == "B:;") {

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

    /*

    GETTEMP:;LEDON:;LEDOFF:;

    do {
        read until first semicolon
        do somn with that info

        switch (String) {

            case "Emergency":

                getAlarm();
                if (Alarm) {

                }

            case "GETTEMP":
                ...
                break;


        }

    } while ( repeat if there is shit left)

    */

    /*

    Uint_8 alarm;

    Emergency:alarm;


    */


    /*

    var = array[0]
    var = array[1]

    if (array[0]) {}

    if (array[1]) {}

    */

    String word = Serial.readString();
    Serial.println(word);
/*
    if (word == "GETTEMP:;") {

        Serial.print("TEMPstat: 500:42.1;");

    }
*/
    if(word.indexOf("}") > 0) {


    //char json[] =
      //"{\"sensor\":\"gps\",\"time\":1351824120,\"data\":[48.756080,2.302038]}";

        // Deserialize the JSON document

         StaticJsonDocument<200> doc;

        DeserializationError error = deserializeJson(doc, word);

        // Test if parsing succeeds.
        if (error) {
          Serial.print(F("deserializeJson() failed: "));
          Serial.println(error.f_str());
          return;
        }

        // Fetch values.
        //
        // Most of the time, you can rely on the implicit casts.
        // In other case, you can do doc["time"].as<long>();
        double tempLeft = doc["tempLeft"];
        double tempRight = doc["tempRight"];

        // Print values.

        Serial.println("beeeeeeeeeeeeeeeeeeeeeep");
        Serial.println(tempLeft);
        Serial.println(tempRight);

        delay(100);



    }



}
