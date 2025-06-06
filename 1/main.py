from typing import List


class Solution:
    def validStrings(self, n : int, k : int, arr : List[str]) -> int:
        ans=0
        for el in arr:
            C=0
            for e in el:
                if e in "aeiou":
                    C+=1
            if C==k:
                ans+=1
        return ans
