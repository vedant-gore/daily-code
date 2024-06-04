public class PalindromeChecker {

    public static boolean isPalindrome(String s) {
        // Remove non-alphanumeric characters and convert to lowercase
        String cleaned = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();

        // Check if the cleaned string is equal to its reverse
        int left = 0;
        int right = cleaned.length() - 1;
        while (left < right) {
            if (cleaned.charAt(left) != cleaned.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }

    public static void main(String[] args) {
        String inputString = "A man, a plan, a canal: Panama";
        System.out.println("The string '" + inputString + "' is a palindrome: " + isPalindrome(inputString));
    }
}
