// package day1;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

/** solve https://adventofcode.com/2024/day/6 */
public class Day6 {

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

        private Day6 getEnclosingInstance() {
            return Day6.this;
        }
    }

    public class CoordWithDirection extends Coord {
        String dir;

        public CoordWithDirection(int x, int y, String dir) {
            super(x, y);
            this.dir = dir;
        }

        @Override
        public int hashCode() {
            final int prime = 31;
            int result = super.hashCode();
            result = prime * result + getEnclosingInstance().hashCode();
            result = prime * result + ((dir == null) ? 0 : dir.hashCode());
            return result;
        }

        @Override
        public boolean equals(Object obj) {
            if (this == obj)
                return true;
            if (!super.equals(obj))
                return false;
            if (getClass() != obj.getClass())
                return false;
            CoordWithDirection other = (CoordWithDirection) obj;
            if (!getEnclosingInstance().equals(other.getEnclosingInstance()))
                return false;
            if (obj == null)
                return false;
            if (x != other.x)
                return false;
            if (y != other.y)
                return false;
            if (dir == null) {
                if (other.dir != null)
                    return false;
            } else if (!dir.equals(other.dir))
                return false;
            return true;
        }

        private Day6 getEnclosingInstance() {
            return Day6.this;
        }

        @Override
        public String toString() {
            return "CoordWithDirection [x=" + x + ", y=" + y + ", dir=" + dir + "]";
        }
    }

    int max_x, max_y;
    Map<Coord, String> board;
    Coord startPos;

    int loadBoard(List<String> input) {
        Map<Coord, String> map = new HashMap<>();

        int y = 0;
        for (String line : input) {
            for (int x = 0; x < line.length(); x++) {
                String val = line.substring(x, x + 1);
                if ("^".equals(val)) {
                    val = ".";
                    startPos = new Coord(x, y);
                }
                map.put(new Coord(x, y), val);
            }
            y++;
        }
        max_x = (input.isEmpty() ? 0 : input.get(0).length() - 1);
        max_y = y - 1;

        board = map;
        return map.size();
    }

    public int solvePart1(List<String> lines) {
        int steps = 0;

        loadBoard(lines);

        Map<String, Coord> directions = new HashMap<>();
        directions.put("N", new Coord(0, -1));
        directions.put("E", new Coord(1, 0));
        directions.put("S", new Coord(0, 1));
        directions.put("W", new Coord(-1, 0));

        Set<Coord> visited = new HashSet<>();
        Coord pos = startPos;
        String dir = "N";
        while (board.containsKey(pos)) {
            steps++;
            visited.add(pos);
            // look ahead
            Coord next = pos.move(directions.get(dir));
            if ("#".equals(board.getOrDefault(next, ""))) {
                dir = rotateRight(dir);
            } else {
                pos = next;
            }
        }

        System.out.println("part1: " + visited.size());
        return steps;
    }

    String rotateRight(String dir) {
        switch (dir) {
            case "N":
                return "E";
            case "E":
                return "S";
            case "S":
                return "W";
            case "W":
                return "N";
            default:
                return "";
        }
    }

    String opposite(String dir) {
        switch (dir) {
            case "N":
                return "S";
            case "E":
                return "W";
            case "S":
                return "N";
            case "W":
                return "E";
            default:
                return "";
        }
    }

    public int solvePart2(List<String> lines) {
        int steps = 0;

        loadBoard(lines);

        Map<String, Coord> directions = new HashMap<>();
        directions.put("N", new Coord(0, -1));
        directions.put("E", new Coord(1, 0));
        directions.put("S", new Coord(0, 1));
        directions.put("W", new Coord(-1, 0));

        Set<Coord> visited = new HashSet<>();
        List<CoordWithDirection> visitedDir = new ArrayList<>();
        Coord pos = startPos;
        String dir = "N";
        while (board.containsKey(pos)) {
            steps++;
            visited.add(pos);
            // if (!pos.equals(startPos)) {
            visitedDir.add(new CoordWithDirection(pos.x, pos.y, dir));
            // }
            // look ahead
            Coord next = pos.move(directions.get(dir));
            if ("#".equals(board.getOrDefault(next, ""))) {
                dir = rotateRight(dir);
            } else {
                pos = next;
            }
        }

        plotMap(visited, null);
        System.out.println("start: " + startPos.toString());

        Set<Coord> options = new HashSet<>();
        steps = 0;
        for (CoordWithDirection coordWithDirection : visitedDir) {
            // if (coordWithDirection.x == 8 && coordWithDirection.y == 4) {
            if (coordWithDirection.x == 3 && coordWithDirection.y == 6) {
                int i = 42;
            }
            if (startPos.equals(new Coord(coordWithDirection.x, coordWithDirection.y))) {
                continue;
            }

            Set<CoordWithDirection> path = new HashSet<>();

            // test if temp. blocking this tile leads to a loop
            board.replace(new Coord(coordWithDirection.x, coordWithDirection.y), "#");
            // step back
            pos = startPos;
            dir = "N";
            // start walking
            while (board.containsKey(pos)) {
                path.add(new CoordWithDirection(pos.x, pos.y, dir));
                // look ahead
                Coord next = pos.move(directions.get(dir));
                if ("#".equals(board.getOrDefault(next, ""))) {
                    dir = rotateRight(dir);
                } else {
                    pos = next;
                }
                if (path.contains(new CoordWithDirection(pos.x, pos.y, dir))) {
                    // loop detected
                    steps++;
                    options.add(new Coord(coordWithDirection.x, coordWithDirection.y));
                    // System.out.println(String.format("hit %d: %s", steps, coordWithDirection));
                    break;
                }
                // System.out.println(String.format(" step x=%d y=%d dir=%s", next.x, next.y,
                // dir));
            }
            // unblock tile
            board.replace(new Coord(coordWithDirection.x, coordWithDirection.y), ".");

        }

        if (false) {
            Set<Coord> expected = new HashSet<>();
            expected.add(new Coord(3, 6));
            expected.add(new Coord(6, 7));
            expected.add(new Coord(7, 7));
            expected.add(new Coord(1, 8));
            expected.add(new Coord(3, 8));
            expected.add(new Coord(7, 9));

            // System.out.println();
            // plotMap(visited, expected);
            System.out.println();
            plotMap(visited, options);

            for (Coord coord : options) {
                System.out.println(coord.toString() + (expected.contains(coord) ? " hit" : "miss"));
            }
        }

        System.out.println("part2: " + options.size());
        return steps;
    }

    private void plotMap(Set<Day6.Coord> visited, Set<Day6.Coord> options) {
        for (int y = 0; y < max_y; y++) {
            StringBuilder sb = new StringBuilder();
            for (int x = 0; x < max_x; x++) {
                if (options != null && options.contains(new Coord(x, y))) {
                    sb.append("O");
                } else if (visited.contains(new Coord(x, y))) {
                    sb.append("X");
                } else {
                    sb.append(board.get(new Coord(x, y)));
                }
            }
            System.out.println(sb.toString());
        }
    }

    public static void main(String[] args) {
        if (args.length > 0) {
            // solvePart1(readInput(args[0]));
            // solvePart2(readInput(args[0]));
        } else {
            Day6 app = new Day6();
            app.solvePart1(readInput("day6/input.txt"));
            app.solvePart2(readInput("day6/input2.txt"));
        }
    }
}