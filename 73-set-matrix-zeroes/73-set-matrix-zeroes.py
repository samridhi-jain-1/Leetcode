class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r=0
        c=0
        rl=len(matrix)
        cl=len(matrix[0])
        for j in range(cl):
            if matrix[0][j]==0:
                r=1
        for i in range(rl):
            if matrix[i][0]==0:
                c=1
        for i in range(1,rl):
            for j in range(1,cl):
                if matrix[i][j]==0:
                    matrix[0][j]=0
                    matrix[i][0]=0
        for i in range(rl-1,0,-1):
            for j in range(cl-1,0,-1):
                if matrix[0][j]==0 or matrix[i][0]==0:
                    matrix[i][j]=0
        if r:
            for i in range(cl):
                matrix[0][i]=0
        if c:
            for i in range(rl):
                matrix[i][0]=0