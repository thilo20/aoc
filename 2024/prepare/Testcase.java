// package main;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class Testcase {

    @Test
    public void whenReadWithBufferedReader_thenCorrect()
            throws IOException {
        String expected_value = "Hello, world!";
        String file = "prepare/fileTest.txt";

        BufferedReader reader = new BufferedReader(new FileReader(file));
        String currentLine = reader.readLine();
        reader.close();

        assertEquals("File content mismatch!", expected_value, currentLine);
    }

    public static void main(String[] args) {
        System.out.println("Hi AOC 2024 in java!");
    }
}