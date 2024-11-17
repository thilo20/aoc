import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class RegEx2 {
    public static List<String> readInput(String filename) {
        Path path = Paths.get(filename);
        try {
            return Files.readAllLines(path);
        } catch (IOException e) {
            // e.printStackTrace();
            System.err.println(e);
            return List.of();
        }
    }

    public static void main(String[] args) {
        String file = "../2022/day16/inputs1.txt";
        List<String> inputs = readInput(file);

        Pattern pattern = Pattern.compile("[A-Z]{2}");

        for (String line : inputs) {
            Matcher matcher = pattern.matcher(line);
            boolean matchFound = matcher.find();
            while (matchFound) {
                System.out.println("Match pos: " + matcher.start() + " val: " + matcher.group());
                matchFound = matcher.find();
            }
        }
    }
}