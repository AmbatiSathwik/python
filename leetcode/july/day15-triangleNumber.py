class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        nums.sort()
        for i in range(n-2):
            k = i + 2
            for j in range(i+1,n):
                while k < n and nums[i]+nums[j] > nums[k]:
                    k += 1
                if k > j:
                    count += k-j-1
        return count
            
