import java.util.List;
import java.util.stream.Collectors;

public class removeDupliStream {
    public static void main(String[] args) {
        List<Integer> numbers = List.of(10, 20, 10, 30, 20, 40);
        List<Integer> distinctNumbers = numbers.stream()
            .distinct()
            .collect(Collectors.toList());
        System.out.println("Distinct numbers: " + distinctNumbers);
    }
}
