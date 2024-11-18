// package main;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/** demo grid loading, map lookup and simple algorithm */
public class BoardWalk {

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

        public Coord right() {
            return new Coord(x + 1, y);
        }

        public Coord down() {
            return new Coord(x, y + 1);
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

        private BoardWalk getEnclosingInstance() {
            return BoardWalk.this;
        }
    }

    int max_x, max_y;
    Map<Coord, Integer> board;

    int loadBoard(String filename) {
        Map<Coord, Integer> map = new HashMap<>();
        List<String> input = readInput(filename);
        int y = 0;
        for (String line : input) {
            for (int x = 0; x < line.length(); x++) {
                Integer value = tryParse(String.valueOf(line.charAt(x)));
                map.put(new Coord(x, y), value);
            }
            y++;
        }
        max_x = (input.isEmpty() ? 0 : input.get(0).length() - 1);
        max_y = y - 1;

        board = map;
        return map.size();
    }

    /* Walks across the board from top left to bottom right */
    public int walk() {
        Coord start = new Coord(0, 0);
        Coord destination = new Coord(max_x, max_y);

        return walk(start, destination);
    }

    /* Walks across the board, only directions: right, down */
    public int walk(Coord start, Coord destination) {
        // assert (false); // enable with VM args "-ea"
        assert (board != null);
        assert (board.get(start) != null);
        assert (board.get(destination) != null);
        assert (start.x <= destination.x);
        assert (start.y <= destination.y);

        int sum = flood(start, destination);

        System.out.println("sum: " + sum);
        return sum;
    }

    private int flood(BoardWalk.Coord start, BoardWalk.Coord destination) {
        List<Node> openlist = new ArrayList<>();
        openlist.add(new Node(null, start, 0, 0));

        Map<Coord, Node> closedlist = new HashMap<>();
        int count = 0;
        while (openlist.size() > 0) {
            BoardWalk.Node node = openlist.remove(0);

            // test highest sum
            BoardWalk.Node visited = closedlist.get(node.pos);
            if (visited == null) {
                closedlist.put(node.pos, node);
            } else {
                if (visited.sum < node.sum) {
                    // keep only node with higher sum!
                    closedlist.put(node.pos, node);
                }
            }

            // expand right
            if (node.pos.x < destination.x) {
                BoardWalk.Node r = new Node(node, node.pos.right(), node.steps + 1, node.sum + board.get(node.pos));
                openlist.add(r);
            }
            // expand down
            if (node.pos.y < destination.y) {
                BoardWalk.Node d = new Node(node, node.pos.down(), node.steps + 1, node.sum + board.get(node.pos));
                openlist.add(d);
            }

            count++;
        }
        System.out.println("BoardWalk.flood(): openlist nodes analyzed: " + count);

        BoardWalk.Node found = closedlist.get(destination);
        if (found != null) {
            List<Node> path = getPath(found);
            for (Node node : path) {
                System.out.println(node.toString());
            }
            return found.sum + board.get(found.pos);
        } else
            return -1;
    }

    private List<Node> getPath(BoardWalk.Node found) {
        List<Node> path = new ArrayList<>();
        Node n = found;
        while (n != null) {
            path.add(n);
            n = n.parent;
        }
        Collections.reverse(path);
        return path;
    }

    public class Node {
        Node parent;
        Coord pos;
        int steps;
        int sum;

        public Node(Node parent, Coord pos, int steps, int sum) {
            this.parent = parent;
            this.pos = pos;
            this.steps = steps;
            this.sum = sum;
        }

        @Override
        public String toString() {
            return "Node [pos=" + pos + ", steps=" + steps + ", sum=" + sum + "]";
        }
    }

    public static void main(String[] args) {
        if (args.length > 0) {
            BoardWalk app = new BoardWalk();
            app.loadBoard(args[0]);
            app.walk();
            app.walk(app.new Coord(0, 0), app.new Coord(0, 0));
            app.walk(app.new Coord(0, 0), app.new Coord(1, 1));
        }
    }
}