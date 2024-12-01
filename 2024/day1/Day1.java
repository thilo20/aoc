// package day1;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

/** solve https://adventofcode.com/2024/day/1 */
public class Day1 {

    public static List<String> readInput(String filename) {
        Path path = Paths.get(filename);
        try {
            return Files.readAllLines(path);
        } catch (IOException e) {
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

    public static List<Integer> convertLinesToNumbers(List<String> lines) {
        return lines.stream().map(Day1d::tryParse)
                .collect(Collectors.toList());
    }

    public static int solvePart1(List<String> lines) {
        int total = 0;
        List<Integer> left = new ArrayList<>();
        List<Integer> right = new ArrayList<>();

        for (String line : lines) {
            String[] parts = line.split("   ", 0);
            left.add(Integer.valueOf(parts[0]));
            right.add(Integer.valueOf(parts[1]));
        }

        Collections.sort(left);
        Collections.sort(right);

        for (int i = 0; i < left.size(); i++) {
            total += Math.abs(left.get(i) - right.get(i));
        }
        System.out.println("part1: " + total);
        return total;
    }

    public static int solvePart2(List<String> lines) {
        int total = 0;
        List<Integer> left = new ArrayList<>();
        Map<Integer, Integer> right = new HashMap<>();

        for (String line : lines) {
            String[] parts = line.split("   ", 0);
            left.add(Integer.valueOf(parts[0]));

            Integer val = Integer.valueOf(parts[1]);
            Integer count = right.get(val);
            if (count == null) {
                right.put(val, 1);
            } else {
                right.put(val, count + 1);
            }
        }

        for (Integer val : left) {
            total += val * right.getOrDefault(val, 0);
        }
        System.out.println("part2: " + total);
        return total;
    }

    public static void main(String[] args) {
        if (args.length > 0) {
            solvePart1(readInput(args[0]));
            solvePart2(readInput(args[0]));
        } else {
            solvePart1(readInput("day1/input.txt"));
            solvePart2(readInput("day1/input.txt"));
        }
    }
}