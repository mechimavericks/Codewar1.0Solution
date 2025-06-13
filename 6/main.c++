
class Solution {
  public:
    // Function to find elements in the array that are equal to their index.
    vector<int> valueEqualToIndex(vector<int>& arr) {
        vector<int> result;
        int n = arr.size();
        // iterating over all the elements in the array
        for (int i = 0; i < n; i++) {
            // checking if the element is equal to its index + 1
            if (arr[i] == i + 1) {
                // adding the element to the result vector
                result.push_back(arr[i]);
            }
        }
        // returning the result vector with elements that are equal to their index
        return result;
    }
};
