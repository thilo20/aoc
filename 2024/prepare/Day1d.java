// package main;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;
import java.util.stream.Collectors;

/** solve https://adventofcode.com/2022/day/1 */
public class Day1d {

    public static List<String> readInput(String filename) {
        Path path = Paths.get(filename);
        try {
            return Files.readAllLines(path);
        } catch (IOException e) {
            // e.printStackTrace();
            System.err.println(e);
            return List.of();
        }
    }

    public static Integer tryParse(String text) {
        try {
            return Integer.parseInt(text);
        } catch (NumberFormatException e) {
            return null;
        }
    }

    public static int solvePart1Strings(List<String> lines) {
        return solvePart1(
                lines.stream().map(Day1d::tryParse)
                        .collect(Collectors.toList()));
    }

    public static int solvePart1(List<Integer> numbers) {
        int calories = 0;
        int maxCalories = 0;

        for (Integer num : numbers) {
            if (num != null) {
                calories += num;
            } else {
                calories = 0;
            }
            if (calories > maxCalories) {
                maxCalories = calories;
            }
        }
        System.out.println(maxCalories);
        return maxCalories;
    }

    public static void main(String[] args) {
        if (args.length > 0) {
            solvePart1Strings(readInput(args[0]));
        }
    }
}