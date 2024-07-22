import java.util.List;
import java.util.stream.Collectors;

public class upperCaseStream {
    public static void main(String[] args) {
        List<String> words = List.of("apple", "banana", "cherry");
        List<String> upperCaseWords = words.stream()
            .map(String::toUpperCase)
            .collect(Collectors.toList());
        System.out.println("Uppercase words: " + upperCaseWords);
    }
}
