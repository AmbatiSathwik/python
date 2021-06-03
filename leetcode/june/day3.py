class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        if not h in horizontalCuts:
            horizontalCuts.append(h)
        if not w in verticalCuts:
            verticalCuts.append(w)
        horizontalCuts.sort()
        verticalCuts.sort()
        hmax = 0
        for i in range(len(horizontalCuts)):
            temp = horizontalCuts[i]
            if i > 0:
                temp -= horizontalCuts[i-1]
            if temp > hmax:
                hmax = temp
        vmax = 0
        for i in range(len(verticalCuts)):
            temp = verticalCuts[i]
            if i > 0:
                temp -= verticalCuts[i-1]
            if temp > vmax:
                vmax = temp
        return (hmax*vmax)%(10**9 + 7)
        
        
