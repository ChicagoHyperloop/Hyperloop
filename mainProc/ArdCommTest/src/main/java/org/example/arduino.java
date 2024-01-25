package org.example;

import com.fazecast.jSerialComm.*;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.nio.charset.StandardCharsets;

import java.util.Objects;
import java.util.Scanner;
import java.util.*;

import java.lang.String;

public class arduino {

    private static final int BAUD = 9600;
	private SerialPort sp;

	public arduino(SerialPort sp) {

		this.sp = sp;

        System.out.println("opened COMPORT: " + sp.getDescriptivePortName());

		this.sp.openPort();
        this.sp.setBaudRate(BAUD);

	}

    public int getBytesAvailable() {
        return sp.bytesAvailable();
    }

    public byte[] readBytes(int numBytes) {
        byte[] readBuffer = new byte[numBytes];
        int numRead = sp.readBytes(readBuffer, readBuffer.length);

        return readBuffer;
    }

	public String readString(int numBytes) {
		return new String(this.readBytes(numBytes), StandardCharsets.UTF_8);
	}

	public void writeBytes(byte[] msg) {
		this.sp.writeBytes(msg, msg.length);
	}

    public void write(String msg) {
        this.writeBytes(
                msg.getBytes()
        );
    }

	public SerialPort getSerialPort() {
		return sp;
	}
}
