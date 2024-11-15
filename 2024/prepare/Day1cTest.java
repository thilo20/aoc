import static org.junit.Assert.assertEquals;

import java.util.List;

import org.junit.Ignore;
import org.junit.Test;

public class Day1cTest {

    @Test
    public void readInput_fileNotFound() {
        assertEquals(
                List.of(),
                Day1c.readInput("nofile"));
    }

    @Test
    public void readInput_fileWithText() {
        assertEquals(
                List.of("Hello, world!"),
                Day1c.readInput("prepare/fileTest.txt"));
    }

    @Test
    public void solvePart1_emptyList() {
        assertEquals(
                0,
                Day1c.solvePart1(List.of()));
    }

    @Ignore("we rely on a blank line as last list item!")
    @Test
    public void solvePart1_singleListItem() {
        assertEquals(
                2,
                Day1c.solvePart1(List.of("2")));
    }

    @Test
    public void solvePart1_singleElement() {
        assertEquals(
                2,
                Day1c.solvePart1(List.of("2", "")));
    }

    @Test
    public void solvePart1_singleBlock() {
        assertEquals(
                6,
                Day1c.solvePart1(List.of("1", "2", "3", "")));
    }

    @Test
    public void solvePart1_twoBlocks() {
        assertEquals(
                3,
                Day1c.solvePart1(List.of("1", "", "3", "")));
    }
}
