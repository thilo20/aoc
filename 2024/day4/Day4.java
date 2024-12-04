// package day1;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/** solve https://adventofcode.com/2024/day/4 */
public class Day4 {

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

    public class Coord {
        public int x, y;

        public Coord(int x, int y) {
            this.x = x;
            this.y = y;
        }

        public Coord move(Coord delta) {
            return new Coord(x + delta.x, y + delta.y);
        }

        public String toString() {
            return String.format("(%d %d)", x, y);
        }

        @Override
        public int hashCode() {
            final int prime = 31;
            int result = 1;
            result = prime * result + getEnclosingInstance().hashCode();
            result = prime * result + x;
            result = prime * result + y;
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
            Coord other = (Coord) obj;
            if (!getEnclosingInstance().equals(other.getEnclosingInstance()))
                return false;
            if (x != other.x)
                return false;
            if (y != other.y)
                return false;
            return true;
        }

        private Day4 getEnclosingInstance() {
            return Day4.this;
        }
    }

    int max_x, max_y;
    Map<Coord, String> board;

    int loadBoard(List<String> input) {
        Map<Coord, String> map = new HashMap<>();

        int y = 0;
        for (String line : input) {
            for (int x = 0; x < line.length(); x++) {
                // Integer value = tryParse(String.valueOf(line.charAt(x)));
                map.put(new Coord(x, y), line.substring(x, x + 1));
            }
            y++;
        }
        max_x = (input.isEmpty() ? 0 : input.get(0).length() - 1);
        max_y = y - 1;

        board = map;
        return map.size();
    }

    public int solvePart1(List<String> lines) {
        int total = 0;

        loadBoard(lines);

        String word = "XMAS";

        Map<String, Coord> directions = new HashMap<>();
        directions.put("N", new Coord(0, -1));
        directions.put("NE", new Coord(1, -1));
        directions.put("E", new Coord(1, 0));
        directions.put("SE", new Coord(1, 1));
        directions.put("S", new Coord(0, 1));
        directions.put("SW", new Coord(-1, 1));
        directions.put("W", new Coord(-1, 0));
        directions.put("NW", new Coord(-1, -1));

        for (Coord pos : board.keySet()) {
            String val = board.get(pos);
            if (!val.equals(word.substring(0, 1)))
                continue;
            for (Coord dir : directions.values()) {
                Coord test = pos.move(dir);
                for (int i = 1; i < word.length(); i++) {
                    val = board.get(test);
                    if (val == null || !val.equals(word.substring(i, i + 1)))
                        break;
                    test = test.move(dir);
                    if (i == word.length() - 1)
                        total++;
                }
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
            // solvePart1(readInput(args[0]));
            // solvePart2(readInput(args[0]));
        } else {
            Day4 app = new Day4();
            app.solvePart1(readInput("day4/input3.txt"));
            // solvePart2(readInput("day4/input-pt2.txt"));
        }
    }
}