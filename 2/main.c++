class Solution {
  public:
    double findMedian(vector<int> &arr) {
        // Sorting the vector in ascending order
        sort(arr.begin(), arr.end());

        double ans;
        // if the size of the vector is odd
        if (arr.size() & 1)
            // Median is the middle element
            ans = arr[arr.size() / 2];
        // If the size of the vector is even
        else
            // Median is the average of the two middle elements
            ans = (arr[arr.size() / 2] + arr[arr.size() / 2 - 1]) / 2.0;
        return ans;
    }
};