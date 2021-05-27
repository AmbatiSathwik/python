class Solution:
    def maxProduct(self, words: List[str]) -> int:
        final = []
        for i in range(len(words)):
            l = [words[i][j] for j in range(len(words[i]))]
            for j in range(i,len(words)):
                k = words[j]
                check = 1
                for it in range(len(l)):
                    if l[it] in k:
                        check = 0
                        break
                if check == 1:
                    final.append([words[i],words[j]])
        ma = 0
        for i in range(len(final)):
            pro = len(final[i][0])*len(final[i][1])
            if pro > ma:
                ma = pro
        return(ma)
                    
