class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat)*len(mat[0]) != r*c:
            return mat
        m = [0 for i in range(len(mat)*len(mat[0]))]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                m[len(mat[0])*i + j] = mat[i][j]
        
        final = [[0 for i in range(c)]for j in range(r)]
        for i in range(len(m)):
            final[i//c][i%c] = m[i]
        return(final)
