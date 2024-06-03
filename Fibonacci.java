public class Fibonacci {
    public static int fibonacci(int n) {
        if (n <= 1) {
            return n;
        }
        int a = 0, b = 1;
        int sum = 0;
        for (int i = 2; i <= n; i++) {
            sum = a + b;
            a = b;
            b = sum;
        }
        return b;
    }

    public static void main(String[] args) {
        System.out.println(fibonacci(0));  // Should return 0
        System.out.println(fibonacci(1));  // Should return 1
        System.out.println(fibonacci(9));  // Should return 34
    }
}
