class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def ceil(arr,l,r,key):
            while r-l > 1:
                mid = l + (r-l)//2
                if arr[mid] < key:
                    l = mid
                else:
                    r = mid
            return r
        l = []
        n = len(nums)
        if n < 1:
            return l
        l.append(nums[0])
        for i in range(1,n):
            if nums[i] > l[-1]:
                l.append(nums[i])
            else:
                k = len(l)
                x = ceil(l,-1,k-1,nums[i])
                l[x] = nums[i]
        return len(l)
