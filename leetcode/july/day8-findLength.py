class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        def length(nums1,nums2):
            n1 = len(nums1)
            n2 = len(nums2)
            dp = [[0 for i in range(n2+1)]for j in range(n1+1)]
            ma = 0
            for i in reversed(range(n1)):
                for j in reversed(range(n2)):
                    if nums1[i] == nums2[j]:
                        dp[i][j] = dp[i+1][j+1] + 1
                        if dp[i][j] > ma:
                            ma = dp[i][j]
            return ma
        return(length(nums1,nums2))
            
                
