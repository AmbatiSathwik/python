class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        n = len(searchWord)
        k = ""
        final = []
        for i in range(n):
            k += searchWord[i]
            mid = []
            l = 0
            for word in products:
                if l >= 3:
                    break
                if k == word[:len(k)]:
                    mid.append(word)
                    l += 1
            
            final.append(mid)
        return(final)
