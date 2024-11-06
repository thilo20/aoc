// package main;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;

/** solve https://adventofcode.com/2022/day/1 */
public class Day1c {

    public static List<String> readInput(String filename) {
        Path path = Paths.get(filename);
        try {
            return Files.readAllLines(path);
        } catch (IOException e) {
            e.printStackTrace();
            return List.of();
        }
    }

    public static void solvePart1(List<String> lines) {
        int calories = 0;
        int maxCalories = 0;

        for (String currentLine : lines) {
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
    }

    public static void main(String[] args) {
        if (args.length > 0) {
            solvePart1(readInput(args[0]));
        }
    }
}