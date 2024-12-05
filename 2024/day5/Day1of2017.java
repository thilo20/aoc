// package day1;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import org.junit.Rule;

/** solve https://adventofcode.com/2017/day/1 */
public class Day1of2017 {

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
        return lines.stream().map(Day1of2017::tryParse)
                .collect(Collectors.toList());
    }

    public static int solvePart1(List<String> lines) {
        String input = lines.get(0);
        int total = solveCaptcha(input);
        System.out.println("part1: " + total);
        return total;
    }

    static int solveCaptcha(String input) {
        int total = 0;
        String test = input + input.substring(0, 1); // rotation workaround
        for (int i = 1; i < test.length(); i++) {
            if (test.charAt(i) == test.charAt(i - 1)) {
                total += tryParse(test.substring(i - 1, i));
            }
        }
        return total;
    }

    static int solveCaptcha2(String test) {
        int total = 0;
        int offset = test.length() / 2;
        for (int i = 0; i < test.length() / 2; i++) {
            if (test.charAt(i) == test.charAt(i + offset)) {
                total += tryParse(test.substring(i, i + 1));
            }
        }
        return total * 2;
    }

    public static int solvePart2(List<String> lines) {
        String input = lines.get(0);
        int total = solveCaptcha2(input);
        System.out.println("part2: " + total);
        return total;
    }

    public static void main(String[] args) {
        if (args.length > 0) {
            solvePart1(readInput(args[0]));
            solvePart2(readInput(args[0]));
        } else {
            solvePart1(readInput("day5/input-printer.txt"));
            solvePart2(readInput("day5/input-printer.txt"));
        }
    }
}