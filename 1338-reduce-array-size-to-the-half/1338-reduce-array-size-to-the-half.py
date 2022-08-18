class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d={}
        for i in arr:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        sorted_dt = {key: value for key, value in sorted(d.items(), key=lambda item: item[1],reverse=True)}
        print(sorted_dt)
        l=len(arr)
        tl=l//2
        c=0
        cl=list(sorted_dt.values())
        while tl>0:
            tl-=cl[c]
            c+=1
        return c    
        