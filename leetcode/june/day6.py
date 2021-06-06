class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        co = 1
        if len(nums) > 1:
            prev = nums[0]
        elif len(nums) == 1:
            return 1
        else:
            return 0
        temp = 1
        for num in nums:
            
            if num == prev+1:
                temp += 1
                prev = num
                continue
            elif num == prev:
                continue
            else:
                if temp > co:
                    co = temp
                temp = 1
                prev = num
        if temp>co:
            co = temp
        return co
