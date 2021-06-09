class Solution:
    def longestPalindrome(self, s: str) -> str:
        def longest(s,left,right):
            if s == None or left > right:
                return 0
            else:
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    left -= 1
                    right += 1
                return right-left-1
        
        if s == '':
            return ''
        else:
            start = 0
            end = 0
            for i in range(len(s)):
                le = max(longest(s,i,i),longest(s,i,i+1))
                if le > end-start:
                    start = i - (le-1)//2
                    end = i + le//2
        return s[start:end+1]
