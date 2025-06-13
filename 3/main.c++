class Solution {
  public:
    // Function to find the minimum and second minimum elements in the array.
    vector<int> minAnd2ndMin(vector<int> &arr) {
        vector<int> ans;
        int min1 = arr[0], min2 = INT_MAX, n = arr.size();

        // Traverse the array to find the minimum and second minimum elements.
        for (int i = 1; i < n; i++) {
            // Update min1 and min2 if arr[i] is smaller than both.
            if (arr[i] < min1) {
                min2 = min1;
                min1 = arr[i];
            }
            // Update min2 if arr[i] is smaller than min2 but greater than min1.
            else if (arr[i] < min2 && arr[i] != min1)
                min2 = arr[i];
        }

        // If there is only one element in the array or second minimum is not found,
        // return
        // {-1, -1}.
        if (n == 1 || min2 == INT_MAX) {
            ans.push_back(-1);
            ans.push_back(-1);
        }
        // Otherwise, return the minimum and second minimum elements.
        else {
            ans.push_back(min1);
            ans.push_back(min2);
        }
        return ans;
    }
};

