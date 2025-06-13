// Back-end complete function Template for Java

class Solution {
    // Function to find element with more appearances between two elements in an
    // array.
    public int majorityWins(int arr[], int n, int x, int y) {
        int count_x = 0;
        int count_y = 0;

        // Iterating through the array elements.
        // Incrementing the counter variables accordingly.
        for (int i = 0; i < n; i++) {
            if (arr[i] == x) count_x++;
            if (arr[i] == y) count_y++;
        }

        // Comparing the two counters.
        if (count_x > count_y)
            // Returning the number with more appearances in the array.
            return x;

        else if (count_y > count_x)
            // Returning the number with more appearances in the array.
            return y;

        // If both appear same number of times, returning the smaller number.
        else if (x < y)
            return x;
        else
            return y;
    }
}


