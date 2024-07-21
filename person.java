import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class person {
    public static void main(String[] args) {
        List<Person> people = new ArrayList<>();
        people.add(new Person("Alice", 25));
        people.add(new Person("Bob", 17));
        people.add(new Person("Charlie", 19));
        people.add(new Person("David", 16));
        people.add(new Person("Eve", 22));

        // Filter the list to include only people who are 18 years or older.
        // Sort the filtered list by name in alphabetical order.
        // Create a list of names (String) from the sorted list of people.
        // Print each name from the list of names.

        // TODO: Use Stream API to filter, sort, and collect names
        List<String> names = people.stream()
            .filter(person -> person.getAge() >= 18) // Filter people who are 18 or older
            .sorted((p1, p2) -> p1.getName().compareTo(p2.getName())) // Sort by name
            .map(Person::getName) // Extract names
            .collect(Collectors.toList());

        // Print each name
        names.forEach(System.out::println);
    }
}

class Person {
    private String name;
    private int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }
}
