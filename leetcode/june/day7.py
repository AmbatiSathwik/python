class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def cheap(cost,i,arr):
            count = 0
            if i >= len(cost):
                return count
            elif arr[i] != -1:
                return cost[i] + arr[i]
            else:
                count = min(cheap(cost,i+1,arr),cheap(cost,i+2,arr))
                arr[i] = count
                return count + cost[i]
            return count
        arr = [-1 for i in range(len(cost))]
        final = min(cheap(cost,0,arr),cheap(cost,1,arr))
        return final
