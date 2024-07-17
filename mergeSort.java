import java.util.*;

public class Main {
    public static void main(String[] args) {
        int[] arr = {5, 1, 4, 2, 3};
        int[] result = sortOddIndexedElements(arr);
        System.out.println(Arrays.toString(result));
    }

    public static int[] sortOddIndexedElements(int[] arr) {
        // Extract the odd-indexed elements
        List<Integer> oddIndexedElements = new ArrayList<>();
        for (int i = 1; i < arr.length; i += 2) {
            oddIndexedElements.add(arr[i]);
        }

        // Convert the list to an array
        int[] oddArr = oddIndexedElements.stream().mapToInt(i -> i).toArray();

        // Sort the extracted elements using merge sort
        mergeSort(oddArr, 0, oddArr.length - 1);

        // Replace the odd-indexed elements in the original array with the sorted elements
        for (int i = 1, j = 0; i < arr.length; i += 2, j++) {
            arr[i] = oddArr[j];
        }

        return arr;
    }

    public static void mergeSort(int[] arr, int left, int right) {
        if (left < right) {
            int mid = (left + right) / 2;

            mergeSort(arr, left, mid);
            mergeSort(arr, mid + 1, right);

            merge(arr, left, mid, right);
        }
    }

    public static void merge(int[] arr, int left, int mid, int right) {
        int n1 = mid - left + 1;
        int n2 = right - mid;

        int[] L = new int[n1];
        int[] R = new int[n2];

        for (int i = 0; i < n1; ++i)
            L[i] = arr[left + i];
        for (int j = 0; j < n2; ++j)
            R[j] = arr[mid + 1 + j];

        int i = 0, j = 0;

        int k = left;
        while (i < n1 && j < n2) {
            if (L[i] <= R[j]) {
                arr[k] = L[i];
                i++;
            } else {
                arr[k] = R[j];
                j++;
            }
            k++;
        }

        while (i < n1) {
            arr[k] = L[i];
            i++;
            k++;
        }

        while (j < n2) {
            arr[k] = R[j];
            j++;
            k++;
        }
    }
}
