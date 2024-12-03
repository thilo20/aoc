// package day1;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/** solve https://adventofcode.com/2024/day/3 */
public class Day3 {

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

    public static int solvePart1(List<String> lines) {
        int total = 0;

        Pattern pattern = Pattern.compile("mul\\((\\d+),(\\d+)\\)");

        for (String line : lines) {
            Matcher matcher = pattern.matcher(line);
            boolean matchFound = matcher.find();
            while (matchFound) {
                System.out.println("Match pos: " + matcher.start() + " val: " + matcher.group());
                total += tryParse(matcher.group(1)) * tryParse(matcher.group(2));
                matchFound = matcher.find();
            }
        }

        System.out.println("part1: " + total);
        return total;
    }

    public static int solvePart2(List<String> lines) {
        int total = 0;

        Pattern pattern = Pattern.compile("mul\\((\\d+),(\\d+)\\)");
        Pattern pattern2 = Pattern.compile("do(n't)?\\(\\)");

        boolean enabled = true;
        for (String line : lines) {
            Matcher matcher = pattern.matcher(line);
            boolean matchFound = matcher.find();
            while (matchFound) {
                System.out.println("mul pos: " + matcher.start() + " val: " + matcher.group());

                // process all do/don't toggles left of current start index
                Matcher matcher2 = pattern2.matcher(line.subSequence(0, matcher.start()));
                boolean matchFound2 = matcher2.find();
                while (matchFound2 && matcher2.start() < matcher.start()) {
                    System.out.println("do/n't pos: " + matcher2.start() + " val: " + matcher2.group());
                    enabled = "do()".equals(matcher2.group()) ? true : false;
                    matchFound2 = matcher2.find();
                }

                if (enabled)
                    total += tryParse(matcher.group(1)) * tryParse(matcher.group(2));
                matchFound = matcher.find();
            }
        }

        System.out.println("part2: " + total);
        return total;
    }

    public static void main(String[] args) {
        if (args.length > 0) {
            solvePart1(readInput(args[0]));
            solvePart2(readInput(args[0]));
        } else {
            solvePart1(readInput("day3/input.txt"));
            solvePart2(readInput("day3/input-pt2.txt"));
        }
    }
}