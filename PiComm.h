/**
 * PiComm.h - Library for communicating with Raspberry Pi for Pod control
 * Chicago Hyperloop, 2022
 **/
#ifndef PiComm_h
#define PiComm_h

#include "Arduino.h"

class PiComm {
  public:
    PiComm(int baud);

    // Temp sensors
    void getTemp();
    void sendTemp(int temp1, int temp2);
    void getMaxTemp();

    // ESC Control
    void getPID();
    void getTarget();

    // HFX sensors
    void getRPM();
    void sendRPM();

    // Power/Relays
    void getActivateMotorRelay();
    void getDeactivateMotorRelay();

    // Indicators
    void getActivateGreenIndicator();
    void getDeactivateGreenIndicator();
    void getActivateRedIndicator();
    void getDeactivateRedIndicator();

    // E-Stop
    void sendEmergencyStop();
    void getReleaseEmergencyStop();

    // Brakes
    void getApplyBrakes();
    void getReleaseBrakes();

    // Keep Alive
    void getKeepAlive();
    void sendKeepAlive();
  private:
    void sendCommand(std::string command, std::string param1, std::string param2, std::string param3);
}

#endif