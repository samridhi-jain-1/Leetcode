class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        d={}
        c={}
        mx=0
        for i in range(len(nums)):
            k=nums[i]
            if k not in c:
                c[k]=1
                d[k]=[i]
            else:
                c[k]+=1
                d[k].append(i)
            mx=max(mx,c[k])
        res=len(nums)+1
        if mx==1:
            return 1
        
        for k,v in c.items():
         
            
            if(c[k]==mx):
               
                res=min(res,d[k][-1]-d[k][0]+1)
        return res  
            
        