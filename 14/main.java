class Solution {
    // Function to find equilibrium point in the array.
    public static int findEquilibrium(int arr[]) {
        int n = arr.length;

        // We store the sum of all array elements in a long to prevent overflow.
        long sum = 0;
        for (int i = 0; i < n; i++) sum += arr[i];

        // sum2 is used to store the prefix sum.
        long sum2 = 0;

        for (int i = 0; i < n; i++) {

            // Leaving out the value of the current element from the suffix sum.
            sum = sum - arr[i];

            // Checking if suffix and prefix sums are the same.
            if (sum2 == sum) {
                // Returning the index or equilibrium point.
                return i;
            }

            // Adding the value of the current element to the prefix sum.
            sum2 = sum2 + arr[i];
        }
        return -1;
    }
}
