class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)
        if '0000' in visited:
            return -1
        graph = {
            '0' : ['9','1'],
            '1' : ['0','2'],
            '2' : ['1','3'],
            '3' : ['2','4'],
            '4' : ['3','5'],
            '5' : ['4','6'],
            '6' : ['5','7'],
            '7' : ['6','8'],
            '8' : ['7','9'],
            '9' : ['8','0'],
        }
        queue = ['0000']
        level = 0
        while len(queue) > 0:
            for _ in range(len(queue)):
                curr = queue.pop(0)
                if curr == target:
                    return level
                for i in range(4):
                    for nex in graph[curr[i]]:
                        nex = curr[:i] + nex + curr[i+1:]
                        if nex not in visited:
                            visited.add(nex)
                            queue.append(nex)
            level += 1
        return -1
                            
