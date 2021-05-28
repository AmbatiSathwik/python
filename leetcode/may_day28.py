class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        pre_sum = [0 for i in range(n+1)]
        for i in range(n):
            pre_sum[i+1] = pre_sum[i] + nums[i]
        s = 0
        ans = 0
        ma = [-1 for i in range(10001)]
        for i in range(n):
            s = max(s,ma[nums[i]]+1)
            ans = max(ans,pre_sum[i+1]-pre_sum[s])
            ma[nums[i]] = i
        return ans
