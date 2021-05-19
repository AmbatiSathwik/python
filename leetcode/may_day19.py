class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        if n % 2 == 0:
            change1 = 0
            change2 = 0
            k1 = nums[n//2-1]
            k2 = nums[n//2]
            for num in nums:
                change1 += abs(k1 - num)
                change2 += abs(k2 - num)
            return min(change1,change2)
        else:
            change1 = 0
            k1 = nums[n//2]
            for num in nums:
                change1 += abs(k1 - num)
            return change1
