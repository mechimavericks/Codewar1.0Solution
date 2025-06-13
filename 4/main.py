import math


class Solution:
    # Function to count the number of perfect squares from 1 to N
    def countSquares(self, n):
        # total number of perfect squares less than or equal to N-1
        ans = int(math.sqrt(n - 1))
        # return the result
        return ans
