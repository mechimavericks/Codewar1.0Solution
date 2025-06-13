from typing import List


class Solution:
    def findAnswer(self, n : int, A : List[int]) -> List[int]:
        pref=[A[0]]
        for i in range(1,n):
            pref.append(pref[-1]+A[i])
        s=[]
        res=[0]*(n+1)
        for i in range(n):
            if pref[i]>0:
                res[0]=i+1
                break
        for i in range(n-1,-1,-1):
            while s and pref[s[-1]]<=pref[i]:
                s.pop()
            if not s:
                res[i+1]=0
            elif i<n-1:
                res[i+1]=s[-1]-i
            s.append(i)
        res.pop()
        return res


