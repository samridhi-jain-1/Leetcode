class Solution:
    def generate(self, n: int) -> List[List[int]]:
        res=[[1]]
        for i in range(1,n):
            t=[0]+res[-1]+[0]
            r=[]
            for j in range(i+1):
                r.append(t[j]+t[j+1])
            res.append(r) 
        return res  
        