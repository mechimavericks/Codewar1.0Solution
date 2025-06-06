class Solution:

    def swapKth(self, arr, k):
        # Swapping the k'th element from beginning and end.
        n = len(arr)
        arr[k - 1], arr[n - k] = arr[n - k], arr[k - 1]

