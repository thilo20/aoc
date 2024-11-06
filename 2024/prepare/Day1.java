// package main;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

/** solve https://adventofcode.com/2022/day/1 */
public class Day1 {

    public static void solvePart1(String filename) {
        int calories = 0;
        int maxCalories = 0;

        try (BufferedReader reader = new BufferedReader(new FileReader(filename))) {
            String currentLine;
            while ((currentLine = reader.readLine()) != null) {

                if (currentLine.length() > 0) {
                    calories += Integer.parseInt(currentLine);
                } else {
                    if (calories > maxCalories) {
                        maxCalories = calories;
                    }
                    calories = 0;
                }
            }
            System.out.println(maxCalories);

            reader.close();
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        if (args.length > 0) {
            solvePart1(args[0]);
        }
    }
}