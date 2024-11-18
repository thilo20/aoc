import static org.junit.Assert.assertEquals;

import org.junit.Before;
import org.junit.Test;

public class BoardWalkTest {

    BoardWalk bw;

    @Before
    public void init() {
        bw = new BoardWalk();
        int fields = bw.loadBoard("prepare/board.txt");
        assertEquals(18, fields);
    }

    @Test
    public void walk_full() {
        assertEquals(
                11,
                bw.walk());
    }

    @Test
    public void walk_self() {
        BoardWalk.Coord coord = bw.new Coord(1, 1);
        assertEquals(
                2,
                bw.walk(coord, coord));
    }

    @Test
    public void walk_right() {
        BoardWalk.Coord coord = bw.new Coord(1, 1);
        BoardWalk.Coord coord2 = bw.new Coord(2, 1);
        assertEquals(
                3,
                bw.walk(coord, coord2));
    }

    @Test
    public void walk_down() {
        BoardWalk.Coord coord = bw.new Coord(2, 0);
        BoardWalk.Coord coord2 = bw.new Coord(2, 1);
        assertEquals(
                2,
                bw.walk(coord, coord2));
    }

    @Test(expected = AssertionError.class)
    public void walk_wrongDirection() {
        BoardWalk.Coord start = bw.new Coord(1, 1);
        BoardWalk.Coord dest = bw.new Coord(0, 0);
        bw.walk(start, dest);
    }

    @Test(expected = AssertionError.class)
    public void walk_offBoard() {
        BoardWalk.Coord start = bw.new Coord(0, 0);
        BoardWalk.Coord dest = bw.new Coord(10, 0);
        bw.walk(start, dest);
    }
}
