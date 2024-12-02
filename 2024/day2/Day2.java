// package day1;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

/** solve https://adventofcode.com/2024/day/2 */
public class Day2 {

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

    public static List<Integer> convertLineToNumbers(String line) {
        return Stream.of(line.split(" ")).map(Day2::tryParse)
                .collect(Collectors.toList());
    }

    public static int solvePart1(List<String> lines) {
        int total = 0;
        List<Integer> delta;

        for (String line : lines) {
            List<Integer> numbers = convertLineToNumbers(line);
            assert (numbers.size() > 1);
            delta = toDeltaList(numbers);

            if (isSafe(delta)) {
                total++;
            }
        }

        System.out.println("part1: " + total);
        return total;
    }

    private static List<Integer> toDeltaList(List<Integer> numbers) {
        List<Integer> delta;
        delta = new ArrayList<>();
        for (int i = 1; i < numbers.size(); i++) {
            delta.add(numbers.get(i) - numbers.get(i - 1));
        }
        return delta;
    }

    private static boolean isSafe(List<Integer> delta) {
        if (delta.get(0) == 0)
            return false;
        boolean asc = delta.get(0) > 0;
        for (Integer diff : delta) {
            if ((diff == 0) || (Math.abs(diff) > 3)) {
                return false;
            } else {
                if ((asc && diff < 0) || (!asc && diff > 0)) {
                    return false;
                }
            }
        }
        return true;
    }

    public static int solvePart2(List<String> lines) {
        int total = 0;
        List<Integer> delta;

        for (String line : lines) {
            List<Integer> numbers = convertLineToNumbers(line);
            assert (numbers.size() > 1);
            delta = toDeltaList(numbers);

            if (isSafe(delta)) {
                total++;
            } else {
                // test with dampener = removing a number
                for (int i = 0; i < numbers.size(); i++) {
                    List<Integer> nums = new ArrayList(numbers);
                    nums.remove(i);
                    delta = toDeltaList(nums);
                    if (isSafe(delta)) {
                        total++;
                        break;
                    }
                }
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
            solvePart1(readInput("day2/input2.txt"));
            solvePart2(readInput("day2/input2.txt"));
        }
    }
}