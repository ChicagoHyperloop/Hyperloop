/**
 * PiComm.h - Library for communicating with Raspberry Pi for Pod control
 * Chicago Hyperloop, 2022
 **/
#include "Arduino.h"
#include "PiComm.h"

PiComm::PiComm(int baud) {
  Serial.begin(baud);

  // Read in commands
  if (Serial.available() > 0) {
    std::string raw = Serial.readString();
    std::string command = raw.substr(0, s.find(:));
    param 1 2 3

    switch(command) {
      case "GETTEMP":
        getTemp(param1, param 2, param3);
        break;
      case "TEMPMAX":
        break;
      case "SETPID":
        break;
      case "SETTARGET":
        break;
      case "GETHFX":
        break;
      case "RELAYFL":
        break;
      case "RELAYFR":
        break;
      case "RELAYBL":
        break;
      case "RELAYBR":
        break;
      case "SETGREEN":
        break;
      case "SETRED":
        break;
      case "ESTOP":
        break;
      case "BRAKES":
        break;
      case: "LIVEMYCHILD":
        break;
    }
  }
}

PiComm::sendCommand(
  std::string command,
  std::string param1,
  std::string param2,
  std::string param3
) {
  std:string formedCommand = command + ":"

  // Form command string with multiple parameters
  param1 != "" && formedCommand += param1 + ":";
  param2 != "" && formedCommand += param2 + ":";
  param3 != "" && formedCommand += param3;

  formedCommand += ";";

  Serial.write(formedCommand);
}

PiComm::sendTemp(int temp1, int temp2) {
  sendCommand("TEMPstat", std::to_string(temp1), std::to_string(temp2), "");
}

PiComm::sendRPM(int rpm1, int rpm2) {
  sendCommand("SPEEDstat", std::to_string(rpm1), std::to_string(rpm2), "");
}

PiComm::sendEmergencyStop(std::string reason) {
  sendCommand("ESTOP", reason, "", "");
}

PiComm::sendKeepAlive() {
  sendCommand("LIVEMYCHILD", "", "", "");
}