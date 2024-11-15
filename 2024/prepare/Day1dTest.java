import static org.junit.Assert.assertEquals;

import java.util.Arrays;
import java.util.List;

import org.junit.Test;

public class Day1dTest {

    @Test
    public void readInput_fileNotFound() {
        assertEquals(
                List.of(),
                Day1d.readInput("nofile"));
    }

    @Test
    public void readInput_fileWithText() {
        assertEquals(
                List.of("Hello, world!"),
                Day1d.readInput("prepare/fileTest.txt"));
    }

    @Test
    public void solvePart1_emptyList() {
        assertEquals(
                0,
                Day1d.solvePart1(List.of()));
    }

    @Test
    public void solvePart1_singleListItem() {
        assertEquals(
                2,
                Day1d.solvePart1(List.of(2)));
    }

    @Test
    public void solvePart1_singleElement() {
        assertEquals(
                2,
                Day1d.solvePart1(Arrays.asList(2, null)));
    }

    @Test
    public void solvePart1_singleBlock() {
        assertEquals(
                6,
                Day1d.solvePart1(Arrays.asList(1, 2, 3)));
    }

    @Test
    public void solvePart1_twoBlocks() {
        assertEquals(
                3,
                Day1d.solvePart1(Arrays.asList(1, null, 3)));
    }
}
