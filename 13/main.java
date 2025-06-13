class Solution {
    public void swapKth(List<Integer> arr, int k) {
        // Swapping the k'th element from beginning and end.
        int n = arr.size();
        Collections.swap(arr, k - 1, n - k);
    }
}
