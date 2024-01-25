// jSerialComm read keyboard and transmit to COM port - read response

// compile and run commands - note that jSerialComm-1.3.11.jar should be in same directory as .java file
// javac -cp F:\Programming\JAVA\JSerialComm\jSerialComm-1.3.11.jar;.  SimpleTerminal.java
// java -cp F:\Programming\JAVA\JSerialComm\jSerialComm-1.3.11.jar;.  SimpleTerminal
package org.example;

import com.fazecast.jSerialComm.*;

import java.util.*;

public class Main {
    public static void main(String[] args) {

        Scanner console = new Scanner(System.in);
        System.out.println("List COM ports");
        SerialPort comPorts[] = SerialPort.getCommPorts();

        arduino[] ards = new arduino[comPorts.length];

        for (int i = 0; i < comPorts.length; i++) {
            ards[i] = new arduino(comPorts[i]);

            try {
                while (true) {
                    // if keyboard token entered read it
                    if (System.in.available() > 0) {
                        ards[i].write(console.nextLine() + "\n");
                    }
                    // read serial port  and display data
                    int byteCount = ards[i].getBytesAvailable();
                    String inputMSG = ards[i].readString(byteCount);
                    System.out.print(inputMSG);

                }
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }
}