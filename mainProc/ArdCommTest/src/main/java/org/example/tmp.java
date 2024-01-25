package org.example;

import com.fazecast.jSerialComm.*;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.util.Objects;
import java.util.Scanner;

// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
// then press Enter. You can now see whitespace characters in your code.
/*
public class Main {

    public static SerialPort ardPort1;

    public static void main(String[] args) throws IOException {


        SerialPort[] allports = SerialPort.getCommPorts();

        for (SerialPort sp : allports) {
            System.out.println(sp.getDescriptivePortName() + " - " + sp.getSystemPortPath());
        }

        ardPort1 = allports[0];    // /dev.cu.usbmodem1101 on Pranav's computer
        ardPort1.openPort();


        InputStream ardin = ardPort1.getInputStream();
        OutputStream ardout = ardPort1.getOutputStream();

        System.out.println("Connection to Arduino 1 established");

        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("Press 1 to start and 0 to stop");
            String comm = scanner.nextLine();
            System.out.println(comm);
            //comm.trim();

            if (Objects.equals(comm, "1")) {
                ardout.write("START\n".getBytes());
                System.out.println("Thing is on");

            } else if (Objects.equals(comm, "0")) {

	       ardout.write("STOP\n".getBytes());
                System.out.println("Thing is off");

            }
        }
    }
}
*/
