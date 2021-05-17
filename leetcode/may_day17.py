class Solution:
    d = []
    
    def long(self,i,n,edges):
        if self.d[i] > 0:
            return self.d[i]
        for j in range(n):
            if edges[i][j] == 1:
                self.d[i] = max(self.d[i],self.long(j,n,edges)+1)
        return self.d[i]
            
    
    def longestStrChain(self, words: List[str]) -> int:
        n = len(words)
        edges = [[0 for i in range(n)] for j in range(n)]
        self.d = [0 for i in range(n)]
        table = {}
        for i in range(n):
           table[words[i]] = i
        for i in range(n):
            strg1 = words[i]
            for j in range(len(strg1)):
                strg2 = strg1[:j] + strg1[j+1:]
                try:
                    #print(strg2)
                    pos = table[strg2]
                    #print(pos)
                    
                    edges[i][pos] = 1
                except:
                    continue
        ans = 0
        #print(edges)
        for i in range(n):
            ans = max(ans,self.long(i,n,edges))
        return ans+1
        
