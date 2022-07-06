class Solution:
    def generate(self, n: int) -> List[List[int]]:
        r=[0]*n
        for i in range(0,n):
            r[i]=[0]*(i+1)
            r[i][0]=1
            r[i][-1]=1
            for j in range(1,i):
                r[i][j]=(r[i-1][j-1]+r[i-1][j])

        return r
        