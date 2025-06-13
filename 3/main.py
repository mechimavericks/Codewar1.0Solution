class Solution:

    def minAnd2ndMin(self, arr):
        # Initialize the answer list
        ans = []

        # Edge case: if the array is empty, return [-1, -1]
        if len(arr) == 0:
            return [-1, -1]

        min1 = arr[0]
        min2 = float('inf')
        n = len(arr)

        # Traverse the array to find the minimum and second minimum elements.
        for i in range(1, n):
            # Update min1 and min2 if arr[i] is smaller than both.
            if arr[i] < min1:
                min2 = min1
                min1 = arr[i]
            # Update min2 if arr[i] is smaller than min2 but greater than min1.
            elif arr[i] < min2 and arr[i] != min1:
                min2 = arr[i]

        # If there is only one element in the array or second minimum is not found,
        # return [-1, -1].
        if n == 1 or min2 == float('inf'):
            ans.append(-1)
            ans.append(-1)
        else:
            # Otherwise, return the minimum and second minimum elements.
            ans.append(min1)
            ans.append(min2)

        return ans
