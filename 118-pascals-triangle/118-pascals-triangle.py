class Solution:
    def generate(self, n: int) -> List[List[int]]:
        ans=[]
        for i in range(0,n):
            r=[None]*(i+1)
            r[0]=r[-1]=1
            for j in range(1,i):
                r[j]=ans[i-1][j-1]+ans[i-1][j]
            ans.append(r)    
        return ans
        