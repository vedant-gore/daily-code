import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class FilterNames {
    public static void main(String[] args) {
        // Step 1: Create a list of strings
        List<String> names = Arrays.asList("Alice", "Bob", "Alex", "Charlie", "Ann", "David");

        // Step 2: Use Stream API to filter out names that start with "A"
        List<String> filteredNames = names.stream()
                                          .filter(name -> name.startsWith("A"))
                                          .collect(Collectors.toList());

        // Step 3: Print the resulting list
        System.out.println(filteredNames);
    }
}
