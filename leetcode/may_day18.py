class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic = collections.defaultdict(list)
        for i in range(len(paths)):
            path = paths[i].split(' ')
            for j in range(1,len(path)):
                name, content = path[j].split('(')
                dic[content].append(path[0] + '/'+name)
        li = []
        for v in dic:
            if len(dic[v]) > 1:
                li.append(dic[v])
        return li
