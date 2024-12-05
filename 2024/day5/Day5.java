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

/** solve https://adventofcode.com/2024/day/5 */
public class Day5 {

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
        return lines.stream().map(Day5::tryParse)
                .collect(Collectors.toList());
    }

    static class Rule {
        Integer before;
        Integer after;

        public Rule(Integer before, Integer after) {
            this.before = before;
            this.after = after;
        }

        @Override
        public int hashCode() {
            final int prime = 31;
            int result = 1;
            result = prime * result + before;
            result = prime * result + after;
            return result;
        }

        @Override
        public boolean equals(Object obj) {
            if (this == obj)
                return true;
            if (obj == null)
                return false;
            if (getClass() != obj.getClass())
                return false;
            Rule other = (Rule) obj;
            if (before != other.before)
                return false;
            if (after != other.after)
                return false;
            return true;
        }

        @Override
        public String toString() {
            return "Rule " + before + "|" + after;
        }
    }

    public static int solvePart1(List<String> lines) {
        int total = 0;

        Set<Rule> rules = new HashSet<>();
        List<List<Integer>> updates = new ArrayList<>();

        for (String line : lines) {
            String[] parts = line.split("\\|");
            if (parts.length == 2) {
                rules.add(new Rule(tryParse(parts[0]), tryParse(parts[1])));
                continue;
            }

            parts = line.split(",");
            if (parts.length > 1) {
                updates.add(Stream.of(parts).map(Day5::tryParse)
                        .collect(Collectors.toList()));
            }
        }

        for (List<Integer> update : updates) {
            boolean correct = isCorrect(rules, update);
            if (correct) {
                total += update.get(update.size() / 2);
            }

        }
        System.out.println("part1: " + total);
        return total;
    }

    public static int solvePart2(List<String> lines) {
        int total = 0;

        Set<Rule> rules = new HashSet<>();
        List<List<Integer>> updates = new ArrayList<>();

        for (String line : lines) {
            String[] parts = line.split("\\|");
            if (parts.length == 2) {
                rules.add(new Rule(tryParse(parts[0]), tryParse(parts[1])));
                continue;
            }

            parts = line.split(",");
            if (parts.length > 1) {
                updates.add(Stream.of(parts).map(Day5::tryParse)
                        .collect(Collectors.toList()));
            }
        }

        for (List<Integer> update : updates) {
            // test if any page pair violates a rule (upper triangle)
            boolean correct = isCorrect(rules, update);
            if (!correct) {
                // fix order
                update = fix(rules, update);
                correct = isCorrect(rules, update);
                assert (correct);
                total += update.get(update.size() / 2);
            }

        }
        System.out.println("part2: " + total);
        return total;
    }

    private static boolean isCorrect(Set<Rule> rules, List<Integer> update) {
        for (int i = 0; i < update.size() - 1; i++) {
            for (int j = i + 1; j < update.size(); j++) {
                if (rules.contains(new Rule(update.get(j), update.get(i)))) {
                    System.out.println(String.format("i=%d j=%d size=%d", i, j, update.size()));
                    return false;
                }
            }
        }
        return true;
    }

    private static List<Integer> fix(Set<Rule> rules, List<Integer> buggy) {
        List<Integer> update = new ArrayList<>(buggy);
        for (int i = 0; i < update.size() - 1; i++) {
            for (int j = i + 1; j < update.size(); j++) {
                if (rules.contains(new Rule(update.get(j), update.get(i)))) {
                    // System.out.println(String.format("%s i=%d j=%d size=%d", update.toString(),
                    // i, j, update.size()));
                    // sort item at index i after j
                    update.add(j + 1, update.get(i));
                    update.remove(i);
                    // re-test i
                    i--;
                    break;
                }
            }
        }
        return update;
    }

    public static void main(String[] args) {
        if (args.length > 0) {
            solvePart1(readInput(args[0]));
            solvePart2(readInput(args[0]));
        } else {
            solvePart1(readInput("day5/input.txt"));
            solvePart2(readInput("day5/input.txt"));
        }
    }
}