import math
class Solution:
    def minimumSum(self, s : str) -> int:
        # code here
        ans = 1e9
        n = len(s)
        for i in range(math.ceil(n/2)):
            if s[i] != s[n-i-1]:
                if s[i] == "?" or s[n-i-1] == "?":
                    if s[i] != "?":
                        s = s[:n-i-1] + s[i] + s[n-i-1+1:]
                    else:
                        s = s[:i] + s[n-i-1] + s[i+1:]
                else:
                    ans = -1
                    break
        
        if ans == -1:
            return ans
        
        idx, prev, cur, i = n-1, -1, -1, 0
        
        while i < math.ceil(n/2):
            if s[i] == "?":
                while i < math.ceil(n/2) and s[i] == "?":
                    i += 1
                    cur = i
                if prev == -1 and cur == (math.ceil(n/2)):
                    for j in range(math.ceil(n/2)):
                        s = s[:j] + "a" + s[j+1:]
                    if n & 1:
                        s = s[:math.ceil(n/2)] + "a" + s[(math.ceil(n/2))+1:]
                elif prev != -1 and cur == (math.ceil(n/2)):
                    for j in range(prev+1, cur):
                        s = s[:j] + s[prev] + s[j+1:]
                    if n & 1:
                        s = s[:(math.ceil(n/2))] + s[prev] + s[(math.ceil(n/2))+1:]
                elif prev == -1 and cur != (math.ceil(n/2)):
                    for j in range(cur):
                        s = s[:j] + s[cur] + s[j+1:]
                else:
                    dis = abs(ord(s[cur]) - ord(s[prev]))
                    prevChar, curChar = s[prev], s[cur]
                    if prevChar > curChar:
                        prevChar, curChar = curChar, prevChar
                    ch = ""
                    if dis == 0 or dis == 1:
                        ch = s[cur]
                    else:
                        dis = math.ceil(dis / 2)
                        ch = chr(ord(prevChar) + (dis))
                    for j in range(prev+1, cur):
                        s = s[:j] + ch + s[j+1:]
            else:
                prev = i
                i += 1
                
        for i in range(math.ceil(n/2)):
            s = s[:n-i-1] + s[i] + s[n-i-1+1:]
        
        ssum = 0
        for i in range(1, n):
            ssum += abs(ord(s[i]) - ord(s[i-1]))
        return ssum

