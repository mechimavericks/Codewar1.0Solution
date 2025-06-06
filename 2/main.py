class Solution:

    def findMedian(self, arr):
        arr.sort()  # Sorting the list in ascending order

        n = len(arr)
        # If the size of the list is odd
        if n % 2 == 1:
            # Median is the middle element
            return arr[n // 2]
        else:
            # Median is the average of the two middle elements
            return (arr[n // 2] + arr[(n // 2) - 1]) / 2.0
