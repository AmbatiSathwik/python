class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                left = j + 1
                right = n - 1
                while left < right:
                    result = nums[i]+nums[j]+nums[left]+nums[right]
                    if result == target:
                        new = [nums[i],nums[j],nums[left],nums[right]]
                        if not new in res:
                            res.append(new)
                        
                        left += 1
                        right -= 1
                    
                    elif result < target:
                        left += 1
                    elif result > target:
                        right -= 1
        return res
