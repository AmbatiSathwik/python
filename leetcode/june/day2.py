class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        def solve(s1,s2,s3,mat,i,j):
            k = False
            if s1 == '' and s2 == '' and s3 == '':
                return True
            if s3 == '':
                return False
            if mat[j][i] != -1:
                return True if mat[j][i] == 1 else False
            if s1 != '' and s1[0] == s3[0]:
                k = k or solve(s1[1:],s2,s3[1:],mat,i+1,j)
            if s2 != '' and s2[0] == s3[0]:
                k = k or solve(s1,s2[1:],s3[1:],mat,i,j+1)
            mat[j][i] = 1 if k else 0
            return k
        mat = [[-1 for i in range(len(s1)+1)]for j in range(len(s2)+1)]
        return solve(s1,s2,s3,mat,0,0)
