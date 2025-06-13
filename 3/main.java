class Solution {
    public int[] minAnd2ndMin(int[] arr) {
        int[] ans = new int[2];
        int min1 = arr[0], min2 = Integer.MAX_VALUE, n = arr.length;

        // Traverse the array to find the minimum and second minimum elements.
        for (int i = 1; i < n; i++) {
            // Update min1 and min2 if arr[i] is smaller than both.
            if (arr[i] < min1) {
                min2 = min1;
                min1 = arr[i];
            }
            // Update min2 if arr[i] is smaller than min2 but greater than min1.
            else if (arr[i] < min2 && arr[i] != min1) {
                min2 = arr[i];
            }
        }

        // If there is only one element in the array or second minimum is not found,
        // return {-1, -1}.
        if (n == 1 || min2 == Integer.MAX_VALUE) {
            ans[0] = -1;
            ans[1] = -1;
        } else {
            // Otherwise, return the minimum and second minimum elements.
            ans[0] = min1;
            ans[1] = min2;
        }
        return ans;
    }
}

