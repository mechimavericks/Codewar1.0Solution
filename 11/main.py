#Back-end complete function Template for Python 3
class Solution:
    
    def min_lights(self,hallway,n):
        lights = []
        for i in range(n):
            if hallway[i]>-1:
                lights.append( [i-hallway[i] , i+hallway[i]] );
        lights.sort()
        target=0
        lights_on=0
        i=0
        while(target<n):
            if i==len(lights) or lights[i][0]>target:
                return -1
            max_range = lights[i][1]
            while( i+1<len(lights) and lights[i+1][0]<=target ):
                i+=1
                max_range = max(max_range,lights[i][1])
            if max_range<target:
                return -1
            lights_on+=1
            target=max_range+1
            i+=1
        return lights_on
