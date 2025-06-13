#Back-end complete function Template for Python 3
class Solution:
    def timeTravel(self, n, arr):
        ans=0
        for i in range(1,n):
            if (arr[i]>arr[i-1]):
                ans+=1
            elif (arr[i]<arr[i-1]):
                ans+=2
        return ans
