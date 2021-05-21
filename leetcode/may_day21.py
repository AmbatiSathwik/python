class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        m = {}
        l = []
        k = ''
        for word in words:
            m.clear()
            check = 1
            k = ''
            for i in range(len(word)):
                try:
                    if m[pattern[i]] == word[i]:
                        continue
                    else:
                        check = 0
                        break
                except:
                    if word[i] in k:
                        check = 0
                        break
                    else:
                        m[pattern[i]] = word[i]
                        k += word[i]
           # print(k)
            if check == 1:
                l.append(word)
        return l
