class Solution:
    def toLowerCase(self, s: str) -> str:
        low = ''
        for ch in s:
            k = ord(ch)
            if k <= 90 and k >= 65:
                k = k + 32
            low += chr(k)
        print(low)
        return low
