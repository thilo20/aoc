import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class RegEx1 {
    public static void main(String[] args) {
        Pattern pattern = Pattern.compile("XMAS", Pattern.CASE_INSENSITIVE);
        Matcher matcher = pattern.matcher("Have a fun xmas time!");
        boolean matchFound = matcher.find();
        if (matchFound) {
            System.out.println(String.format("Match found, offset: %d value: %s",
                    matcher.start(), matcher.group()));
        } else {
            System.out.println("Match not found");
        }
    }
}
// Output: Match found, offset: 11 value: xmas
