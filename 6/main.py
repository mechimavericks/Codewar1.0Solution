class Solution:
    # Function to find values in array equal to their indices
    def valueEqualToIndex(self, arr):
        ans = []  # create an empty list to store the values
        n = len(arr)
        # iterate through the array
        for i in range(n):
            # check if the value at index i is equal to its index + 1
            if arr[i] == i + 1:
                ans.append(arr[i])  # if true, add the value to the list
        return ans  # return the list of values that are equal to their indices
    
    

