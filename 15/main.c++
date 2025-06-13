class Solution {
  public:
    // Returns count of rotations for an array which
    // is first sorted in ascending order, then rotated
    int countRotations(vector<int> &arr, int low, int high) {
        // This condition is needed to handle the case
        // when the array is not rotated at all
        if (high < low)
            return 0;

        // If there is only one element left
        if (high == low)
            return low;

        // Find mid
        int mid = low + (high - low) / 2; /*(low + high)/2;*/

        // Check if element (mid+1) is minimum element.
        // Consider the cases like {3, 4, 5, 1, 2}
        if (mid < high && arr[mid + 1] < arr[mid])
            return (mid + 1);

        // Check if mid itself is minimum element
        if (mid > low && arr[mid] < arr[mid - 1])
            return mid;

        // Decide whether we need to go to left half or
        // right half
        if (arr[high] > arr[mid])
            return countRotations(arr, low, mid - 1);

        return countRotations(arr, mid + 1, high);
    }

  public:
    int findKRotation(vector<int> &arr) {
        int n = arr.size();
        return countRotations(arr, 0, n - 1);
    }
};

