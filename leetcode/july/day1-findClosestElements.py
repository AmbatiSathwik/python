class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        arr.sort(key = lambda num : abs(x-num))
        #print(arr)
        final = arr[:k]
        return (sorted(final))
