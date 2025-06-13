class Solution {
    public static int timeTravel(int n, int[] arr) {
        int ans = 0;
        for(int i = 1; i < n; i++)
            ans += (arr[i] > arr[i - 1] ? 1 : (arr[i] < arr[i - 1] ? 2 : 0));
        return ans;
    }
}
