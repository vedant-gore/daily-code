public class findSmallestPositiveMissingInt {

    public static void main(String[] args) {
        int[] nums = {0, 1, 2, 6, 9, 11, 15};
        System.out.println("The smallest missing positive number is: " + findSmallestMissingNumber(nums));
    }

    public static int findSmallestMissingNumber(int[] nums) {
        int left = 0;
        int right = nums.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            // If the value at mid index is equal to its index, the missing number is on the right side
            if (nums[mid] == mid) {
                left = mid + 1;
            } else {
                // If the value at mid index is not equal to its index, the missing number is on the left side
                right = mid - 1;
            }
        }

        // The left pointer will be at the position of the smallest missing number
        return left;
    }
}
