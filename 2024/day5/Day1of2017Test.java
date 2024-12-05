import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class Day1of2017Test {

    @Test
    public void solveCaptcha_1() {
        assertEquals(3, Day1of2017.solveCaptcha("1122"));
    }

    @Test
    public void solveCaptcha_2() {
        assertEquals(4, Day1of2017.solveCaptcha("1111"));
    }

    @Test
    public void solveCaptcha_3() {
        assertEquals(0, Day1of2017.solveCaptcha("1234"));
    }

    @Test
    public void solveCaptcha_4() {
        assertEquals(9, Day1of2017.solveCaptcha("91212129"));
    }

    @Test
    public void solveCaptcha2_1() {
        assertEquals(6, Day1of2017.solveCaptcha2("1212"));
    }

    @Test
    public void solveCaptcha2_2() {
        assertEquals(0, Day1of2017.solveCaptcha2("1221"));
    }

    @Test
    public void solveCaptcha2_3() {
        assertEquals(4, Day1of2017.solveCaptcha2("123425"));
    }

    @Test
    public void solveCaptcha2_4() {
        assertEquals(12, Day1of2017.solveCaptcha2("123123"));
    }

    @Test
    public void solveCaptcha2_5() {
        assertEquals(4, Day1of2017.solveCaptcha2("12131415"));
    }
}