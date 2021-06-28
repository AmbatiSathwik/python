#my solution
class Solution:
    def removeDuplicates(self, s: str) -> str:
        def remove(S):
            l=[]
            i = 0
            while i < len(S):
                if i < len(S)-1 and S[i]==S[i+1]:
                    i += 1
                else:
                    l.append(S[i])
                i += 1
            a = ''
            for k in l:
                a += k
            return a
        
        while True:
            if s == remove(s):
                return s
            s = remove(s)
            
#optimum solution
class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        stack = []
        for char in s:
            if not stack or stack[-1]!= char:
                stack.append(char)
            elif stack[-1] == char:
                stack.pop()
        
        return "".join(stack)
