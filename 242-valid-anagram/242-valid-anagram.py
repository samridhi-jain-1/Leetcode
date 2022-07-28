class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d={}
        for i in s:
            d[i]=d.get(i,0)+1
        for i in t:
            if i in d:
                d[i]-=1
            else:
                d[i]=1
        for k,v in d.items():
            if v is not 0:
                return False
        return True  