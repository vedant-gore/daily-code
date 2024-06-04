import java.util.HashSet;
import java.util.Set;

public class DuplicateFinder {
    public static void main(String[] args) {
        int[] inputArray = {4, 3, 2, 7, 8, 2, 3, 1};
        Set<Integer> duplicates = findDuplicates(inputArray);
        System.out.println("Duplicates: " + duplicates);
    }

    public static Set<Integer> findDuplicates(int[] numbers) {
        Set<Integer> seen = new HashSet<>();
        Set<Integer> duplicates = new HashSet<>();
        
        for (int number : numbers) {
            if (!seen.add(number)) {
                duplicates.add(number);
            }
        }
        
        return duplicates;
    }
}
