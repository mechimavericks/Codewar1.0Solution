class Solution {
  public:
    int timeTravel(int n, vector<int> &arr) {
        int ans = 0;
        for(int i = 1; i < n; i++)
            ans += (arr[i] > arr[i - 1] ? 1 : (arr[i] < arr[i - 1] ? 2 : 0));
        return ans;
    }
};
