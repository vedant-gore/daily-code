import java.util.Arrays;
import java.util.List;
import java.util.function.Predicate;
import java.util.stream.Collectors;

public class FilterEvenNumbers {
    public static void main(String[] args) {
        // Step 1: Create a list of integers
        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);

        // Step 2: Use Stream API to filter out even numbers
        List<Integer> oddNumbers = numbers.stream()
                                          .filter(number -> number%2 != 0)
                                          .collect(Collectors.toList());

        // Step 3: Print the resulting list
        System.out.println(oddNumbers);
    }
}


