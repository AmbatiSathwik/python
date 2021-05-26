class Solution:
    def minPartitions(self, n: str) -> int:
        l = []
        for k in n:
            l.append(int(k))
        return max(l)
