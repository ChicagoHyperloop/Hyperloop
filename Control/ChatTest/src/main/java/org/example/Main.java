package org.example;

import java.net.*;
import java.util.Enumeration;

public class Main {

    public static void main(String[] args) {
        int clients = 0;
        System.out.println("Welcome to HLChat Server Edition");
        System.out.println("Using port 5555");

        try {


            Server server = new Server(data -> {
                System.out.println(data);
            });


        } catch (Exception e) {
            e.printStackTrace();
        }


    }
}