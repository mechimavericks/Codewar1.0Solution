from typing import List


class Solution:
    def isFriend(self, n : int, x : int, y : int, arr : List[int]) -> str:
        if y-x in arr:
            return "yes"
        else:
            return "no"
