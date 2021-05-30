class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) < 2:
            return 0
        ma = 0
        for i in range(1,len(nums)):
            k = nums[i]-nums[i-1]
            if k>ma:
                ma = k
        return ma
