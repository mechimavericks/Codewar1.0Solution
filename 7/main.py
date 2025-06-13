from collections import defaultdict


class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        #creating two dictionaries to store the frequency of each element in a and b.
        dic1 = defaultdict(lambda: 0)

        #iterating over a and updating the frequency in dic1.
        for i in a:
            dic1[i] += 1

        #iterating over b and checking if the frequency of each element in b is greater than 0 in dic1.
        for i in b:
            if dic1[i] > 0:
                dic1[i] -= 1
            else:
                return False

        return True

