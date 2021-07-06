class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d = {}
        for num in arr:
            d[num] = d.get(num,0) + 1
        new_d = sorted(d.items(),key = lambda x:x[1], reverse = True)
        #print(new_d)
        n = len(arr)
        i = 0
        k = 0
        for key,value in new_d:
            k += 1
            
            i += value
        
            if i >= n//2:
                return k 
