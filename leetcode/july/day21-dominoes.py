class Solution:
    def pushDominoes(self, d: str) -> str:
        n = len(d)
        forces = [0 for i in range(n)]
        present = 0
        start = 10**6
        for i in range(n):
            if d[i] == 'R':
                present = 1
                start = 10**6
                forces[i] = start
            elif d[i] == 'L':
                present = 0
                start = 0
                forces[i] = start
            elif d[i] == '.':
                if present == 1:
                    start -= 1
                    forces[i] = start
                else:
                    forces[i] = 0
                    
        present = 0
        start = -10**6
        for i in reversed(range(n)):
            if d[i] == 'L':
                present = 1
                start = -10**6
                forces[i] = start
            elif d[i] == 'R':
                present = 0
                start = -10**6
            elif d[i] == '.':
                if present:
                    start += 1
                    forces[i] += start
                else:
                    continue
        
        s = ''
        for val in forces:
            if val == 0:
                s += '.'
            elif val < 0:
                s += 'L'
            else:
                s += 'R'
        return s
