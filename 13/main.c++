class Solution {
  public:
    void swapKth(vector<int> &arr, int k) {
        // swapping the k'th element from beginning and end.
        int n = arr.size();
        swap(arr[k - 1], arr[n - k]);
    }
};
